<?php
header("Content-Type: application/json");
$python = "python";   // falls nötig: voller Pfad zur python.exe
echo shell_exec($python . " " . escapeshellarg(__DIR__ . "../../Python/daten.py"));
