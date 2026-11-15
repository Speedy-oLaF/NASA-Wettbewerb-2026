<?php

$non_critical_data = [];
$send_data = [];
$critical_data = [];

$astronaut = $_GET['Astronaut'] ?? 'Glover';

if ($astronaut === "Glover") {
    $file = "../../python/Astronauten/send_data_glover.json";
    $returned_critical_data = "../../python/Astronauten/critical_data_glover.json";

} elseif ($astronaut === "Hansen") {
    $file = "../../python/Astronauten/send_data_hansen.json";
    $returned_critical_data = "../../python/Astronauten/critical_data_hansen.json";

} elseif ($astronaut === "Koch") {
    $file = "../../python/Astronauten/send_data_koch.json";
    $returned_critical_data = "../../python/Astronauten/critical_data_koch.json";

} elseif ($astronaut === "Wiseman") {
    $file = "../../python/Astronauten/send_data_wiseman.json";
    $returned_critical_data = "../../python/Astronauten/critical_data_wiseman.json";
}

$send_data = json_decode(file_get_contents($file), true) ?? [];
$critical_data = json_decode(file_get_contents($returned_critical_data), true) ?? [];

foreach ($send_data as $element) {
    $found = false;

    foreach ($critical_data as $value) {
        if (is_array($value) && in_array($element, $value, true)) {
            $found = true;
            break;
        }
    }

    if (!$found) {
        $non_critical_data[] = $element;
    }
}

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
            <h1>Auswertung</h1>
        </header>


        <div class="content">
            <nav class="nav">
                <aside>
                    <ul>
                        <li><a href="../index.html">Home</a></li>
                        <li><a href="../sides/vitalMeasurements.html">Messen</a></li>
                        <li><a href="../php/auswertung.php">Auswertung</a></li>
                        <li><a href="../sides/symptome.html">Symptome</a></li>
                        <li><a href="../sides/verlauf.html">Verlauf</a></li>
                        <li><a href="../sides/training.html">Training</a></li>
                    </ul>
                </aside>
            </nav>


            <main class="main">
                <article>
                    <form method="GET">
                        <select name="Astronaut" id="Astronaut" onchange="this.form.submit()">
                            <option value="Glover">Glover</option>
                            <option value="Hansen">Hansen</option>
                            <option value="Koch">Koch</option>
                            <option value="Wiseman">Wiseman</option>
                        </select>
                    </form>
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

                    <h3>NON-CRITICAL Data:</h3>
                    <table>
                        <?php foreach ($non_critical_data as $key => $value): ?>
                            <tr>
                                <td><?= htmlspecialchars($key) ?></td>
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
</body>


</html>