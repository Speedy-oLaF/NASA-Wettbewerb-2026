const UEBUNGEN = {
    aufwaermen: {
        name: "Dynamic warm-up",
        geraet: "No equipment",
        umfang: "10 min",
        dauer: 10,
        art: "Mobility",
        warum: "Prepares joints and muscles, lowers injury risk in microgravity.",
    },
    laufband: {
        name: "Treadmill run with harness",
        geraet: "Treadmill + bungee harness",
        umfang: "30 min · moderate pace",
        dauer: 30,
        art: "Cardio",
        warum: "Keeps heart and lungs fit; the harness loads legs and spine.",
    },
    ergometerIntervalle: {
        name: "Cycle ergometer intervals",
        geraet: "Cycle ergometer",
        umfang: "4 × 4 min hard / 3 min easy",
        dauer: 30,
        art: "Cardio",
        warum: "Short hard intervals keep VO₂max up efficiently.",
    },
    ergometerLeicht: {
        name: "Easy cycling",
        geraet: "Cycle ergometer",
        umfang: "20 min · easy, can still talk",
        dauer: 20,
        art: "Cardio",
        warum: "Light movement without stressing the body on a recovery day.",
    },
    extraCardio: {
        name: "Extra cardio block",
        geraet: "Cycle ergometer",
        umfang: "15 min · moderate",
        dauer: 15,
        art: "Cardio",
        warum: "Makes up for too little exercise in the last measurement.",
    },
    kniebeugen: {
        name: "Squats",
        geraet: "Resistance device",
        umfang: "4 × 8 reps",
        dauer: 15,
        art: "Strength",
        warum: "Biggest lever against loss of leg muscle and hip bone density.",
    },
    kreuzheben: {
        name: "Deadlifts",
        geraet: "Resistance device",
        umfang: "3 × 8 reps",
        dauer: 15,
        art: "Strength",
        warum: "Loads spine and hips; protects the lower back.",
    },
    bankdruecken: {
        name: "Bench press",
        geraet: "Resistance device",
        umfang: "3 × 10 reps",
        dauer: 12,
        art: "Strength",
        warum: "Maintains upper-body strength needed for EVA work.",
    },
    rudern: {
        name: "Bent-over rows",
        geraet: "Resistance device",
        umfang: "3 × 10 reps",
        dauer: 10,
        art: "Strength",
        warum: "Extra pulling work to rebuild lost muscle strength.",
    },
    wadenheben: {
        name: "Heel raises",
        geraet: "Resistance device",
        umfang: "3 × 15 reps",
        dauer: 8,
        art: "Strength",
        warum: "Calf muscles shrink fastest in weightlessness.",
    },
    spruenge: {
        name: "Impact hops",
        geraet: "Treadmill + harness",
        umfang: "5 × 20 small hops",
        dauer: 8,
        art: "Bone",
        warum: "Short impacts are the strongest signal for bones to stay dense.",
    },
    schwereKniebeugen: {
        name: "Heavy squats",
        geraet: "Resistance device",
        umfang: "5 × 5 reps · heavy",
        dauer: 12,
        art: "Bone",
        warum: "High load stimulates bone growth in hips and spine.",
    },
    dehnen: {
        name: "Stretching",
        geraet: "No equipment",
        umfang: "10 min",
        dauer: 10,
        art: "Recovery",
        warum: "Keeps muscles flexible; the spine lengthens in space.",
    },
    atmung: {
        name: "Breathing & relaxation",
        geraet: "No equipment",
        umfang: "5 min · slow breathing",
        dauer: 5,
        art: "Recovery",
        warum: "Lowers heart rate and stress, helps sleep.",
    },
};

const WOCHE = [
    { tag: "Sun", fokus: "Recovery",          text: "Stretching, easy cycling" },
    { tag: "Mon", fokus: "Cardio + upper",    text: "Treadmill, bench press, rows" },
    { tag: "Tue", fokus: "Legs + bone",       text: "Squats, impact hops, heel raises" },
    { tag: "Wed", fokus: "Intervals",         text: "Cycle ergometer intervals" },
    { tag: "Thu", fokus: "Upper + core",      text: "Bench press, rows, deadlifts" },
    { tag: "Fri", fokus: "Legs + bone",       text: "Heavy squats, impact hops" },
    { tag: "Sat", fokus: "Long cardio",       text: "Treadmill 45 min" },
];

// Ziel aus Auswertung.py: mindestens 1,5 h Sport
const SPORT_ZIEL_STUNDEN = 1.5;

function planErstellen(messung, datum = new Date()) {
    const hinweise = [];

    if (!messung) {
        hinweise.push({ art: "info", text: "No measurement up to this day – showing the standard plan." });
        return { plan: standardPlan(datum), hinweise, leichterTag: false };
    }

    const herz = zahlOderNull(messung.herzfrequenz);
    const temp = zahlOderNull(messung.koerpertemperatur);
    const sauerstoff = zahlOderNull(messung.sauerstoffsaettigung);
    const schlaf = zahlOderNull(messung.schlafdauer);
    const sport = zahlOderNull(messung.sport);
    const strahlung = zahlOderNull(messung.strahlungsbelastung);
    const muskelProzent = prozentVon(messung.muskelkraft, messung.ausgangswert_muskelkraft);
    const knochenProzent = prozentVon(messung.knochendichte, messung.anfangs_knochendichte);

    const gruende = [];
    if (herz !== null && (herz > 120 || herz < 50)) gruende.push("heart rate " + herz + " bpm");
    if (temp !== null && (temp > 37.5 || temp < 35.5)) gruende.push("body temperature " + temp + " °C");
    if (sauerstoff !== null && sauerstoff < 95) gruende.push("oxygen saturation " + sauerstoff + " %");
    if (schlaf !== null && schlaf < 6) gruende.push("only " + schlaf + " h of sleep");

    if (gruende.length > 0) {
        hinweise.push({
            art: "warnung",
            text: "Light day: " + gruende.join(", ") + ". Only easy training today – check with the flight surgeon before anything intense.",
        });
        return { plan: ["aufwaermen", "ergometerLeicht", "dehnen", "atmung"], hinweise, leichterTag: true };
    }

    const plan = standardPlan(datum);

    if (muskelProzent !== null && muskelProzent < 90) {
        plan.splice(plan.indexOf("dehnen"), 0, "rudern", "wadenheben");
        hinweise.push({ art: "fokus", text: "Muscle strength is at " + muskelProzent + " % of the starting value – extra strength exercises added." });
    }

    if (knochenProzent !== null && knochenProzent < 95) {
        plan.splice(plan.indexOf("kniebeugen"), 1, "schwereKniebeugen");
        plan.splice(plan.indexOf("dehnen"), 0, "spruenge");
        hinweise.push({ art: "fokus", text: "Bone density is at " + knochenProzent + " % of the starting value – heavy squats and impact hops added." });
    }

    if (sport !== null && sport < SPORT_ZIEL_STUNDEN) {
        plan.splice(plan.indexOf("dehnen"), 0, "extraCardio");
        hinweise.push({ art: "fokus", text: "Last exercise time was " + sport + " h (goal " + SPORT_ZIEL_STUNDEN + " h) – extra cardio block added." });
    }

    if (strahlung !== null && strahlung > 0.9) {
        hinweise.push({ art: "info", text: "Radiation " + strahlung + " mSv is above the EVA limit – training is fine, but stay Raumstation." });
    }

    if (hinweise.length === 0) {
        hinweise.push({ art: "ok", text: "All values look good – standard plan." });
    }

    return { plan, hinweise, leichterTag: false };
}

function standardPlan(datum = new Date()) {
    // Wechselt Laufband und Intervalle je nach Wochentag ab
    const cardio = datum.getDay() % 2 === 0 ? "ergometerIntervalle" : "laufband";
    return ["aufwaermen", cardio, "kniebeugen", "kreuzheben", "bankdruecken", "dehnen"];
}