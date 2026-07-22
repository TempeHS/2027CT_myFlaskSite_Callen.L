const getStoredTheme = () => localStorage.getItem("theme");
const setStoredTheme = (theme) => localStorage.setItem("theme", theme);

const getPreferredTheme = () => {
  const storedTheme = getStoredTheme();
  if (storedTheme) {
    return storedTheme;
  }
  return window.matchMedia("(prefers-color-scheme: dark)").matches
    ? "dark"
    : "light";
};

const setTheme = (theme) => {
  document.documentElement.setAttribute("data-bs-theme", theme);
};

window.toggleTheme = () => {
  const currentTheme = document.documentElement.getAttribute("data-bs-theme");
  const newTheme = currentTheme === "dark" ? "light" : "dark";
  setStoredTheme(newTheme);
  setTheme(newTheme);
};

setTheme(getPreferredTheme());

const updateTheme = () => {
  const isDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  document.documentElement.setAttribute(
    "data-bs-theme",
    isDark ? "dark" : "light",
  );
};

updateTheme();
window
  .matchMedia("(prefers-color-scheme: dark)")
  .addEventListener("change", updateTheme);
