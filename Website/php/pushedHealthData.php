
<?php


// Rückgängig-Funktion
if (isset($_POST['action']) && $_POST['action'] === 'undo') {

    $astronaut = $_POST['astronaut'] ?? '';
    $timestamp = $_POST['timestamp'] ?? '';

    $dateien = [
        "Glover" => "glover",
        "Hansen" => "hansen",
        "Koch" => "koch",
        "Wiseman" => "wiseman"
    ];

    if (isset($dateien[$astronaut]) && $timestamp !== '') {

        $file = __DIR__ . "/../../python/Astronauten/send_data_"
              . $dateien[$astronaut] . ".json";

        if (file_exists($file)) {

            $all_data = json_decode(file_get_contents($file), true) ?? [];

            // Genau den gerade gespeicherten Datensatz entfernen
            $all_data = array_values(array_filter($all_data, function ($entry) use ($timestamp) {
                return ($entry['timestamp'] ?? '') !== $timestamp;
            }));

            file_put_contents(
                $file,
                json_encode($all_data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE)
            );
        }
    }

    $zurueck = $_POST['return_url'] ?? '../sides/vitalMeasurements.html';

    // Nur lokale relative Pfade erlauben
    if (
        str_starts_with($zurueck, '/') ||
        str_starts_with($zurueck, 'http')
    ) {
        $zurueck = '../sides/vitalMeasurements.html';
    }

    header("Location: " . $zurueck);
    exit;
}




$data = $_POST;

$send_data = []; 
$send_data["timestamp"] = date("c");
$non_send_data = [];







foreach ($data as $key => $value) {

    if ($value === null or $value === "Not-Measured" || $value === "") {
        $non_send_data[$key] = $value;
    } else {
        $send_data[$key] = $value;
    }
}



$json = json_encode($send_data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);


if ($send_data["Astronaut-Name"] === "Glover") {
    $file = __DIR__ . "/../../python/Astronauten/send_data_glover.json";
    $returned_critical_data = file_get_contents("../../python/Astronauten/critical_data_glover.json");
} elseif ($send_data["Astronaut-Name"] === "Hansen") {
    $file = __DIR__ . "/../../python/Astronauten/send_data_hansen.json";
    $returned_critical_data = file_get_contents("../../python/Astronauten/critical_data_hansen.json");
} elseif ($send_data["Astronaut-Name"] === "Koch") {
    $file = __DIR__ . "/../../python/Astronauten/send_data_koch.json";
    $returned_critical_data = file_get_contents("../../python/Astronauten/critical_data_koch.json");
} elseif ($send_data["Astronaut-Name"] === "Wiseman") {
    $file = __DIR__ . "/../../python/Astronauten/send_data_wiseman.json";
    $returned_critical_data = file_get_contents("../../python/Astronauten/critical_data_wiseman.json");
}

$critical_data = json_decode($returned_critical_data, true);


$all_data = json_decode(file_get_contents($file), true);

$all_data[] = $send_data;

file_put_contents(
    $file,
    json_encode($all_data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE)
);


?>

<!DOCTYPE html>
<html lang="en">

<head>
<link rel="stylesheet"
      href="{{ url_for('static', filename='css/pico.min.css') }}">    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">


    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Main</title>
    <style>
        nav ul {
            display: flex;
            background-color: #2b2d2e;
            gap: 0px;
            border: 1px solid #343738;
        }

        #buttons-tr {
            display: flex;
            width: 100%;
            gap: 5px;
        }

        #buttons-tr td {
            flex: 1;
            display: flex;
        }

        #buttons-tr td button {
            width: 100%;
            flex: 1;
        }

    </style>
</head>

<body>
    <div class="wrapper">
        <header class="header">
            <h1>Health Monitoring Software</h1>
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
                    <h3>This Data will be pushed:</h3>
                    <table>
                        <?php foreach ($send_data as $key => $value): ?>
                        <tr>
                            <td><?= htmlspecialchars($key) ?></td>
                            <td><?= htmlspecialchars((string)$value) ?></td>
                        </tr>
                        <?php endforeach; ?>
                    </table>

                    <h3>This Data won't be pushed:</h3>
                    <table>
                        <?php foreach ($non_send_data as $key => $value): ?>
                        <tr>
                            <td><?= htmlspecialchars($key) ?></td>
                        </tr>
                        <?php endforeach; ?>
                    </table>      
                </article>
                <table>
                    <tr id="buttons-tr">
                        <td>
                            <form method="POST">
                                <input type="hidden" name="action" value="undo">

                                <input type="hidden" name="astronaut"
                                    value="<?= htmlspecialchars($send_data['Astronaut-Name']) ?>">

                                <input type="hidden" name="timestamp"
                                    value="<?= htmlspecialchars($send_data['timestamp']) ?>">

                                <input type="hidden" name="return_url"
                                    value="../sides/vitalMeasurements.html">

                                <button type="submit">Zurück</button>
                            </form>
                        </td>
                        <td><button type="button" onclick="window.location.href='auswertung.php'">Auswerten</button></td>
                    </tr>
                </table>
                 <h2>Gesendete Daten</h2>
                <pre>
                <?php print_r($send_data); ?>
                </pre>

                <h2>Nicht gesendete Daten</h2>
                <pre>
                <?php print_r($non_send_data); ?>
                </pre>

            </main>

        </div>
        <footer class="footer">
            <p>© 2026 Health Monitoring Software</p>
        </footer>



    </div>
    <script src="../sides/layout.js"></script>
</body>

</html>
