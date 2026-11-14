
<?php
$data = $_POST;

$send_data = [];
$non_send_data = [];

foreach ($data as $key => $value) {

    if ($value === null || $value === "") {
        $non_send_data[$key] = $value;
    } else {
        $send_data[$key] = $value;
    }
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <link rel="stylesheet" href="design.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">
    <link rel="stylesheet" href="{{ url_for('static', filename='design.css') }}">


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
                        <li><a href="index.html">Home</a></li>
                        <li><a href="vitalMeasurements.html">Messen</a></li>
                        <li><a href="auswertung.html">Auswertung</a></li>
                        <li><a href="symthome.html">Symptome</a></li>
                        <li><a href="verlauf.html">Verlauf</a></li>
                        <li><a href="training.html">Training</a></li>
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
