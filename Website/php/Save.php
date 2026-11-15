<?
    $beispiel = htmlspecialchars($daten);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
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
   
    <p>Die Methode des Requests war: <?= $methode ?> </p>
    <p>Die Methode des Requests war: <?= print_r($daten) ?> </p>
    <p>Die Methode des Requests war: <?= $daten['name'] ?> </p>
    <p>Die Methode des Requests war: <?= $name ?> </p>
    <p>Die Methode des Requests war: <?= $art ?> </p>
    <p>Security: <?= $beispiel ?> </p>
    <a href="../formular.html">zurück zum Formular</a>
</body>
</html>