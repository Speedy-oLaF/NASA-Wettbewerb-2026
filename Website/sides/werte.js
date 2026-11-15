// Anzeigenamen und Einheiten der Messwerte (gemeinsam für Auswertung und Verlauf)
const WERTE = {
    herzfrequenz:             { label: "Heart rate",               einheit: "bpm" },
    blutdruck:                { label: "Blood pressure",           einheit: "mmHg" },
    koerpertemperatur:        { label: "Body temperature",         einheit: "°C" },
    sauerstoffsaettigung:     { label: "Oxygen saturation",        einheit: "%" },
    sauerstoffsaetigung:      { label: "Oxygen saturation",        einheit: "%" },
    schlafdauer:              { label: "Sleep",                    einheit: "h" },
    knochendichte:            { label: "Bone density",             einheit: "g/cm²" },
    anfangs_knochendichte:    { label: "Initial bone density",     einheit: "g/cm²" },
    muskelkraft:              { label: "Muscle strength",          einheit: "N" },
    ausgangswert_muskelkraft: { label: "Initial muscle strength",  einheit: "N" },
    sport:                    { label: "Sport",                    einheit: "h" },
    ernaehrung:               { label: "Nutrition",                einheit: "kcal" },
    strahlungsbelastung:      { label: "Radiation",                einheit: "mSv" },
};

function wertLabel(schluessel) {
    return WERTE[schluessel] ? WERTE[schluessel].label : schluessel;
}

function datumFormatieren(iso) {
    if (!iso) return "–";
    const datum = new Date(iso);
    return isNaN(datum) ? iso : datum.toLocaleString("de-DE");
}

// ---------------------------------------------------------------
// Kennzahlen für das Diagramm im Verlauf.
// Die Grenzwerte sind dieselben wie in Python/Auswertung.py –
// wenn du dort etwas änderst, bitte auch hier anpassen!
// [untere Grenze, obere Grenze], null = keine Grenze
// ---------------------------------------------------------------
function zahlOderNull(wert) {
    if (wert === null || wert === undefined || wert === "") return null;
    const z = Number(wert);
    return Number.isFinite(z) ? z : null;
}

function blutdruckTeil(messung, index) {
    const teile = String(messung.blutdruck || "").split("/");
    return teile.length === 2 ? zahlOderNull(teile[index]) : null;
}

function prozentVon(aktuell, anfang) {
    const a = zahlOderNull(aktuell);
    const b = zahlOderNull(anfang);
    return a === null || !b ? null : Math.round((a / b) * 1000) / 10;
}

const KENNZAHLEN = [
    { id: "herzfrequenz", label: "Heart rate", einheit: "bpm",
      serien: [{ name: "Heart rate", wert: m => zahlOderNull(m.herzfrequenz) }],
      grenzen: { innen: [[50, 130]], aussen: [[50, 120]] } },

    { id: "blutdruck", label: "Blood pressure", einheit: "mmHg",
      serien: [
          { name: "Systolic",  wert: m => blutdruckTeil(m, 0) },
          { name: "Diastolic", wert: m => blutdruckTeil(m, 1) },
      ],
      grenzen: { innen: [[90, 140], [60, 90]], aussen: [[90, 135], [60, 85]] } },

    { id: "koerpertemperatur", label: "Body temperature", einheit: "°C",
      serien: [{ name: "Body temperature", wert: m => zahlOderNull(m.koerpertemperatur) }],
      grenzen: { innen: [[35.5, 37.5]], aussen: [[35.8, 37.3]] } },

    { id: "sauerstoffsaettigung", label: "Oxygen saturation", einheit: "%",
      serien: [{ name: "Oxygen saturation", wert: m => zahlOderNull(m.sauerstoffsaettigung) }],
      grenzen: { innen: [[92, null]], aussen: [[95, null]] } },

    { id: "schlafdauer", label: "Sleep", einheit: "h",
      serien: [{ name: "Sleep", wert: m => zahlOderNull(m.schlafdauer) }],
      grenzen: { innen: [[6, null]], aussen: [[7, null]] } },

    { id: "knochendichte", label: "Bone density (of initial)", einheit: "%",
      serien: [{ name: "Bone density", wert: m => prozentVon(m.knochendichte, m.anfangs_knochendichte) }],
      grenzen: { innen: [[90, null]], aussen: [[95, null]] } },

    { id: "muskelkraft", label: "Muscle strength (of initial)", einheit: "%",
      serien: [{ name: "Muscle strength", wert: m => prozentVon(m.muskelkraft, m.ausgangswert_muskelkraft) }],
      grenzen: { innen: [[80, null]], aussen: [[90, null]] } },

    { id: "sport", label: "Sport", einheit: "h",
      serien: [{ name: "Sport", wert: m => zahlOderNull(m.sport) }],
      grenzen: { innen: [[1.5, null]], aussen: [[1.5, null]] } },

    { id: "ernaehrung", label: "Nutrition", einheit: "kcal",
      serien: [{ name: "Nutrition", wert: m => zahlOderNull(m.ernaehrung) }],
      grenzen: { innen: [[2000, 3200]], aussen: [[2500, 3800]] } },

    { id: "strahlungsbelastung", label: "Radiation", einheit: "mSv",
      serien: [{ name: "Radiation", wert: m => zahlOderNull(m.strahlungsbelastung) }],
      grenzen: { innen: [[null, 1.3]], aussen: [[null, 0.9]] } },
];

function imBereich(wert, grenze) {
    if (wert === null || !grenze) return true;
    const [unten, oben] = grenze;
    return (unten === null || wert >= unten) && (oben === null || wert <= oben);
}
