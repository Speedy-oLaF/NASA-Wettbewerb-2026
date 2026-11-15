// =========================================================
// Gemeinsame Symptom-Liste für symptome.html und flugarzt.html
// Dringlichkeit (stufe): 1 = beobachten, 2 = heute Flugarzt, 3 = Notfall
// Neue Symptom-IDs bitte auch in symptome.php ($erlaubt) eintragen.
// =========================================================

const SYMPTOME = [
  { id: "brust",    name: "Brustschmerz",     stufe: 3, messen: ["bp", "hr", "spo2"], ursache: "Herzproblem, manchmal nur Muskelschmerz",  tipp: "Notfall-Ablauf öffnen, AED bereitlegen" },
  { id: "atem",     name: "Atemnot",          stufe: 2, messen: ["spo2", "hr"],       ursache: "zu viel CO₂ in der Kabinenluft",           tipp: "Sauerstoffmaske bereithalten, CO₂-Anzeige prüfen" },
  { id: "verwirrt", name: "Verwirrtheit",     stufe: 3, messen: ["glu", "spo2"],      ursache: "Unterzuckerung oder Sauerstoffmangel",     tipp: "Person nicht allein lassen" },
  { id: "kopf",     name: "Kopfschmerz",      stufe: 1, messen: ["spo2", "bp"],       ursache: "CO₂ in der Kabinenluft",                   tipp: "Ort mit guter Lüftung aufsuchen, 500 ml trinken" },
  { id: "sehen",    name: "Sehstörung",       stufe: 2, messen: ["bp"],               ursache: "Druck auf den Sehnerv durch Schwerelosigkeit", tipp: "Sehtest-Tafel machen" },
  { id: "schwindel",name: "Schwindel",        stufe: 1, messen: ["bp", "glu"],        ursache: "Raumkrankheit oder niedriger Blutdruck",   tipp: "Hinsetzen bzw. festhalten, Kopf langsam bewegen" },
  { id: "uebel",    name: "Übelkeit",         stufe: 1, messen: ["temp"],             ursache: "Raumkrankheit",                            tipp: "Spucktüte bereithalten" },
  { id: "fieber",   name: "Fieber",           stufe: 1, messen: ["temp", "hr"],       ursache: "Infekt – das Immunsystem ist im All schwächer", tipp: "Viel trinken, Abstand zur Crew halten" },
  { id: "ruecken",  name: "Rückenschmerz",    stufe: 1, messen: ["train"],            ursache: "Wirbelsäule streckt sich in Schwerelosigkeit", tipp: "Knie zur Brust ziehen, dehnen" },
  { id: "flanke",   name: "Flankenschmerz",   stufe: 2, messen: ["temp"],             ursache: "Nierenstein durch Knochenabbau",           tipp: "Viel trinken" },
  { id: "muede",    name: "Starke Müdigkeit", stufe: 1, messen: ["sleep", "temp"],    ursache: "Schlafmangel",                             tipp: "Pause einlegen, früher schlafen" },
  { id: "traurig",  name: "Niedergeschlagen", stufe: 1, messen: ["mood"],             ursache: "Isolation, weit weg von zu Hause",         tipp: "Mit jemandem sprechen" }
];

const STUFEN = {
  1: { farbe: "info", symbol: "ℹ", titel: "Beobachten",                text: "Werte messen. Wird es schlimmer, noch einmal prüfen." },
  2: { farbe: "warn", symbol: "⚠", titel: "Heute den Flugarzt fragen", text: "Werte messen und dem Flugarzt einen Bericht schicken." },
  3: { farbe: "crit", symbol: "✚", titel: "Notfall – jetzt handeln",   text: "Crew alarmieren und den Notfall-Ablauf öffnen." }
};
