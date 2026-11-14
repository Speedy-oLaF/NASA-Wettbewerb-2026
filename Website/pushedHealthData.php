
<?php

$file = __DIR__ . "/../python/neil.json";

// JSON-Datei erstellen, falls sie noch nicht existiert
if (!file_exists($file)) {
    file_put_contents($file, "[]");
}

$message = "";

// POST: Neue Daten speichern
if ($_SERVER["REQUEST_METHOD"] === "POST") {

    header("Content-Type: application/json; charset=UTF-8");

    $required = [
        "astronautName",
        "herzfrequenz",
        "blutdruck",
        "koerpertemperatur",
        "sauerstoffsaettigung",
        "schlafdauer",
        "knochendichte",
        "anfangs_knochendichte",
        "muskelkraft",
        "ausgangswert_muskelkraft",
        "sport",
        "strahlungsbelastung",
        "bereich"
    ];

    $newData = [
        "astronautName" => $_POST["astronautName"] ?? null,
        "herzfrequenz" => ($_POST["herzfrequenz"] ?? "") !== "" ? (int)$_POST["herzfrequenz"] : null,
        "blutdruck" => ($_POST["blutdruck"] ?? "") !== "" ? $_POST["blutdruck"] : null,
        "koerpertemperatur" => ($_POST["koerpertemperatur"] ?? "") !== "" ? (float)$_POST["koerpertemperatur"] : null,
        "sauerstoffsaettigung" => ($_POST["sauerstoffsaettigung"] ?? "") !== "" ? (float)$_POST["sauerstoffsaettigung"] : null,
        "schlafdauer" => ($_POST["schlafdauer"] ?? "") !== "" ? (float)$_POST["schlafdauer"] : null,
        "knochendichte" => ($_POST["knochendichte"] ?? "") !== "" ? (float)$_POST["knochendichte"] : null,
        "anfangs_knochendichte" => ($_POST["anfangs_knochendichte"] ?? "") !== "" ? (float)$_POST["anfangs_knochendichte"] : null,
        "muskelkraft" => ($_POST["muskelkraft"] ?? "") !== "" ? (float)$_POST["muskelkraft"] : null,
        "ausgangswert_muskelkraft" => ($_POST["ausgangswert_muskelkraft"] ?? "") !== "" ? (float)$_POST["ausgangswert_muskelkraft"] : null,
        "sport" => ($_POST["sport"] ?? "") !== "" ? (float)$_POST["sport"] : null,
        "strahlungsbelastung" => ($_POST["strahlungsbelastung"] ?? "") !== "" ? (float)$_POST["strahlungsbelastung"] : null,
        "bereich" => ($_POST["bereich"] ?? "") !== "" ? (int)$_POST["bereich"] : null,
        "timestamp" => date("c")
    ];

    $handle = fopen($file, "c+");

    if (!$handle || !flock($handle, LOCK_EX)) {
        http_response_code(500);
        echo json_encode(["error" => "Storage unavailable"]);
        exit;
    }

    $content = stream_get_contents($handle);
    $data = json_decode($content ?: "[]", true);

    if (!is_array($data) || json_last_error() !== JSON_ERROR_NONE) {
        flock($handle, LOCK_UN);
        fclose($handle);
        http_response_code(500);
        echo json_encode(["error" => "Invalid JSON"]);
        exit;
    }

    $data[] = $newData;

    rewind($handle);
    ftruncate($handle, 0);

    fwrite($handle, json_encode(
        $data,
        JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE
    ));

    fflush($handle);
    flock($handle, LOCK_UN);
    fclose($handle);

    // Nach erfolgreichem Speichern zurück zur Website
    header("Location: " . strtok($_SERVER["REQUEST_URI"], "?") . "?success=1");
    exit;
}

// GET: JSON-API nur bei explizitem api-Aufruf
if (isset($_GET["api"])) {

    header("Content-Type: application/json; charset=UTF-8");

    $data = json_decode(file_get_contents($file), true);



    echo json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
    exit;
}

?>

<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NASA Health Data</title>
</head>
<body>

    <h1>NASA Health Data</h1>

    <?php if (isset($_GET["success"])): ?>
        <p style="color: green;">
            Daten erfolgreich gespeichert!
        </p>
    <?php endif; ?>

    <p>Hier kannst du deine Astronautendaten verwalten.</p>

    <a href="vitalMeasurements.html">
        Zum Formular
    </a>

    <br><br>

    <a href="?api=1">
        JSON API öffnen
    </a>

</body>
</html>
