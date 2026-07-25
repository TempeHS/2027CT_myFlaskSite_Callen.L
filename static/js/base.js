// Back to Top Button
const backToTopButton = document.getElementById("back-to-top");
window.addEventListener("scroll", () => {
  if (window.scrollY > 200) {
    backToTopButton.classList.add("show");
  } else {
    backToTopButton.classList.remove("show");
  }
});
backToTopButton.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
});

// Navbar Blur effect
const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", () => {
  if (window.scrollY > 28) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }
});

// Warning Script for XSS
setTimeout(() => {
  if (
    window.location.hostname !== "127.0.0.1" &&
    window.location.hostname !== "localhost"
  ) {
    console.clear();
  }

  console.log(
    "%cSTOP!",
    "color: red; font-size: 55px; font-weight: bold; -webkit-text-stroke: 2px black;",
  );

  console.log(
    "%cUsing this console may allow attackers to impersonate you and steal your information using an attack called Self-XSS.",
    "color: gray; font-size: 20px; font-weight: bold;",
  );

  console.log(
    "%cDo not enter or paste code that you do not understand.",
    "color: tomato; font-size: 18px; font-weight: bold; line-height: 2;",
  );
}, 2000);
