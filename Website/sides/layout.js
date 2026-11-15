// Markiert die aktuelle Seite in der Navigation
(function () {
    const seite = location.pathname.split("/").pop() || "index.html";
    for (const link of document.querySelectorAll("nav a")) {
        if (link.getAttribute("href") === seite) {
            link.setAttribute("aria-current", "page");
        }
    }
})();
