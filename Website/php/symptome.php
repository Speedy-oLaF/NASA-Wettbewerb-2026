<?php
// Symptom-Berichte für den Flugarzt in Python/symptome.json
//
//   POST (JSON) neuer Bericht:
//     { "astronaut": "...", "symptome": ["kopf", ...], "stufe": 1 }
//   POST (JSON) Bericht erledigt / wieder offen:
//     { "aktion": "erledigt", "id": "...", "erledigt": true }
//   GET ?api=1 : alle Berichte
//   GET ?astronauten=1 : Liste der erlaubten Astronauten-Namen
require __DIR__ . "/astronauten.php";

header("Content-Type: application/json; charset=UTF-8");
header("Cache-Control: no-store");

$datei = __DIR__ . "/../../Python/symptome.json";

// Erlaubte Symptom-IDs (wie in symptome.js)
$erlaubt = ["brust", "atem", "verwirrt", "kopf", "sehen", "schwindel",
            "uebel", "fieber", "ruecken", "flanke", "muede", "traurig"];

function fehler($code, $text) {
    http_response_code($code);
    echo json_encode(["error" => $text], JSON_UNESCAPED_UNICODE);
    exit;
}

// Öffnet symptome.json gesperrt, lässt $aendern die Liste bearbeiten und speichert
function berichte_bearbeiten($datei, $aendern) {
    $handle = fopen($datei, "c+");
    if (!$handle || !flock($handle, LOCK_EX)) {
        fehler(500, "Speicher nicht verfügbar");
    }
    $daten = json_decode(stream_get_contents($handle) ?: "[]", true);
    if (!is_array($daten)) {
        $daten = [];
    }

    // Ältere Berichte ohne ID / Status nachrüsten
    foreach ($daten as $i => $b) {
        if (!isset($b["id"])) $daten[$i]["id"] = "alt-" . $i;
        if (!isset($b["erledigt"])) $daten[$i]["erledigt"] = false;
    }

    $ergebnis = $aendern($daten);

    rewind($handle);
    ftruncate($handle, 0);
    fwrite($handle, json_encode($daten, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE));
    fflush($handle);
    flock($handle, LOCK_UN);
    fclose($handle);
    return $ergebnis;
}

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $eingabe = json_decode(file_get_contents("php://input"), true);
    if (!is_array($eingabe)) {
        fehler(400, "Keine gültigen JSON-Daten");
    }

    // --- Bericht als erledigt / offen markieren ---
    if (($eingabe["aktion"] ?? "") === "erledigt") {
        $id = (string)($eingabe["id"] ?? "");
        $erledigt = (bool)($eingabe["erledigt"] ?? true);

        $bericht = berichte_bearbeiten($datei, function (&$daten) use ($id, $erledigt) {
            foreach ($daten as $i => $b) {
                if ($b["id"] === $id) {
                    $daten[$i]["erledigt"] = $erledigt;
                    $daten[$i]["erledigt_am"] = $erledigt ? date("c") : null;
                    return $daten[$i];
                }
            }
            return null;
        });

        if ($bericht === null) {
            fehler(404, "Bericht nicht gefunden");
        }
        echo json_encode(["ok" => true, "bericht" => $bericht], JSON_UNESCAPED_UNICODE);
        exit;
    }

    // --- Neuer Bericht ---
    $name = $eingabe["astronaut"] ?? "";
    $symptome = $eingabe["symptome"] ?? [];
    $stufe = (int)($eingabe["stufe"] ?? 0);

    if (!isset($astronauten[$name])) {
        fehler(400, "Unbekannter Astronaut");
    }
    if (!is_array($symptome) || count($symptome) === 0 ||
        count(array_diff($symptome, $erlaubt)) > 0 || $stufe < 1 || $stufe > 3) {
        fehler(400, "Ungültige Symptome");
    }

    $bericht = [
        "id"            => bin2hex(random_bytes(6)),
        "astronautName" => $name,
        "symptome"      => array_values(array_unique($symptome)),
        "stufe"         => $stufe,
        "timestamp"     => date("c"),
        "erledigt"      => false,
    ];

    berichte_bearbeiten($datei, function (&$daten) use ($bericht) {
        $daten[] = $bericht;
    });

    echo json_encode(["ok" => true, "bericht" => $bericht], JSON_UNESCAPED_UNICODE);
    exit;
}

if (isset($_GET["astronauten"])) {
    echo json_encode(array_keys($astronauten), JSON_UNESCAPED_UNICODE);
    exit;
}

if (isset($_GET["api"])) {
    $daten = json_lesen($datei, []);
    foreach ($daten as $i => $b) {
        if (!isset($b["id"])) $daten[$i]["id"] = "alt-" . $i;
        if (!isset($b["erledigt"])) $daten[$i]["erledigt"] = false;
    }
    echo json_encode($daten, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
    exit;
}

fehler(400, "POST oder ?api=1 verwenden");
