document.addEventListener("DOMContentLoaded", function () {
    var cards = document.querySelectorAll(".integrante-card");

    if (!cards.length) {
        return;
    }

    if (!("IntersectionObserver" in window)) {
        cards.forEach(function (card) {
            card.classList.add("em-vista");
        });
        return;
    }

    var observer = new IntersectionObserver(
        function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add("em-vista");
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.2 }
    );

    cards.forEach(function (card) {
        observer.observe(card);
    });
});
