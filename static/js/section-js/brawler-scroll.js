document.addEventListener("DOMContentLoaded", () => {
  const wrapper = document.querySelector(".scroll-wheel-wrapper");

  if (!wrapper) {
    return;
  }

  const scrollWheel = wrapper.querySelector(".scroll-wheel");
  const leftButton = wrapper.querySelector(".scroll-arrow-left");
  const rightButton = wrapper.querySelector(".scroll-arrow-right");

  if (!scrollWheel || !leftButton || !rightButton) {
    return;
  }

  let isDragging = false;
  let hasDragged = false;
  let dragStartX = 0;
  let dragStartScrollLeft = 0;
  let activePointerId = null;

  const getCards = () => {
    return [...scrollWheel.querySelectorAll(".card-scroll")];
  };

  const getClosestCard = () => {
    const cards = getCards();
    const wheelCentre = scrollWheel.scrollLeft + scrollWheel.clientWidth / 2;

    return cards.reduce((closestCard, card) => {
      const cardCentre = card.offsetLeft + card.offsetWidth / 2;
      const closestCentre =
        closestCard.offsetLeft + closestCard.offsetWidth / 2;

      return Math.abs(cardCentre - wheelCentre) <
        Math.abs(closestCentre - wheelCentre)
        ? card
        : closestCard;
    }, cards[0]);
  };

  const snapToClosestCard = () => {
    const closestCard = getClosestCard();

    if (!closestCard) {
      return;
    }

    closestCard.scrollIntoView({
      behavior: "smooth",
      block: "nearest",
      inline: "center",
    });
  };

  const updateButtons = () => {
    const maximumScroll = scrollWheel.scrollWidth - scrollWheel.clientWidth;

    const threshold = 2;

    leftButton.disabled = scrollWheel.scrollLeft <= threshold;

    rightButton.disabled =
      maximumScroll <= threshold ||
      scrollWheel.scrollLeft >= maximumScroll - threshold;
  };

  const scrollByOneCard = (direction) => {
    const cards = getCards();

    if (!cards.length) {
      return;
    }

    const closestCard = getClosestCard();
    const currentIndex = cards.indexOf(closestCard);

    const nextIndex = Math.max(
      0,
      Math.min(cards.length - 1, currentIndex + direction),
    );

    cards[nextIndex].scrollIntoView({
      behavior: "smooth",
      block: "nearest",
      inline: "center",
    });
  };

  leftButton.addEventListener("click", () => {
    scrollByOneCard(-1);
  });

  rightButton.addEventListener("click", () => {
    scrollByOneCard(1);
  });

  scrollWheel.addEventListener("pointerdown", (event) => {
    if (event.pointerType === "mouse" && event.button !== 0) {
      return;
    }

    isDragging = true;
    hasDragged = false;
    activePointerId = event.pointerId;

    dragStartX = event.clientX;
    dragStartScrollLeft = scrollWheel.scrollLeft;

    scrollWheel.classList.add("is-dragging");
    scrollWheel.setPointerCapture(event.pointerId);
  });

  scrollWheel.addEventListener("pointermove", (event) => {
    if (!isDragging || event.pointerId !== activePointerId) {
      return;
    }

    const distanceMoved = event.clientX - dragStartX;

    if (Math.abs(distanceMoved) > 5) {
      hasDragged = true;
    }

    scrollWheel.scrollLeft = dragStartScrollLeft - distanceMoved;
    updateButtons();
  });

  const finishDragging = (event) => {
    if (!isDragging || event.pointerId !== activePointerId) {
      return;
    }

    isDragging = false;
    activePointerId = null;

    scrollWheel.classList.remove("is-dragging");

    if (scrollWheel.hasPointerCapture(event.pointerId)) {
      scrollWheel.releasePointerCapture(event.pointerId);
    }

    snapToClosestCard();
    updateButtons();
  };

  scrollWheel.addEventListener("pointerup", finishDragging);
  scrollWheel.addEventListener("pointercancel", finishDragging);
  scrollWheel.addEventListener(
    "click",
    (event) => {
      if (!hasDragged) {
        return;
      }

      event.preventDefault();
      event.stopPropagation();
      hasDragged = false;
    },
    true,
  );

  scrollWheel.addEventListener("scroll", updateButtons, {
    passive: true,
  });

  window.addEventListener("resize", () => {
    updateButtons();
    snapToClosestCard();
  });

  updateButtons();
});
