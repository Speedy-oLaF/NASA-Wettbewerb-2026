
<?php
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
    <link rel="stylesheet" href="../css/design.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='../css/design.css') }}">


    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Main</title>

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
                        <li><a href="../sides/symthome.html">Symptome</a></li>
                        <li><a href="../sides/verlauf.html">Verlauf</a></li>
                        <li><a href="../sides/training.html">Training</a></li>
                    </ul>
                </aside>
            </nav>


            <main class="main">
                <article>
                    <h3>CRITICAL Data:</h3>
                    <table>
                        <?php foreach ($critical_data as $key => $value): ?>
                            <?php if (is_array($value)): ?>
                                <?php foreach ($value as $element): ?>
                                    <tr>
                                        <td>
                                            <?= htmlspecialchars(
                                                is_array($element)
                                                    ? print_r($element, true)
                                                    : (string)$element
                                            ) ?>
                                        </td>
                                    </tr>
                                <?php endforeach; ?>
                            <?php endif; ?>
                        <?php endforeach; ?>
                    </table>


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
                <button type="button" onclick="history.back()">Zurück</button>
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
</body>

</html>
