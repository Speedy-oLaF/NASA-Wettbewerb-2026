
<?php

$non_critical_data = [];
$send_data = [];
$critical_data = [];

// Ausgewählten Astronauten auslesen
$astronaut = $_GET['Astronaut'] ?? 'Glover';

// Dateinamen zuordnen
$dateien = [
    "Glover" => "glover",
    "Hansen" => "hansen",
    "Koch" => "koch",
    "Wiseman" => "wiseman"
];

// Prüfen, ob der Astronaut existiert
if (!isset($dateien[$astronaut])) {
    $astronaut = "Glover";
}

$name = $dateien[$astronaut];

// Richtige JSON-Dateien laden
$ordner = __DIR__ . "/../../Python/Astronauten/";

$file = $ordner . "send_data_" . $name . ".json";
$returned_critical_data = $ordner . "critical_data_" . $name . ".json";

// JSON-Dateien sicher einlesen
if (file_exists($file)) {
    $decoded = json_decode(file_get_contents($file), true);
    $send_data = is_array($decoded) ? $decoded : [];
}

if (file_exists($returned_critical_data)) {
    $decoded = json_decode(file_get_contents($returned_critical_data), true);
    $critical_data = is_array($decoded) ? $decoded : [];
}

// Funktion: Neueste Messung finden
function neuesteMessung($daten) {

    if (empty($daten)) {
        return [];
    }

    // Nur gültige Datensätze mit Zeitstempel behalten
    $daten = array_filter($daten, function ($eintrag) {
        return is_array($eintrag) && !empty($eintrag['timestamp']);
    });

    if (empty($daten)) {
        return [];
    }

    // Neueste Messung zuerst
    usort($daten, function ($a, $b) {
        return strtotime($b['timestamp']) <=> strtotime($a['timestamp']);
    });

    return $daten[0];
}

// Neueste Messungen auswählen
$send_data = neuesteMessung($send_data);

// Critical Data prüfen
$hatCriticalData = !empty($critical_data['alarm'])
    && !empty($critical_data['warnings']);

// Non-Critical Data berechnen
foreach ($send_data as $key => $element) {

    // Zeitstempel und Astronautenname überspringen
    if ($key === 'timestamp' || $key === 'Astronaut-Name') {
        continue;
    }

    // Prüfen, ob der Messwert kritisch ist
    if (!array_key_exists($key, $critical_data)) {
        $non_critical_data[$key] = $element;
    }
}

?>

<!DOCTYPE html>
<html lang="de">

<head>
  <link rel="stylesheet"href="{{ url_for('static', filename='css/pico.min.css') }}">
  <link rel="stylesheet" href="../css/pico-main/css/pico.min.css">
  <link rel="stylesheet" href="../css/design.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auswertung</title>

    <style>
        nav ul {
            display: flex;
            background-color: #2b2d2e;
            gap: 0px;
            border: 1px solid #343738;
        }
    </style>
</head>

<body>
    <div class="wrapper">

        <header class="header">
            <h1>Auswertung</h1>
        </header>

        <div class="content">

            <nav class="nav">
                <aside>
                    <ul>
                        <li><a href="../index.html">Home</a></li>
                        <li><a href="../sides/vitalMeasurements.html">Messen</a></li>
                        <li><a href="auswertung.php">Auswertung</a></li>
                        <li><a href="../sides/symptome.html">Symptome</a></li>
                        <li><a href="../sides/verlauf.html">Verlauf</a></li>
                        <li><a href="../sides/training.html">Training</a></li>
                        <li><a href="../sides/flugarzt.html">Flugarzt</a></li>
                    </ul>
                </aside>
            </nav>

            <main class="main">
                <article>

                    <form method="GET" action="auswertung.php">
                        <select name="Astronaut"
                                id="Astronaut"
                                onchange="this.form.submit()">

                            <?php foreach (["Glover", "Hansen", "Koch", "Wiseman"] as $option): ?>
                                <option value="<?= htmlspecialchars($option) ?>"
                                    <?= $astronaut === $option ? 'selected' : '' ?>>
                                    <?= htmlspecialchars($option) ?>
                                </option>
                            <?php endforeach; ?>

                        </select>
                    </form>

                    <h3>CRITICAL Data:</h3>

                    <?php if (!$hatCriticalData): ?>

                        <p>No critical data recognized.</p>

                    <?php else: ?>

                        <p><strong>Alarm aktiv!</strong></p>

                        <ul>
                            <?php foreach ($critical_data['warnings'] as $warning): ?>
                                <li><?= htmlspecialchars($warning) ?></li>
                            <?php endforeach; ?>
                        </ul>

                    <?php endif; ?>

                    <h3>NON-CRITICAL Data:</h3>

                    <table>
                        <?php foreach ($non_critical_data as $key => $value): ?>
                            <tr>
                                <td><?= htmlspecialchars((string)$key) ?></td>
                                <td><?= htmlspecialchars((string)$value) ?></td>
                            </tr>
                        <?php endforeach; ?>
                    </table>

                </article>
            </main>
        </div>

        <footer class="footer">
            <p>© 2026 Health Monitoring Software</p>
        </footer>

    </div>
    <script src="../sides/layout.js"></script>
</body>
</html>
