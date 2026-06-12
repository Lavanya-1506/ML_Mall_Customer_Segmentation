
// =========================
// Page Loaded Animation
// =========================

document.addEventListener("DOMContentLoaded", () => {
    document.body.classList.add("loaded");
});

// =========================
// Prediction Form Validation
// =========================

const predictionForm = document.querySelector("form");

if (predictionForm) {

    predictionForm.addEventListener("submit", (e) => {

        const age = document.querySelector(
            'input[name="age"]'
        ).value;

        const income = document.querySelector(
            'input[name="income"]'
        ).value;

        const score = document.querySelector(
            'input[name="score"]'
        ).value;

        if (
            age < 1 ||
            age > 100
        ) {
            alert(
                "Age must be between 1 and 100"
            );

            e.preventDefault();
            return;
        }

        if (
            income < 1 ||
            income > 200
        ) {
            alert(
                "Income must be between 1 and 200 k$"
            );

            e.preventDefault();
            return;
        }

        if (
            score < 1 ||
            score > 100
        ) {
            alert(
                "Spending Score must be between 1 and 100"
            );

            e.preventDefault();
            return;
        }

        showLoading();
    });
}

// =========================
// Loading Button
// =========================

function showLoading() {

    const btn = document.querySelector(
        "button[type='submit']"
    );

    if (!btn) return;

    btn.innerHTML =
        `<span class="spinner-border spinner-border-sm"></span>
         Predicting...`;

    btn.disabled = true;
}

// =========================
// Active Navbar Highlight
// =========================

const currentPage =
    window.location.pathname;

const navLinks =
    document.querySelectorAll(
        ".nav-link"
    );

navLinks.forEach((link) => {

    if (
        link.getAttribute("href") === currentPage
    ) {

        link.classList.add("active");
    }
});

// =========================
// Feature Card Hover Effect
// =========================

const cards =
    document.querySelectorAll(
        ".feature-card"
    );

cards.forEach((card) => {

    card.addEventListener(
        "mouseenter",
        () => {

            card.style.transform =
                "translateY(-10px) scale(1.03)";
        }
    );

    card.addEventListener(
        "mouseleave",
        () => {

            card.style.transform =
                "translateY(0)";
        }
    );
});

// =========================
// Counter Animation
// Dashboard Cards
// =========================

const counters =
    document.querySelectorAll(
        ".dashboard-card h2"
    );

counters.forEach((counter) => {

    const target =
        parseInt(
            counter.innerText.replace("%", "")
        );

    if (isNaN(target)) return;

    let count = 0;

    const updateCounter = () => {

        const increment =
            target / 50;

        if (count < target) {

            count += increment;

            counter.innerText =
                Math.ceil(count);

            setTimeout(
                updateCounter,
                20
            );

        } else {

            counter.innerText =
                target;
        }
    };

    updateCounter();
});

// =========================
// Smooth Scroll
// =========================

document
.querySelectorAll('a[href^="#"]')
.forEach(anchor => {

    anchor.addEventListener(
        "click",
        function (e) {

            e.preventDefault();

            document
            .querySelector(
                this.getAttribute("href")
            )
            .scrollIntoView({
                behavior: "smooth"
            });
        }
    );
});

// =========================
// Scroll Reveal Animation
// =========================

const observer =
new IntersectionObserver(
(entries) => {

    entries.forEach(
        entry => {

            if (
                entry.isIntersecting
            ) {

                entry.target.classList.add(
                    "show"
                );
            }
        }
    );

});

document
.querySelectorAll(
    ".feature-card, .dashboard-card, .segment-card"
)
.forEach((el) => {

    observer.observe(el);
});