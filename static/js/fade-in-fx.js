function setupFadeObserver(selector, threshold) {
  const elements = document.querySelectorAll(selector);

  if (elements.length === 0) {
    return;
  }

  const observer = new IntersectionObserver(
    (entries, currentObserver) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) {
          return;
        }

        entry.target.classList.add("active");
        currentObserver.unobserve(entry.target);
      });
    },
    {
      root: null,
      threshold,
    },
  );

  elements.forEach((element) => {
    observer.observe(element);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  setupFadeObserver(".fade-in-fx", 1);
  setupFadeObserver(".fade-in-fx-higher", 0.6);
  setupFadeObserver(".fade-in-fx-even-higher", 0.3);
});
