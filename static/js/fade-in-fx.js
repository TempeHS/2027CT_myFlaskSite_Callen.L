document.addEventListener("DOMContentLoaded", function () {
  const observerOptions = {
    root: null,
    threshold: 1.0,
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("active");
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll(".fade-in-fx").forEach((section) => {
    observer.observe(section);
  });
});
