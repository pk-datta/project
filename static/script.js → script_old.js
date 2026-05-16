// Mobile Menu Toggle
const menuBtn = document.getElementById("menu-btn");
const menu = document.getElementById("menu");

menuBtn.addEventListener("click", () => {
    menu.classList.toggle("show");
});

// Close Menu After Click
const navLinks = document.querySelectorAll("#menu a");

navLinks.forEach(link => {
    link.addEventListener("click", () => {
        menu.classList.remove("show");
    });
});

// Navbar Background Change on Scroll
window.addEventListener("scroll", () => {
    const navbar = document.querySelector("nav");

    if (window.scrollY > 50) {
        navbar.style.background = "rgba(15, 23, 42, 0.9)";
        navbar.style.backdropFilter = "blur(15px)";
        navbar.style.boxShadow = "0 8px 20px rgba(0,0,0,0.3)";
    } else {
        navbar.style.background = "rgba(255,255,255,0.1)";
        navbar.style.boxShadow = "none";
    }
});

// Admission Form Submit
const form = document.getElementById("admissionForm");

form.addEventListener("submit", function(e) {
    e.preventDefault();

    alert("Thank You! Your admission form has been submitted successfully.");

    form.reset();
});

// Smooth Fade-In Animation on Scroll
const cards = document.querySelectorAll(".course-card, .feature-box, .hero-form");

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = "1";
            entry.target.style.transform = "translateY(0)";
        }
    });
}, {
    threshold: 0.2
});

cards.forEach(card => {
    card.style.opacity = "0";
    card.style.transform = "translateY(50px)";
    card.style.transition = "all 0.8s ease";
    observer.observe(card);
});

// Typing Effect for Hero Heading
const heading = document.querySelector(".hero-text h1");
const originalText = heading.innerHTML;

heading.innerHTML = "";

let i = 0;

function typeEffect() {
    if (i < originalText.length) {
        heading.innerHTML += originalText.charAt(i);
        i++;
        setTimeout(typeEffect, 40);
    }
}

window.addEventListener("load", typeEffect);