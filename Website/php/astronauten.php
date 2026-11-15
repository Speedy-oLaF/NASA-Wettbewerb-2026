<?php
// Gemeinsame Daten für die PHP-Skripte

// Ordner mit den Messdaten der Astronauten
$ordner = __DIR__ . "/../../Python/Astronauten/";

// Voller Name => Kürzel im Dateinamen (send_data_<kürzel>.json)
$astronauten = [
    "Reid Wiseman"   => "wiseman",
    "Victor Glover"  => "glover",
    "Christina Koch" => "koch",
    "Jeremy Hansen"  => "hansen",
];

// Liest eine JSON-Datei; bei fehlender, leerer oder kaputter Datei kommt $standard zurück
function json_lesen($datei, $standard = []) {
    if (!is_file($datei)) {
        return $standard;
    }
    $inhalt = file_get_contents($datei);
    if ($inhalt === false || trim($inhalt) === "") {
        return $standard;
    }
    $daten = json_decode($inhalt, true);
    return is_array($daten) ? $daten : $standard;
}
