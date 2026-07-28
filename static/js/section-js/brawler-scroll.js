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
  let resizeTimer = null;

  const dragThreshold = 10;

  const getCards = () => {
    return [...scrollWheel.querySelectorAll(".card-scroll")];
  };

  const getCardScrollPosition = (card) => {
    const cardCentre = card.offsetLeft + card.offsetWidth / 2;

    return cardCentre - scrollWheel.clientWidth / 2;
  };

  const getClosestCard = () => {
    const cards = getCards();

    if (!cards.length) {
      return null;
    }

    const wheelCentre = scrollWheel.scrollLeft + scrollWheel.clientWidth / 2;

    return cards.reduce((closestCard, card) => {
      const cardCentre = card.offsetLeft + card.offsetWidth / 2;
      const closestCentre =
        closestCard.offsetLeft + closestCard.offsetWidth / 2;

      const cardDistance = Math.abs(cardCentre - wheelCentre);
      const closestDistance = Math.abs(closestCentre - wheelCentre);

      return cardDistance < closestDistance ? card : closestCard;
    });
  };

  const scrollToCard = (card, behavior = "smooth") => {
    if (!card) {
      return;
    }

    scrollWheel.scrollTo({
      left: getCardScrollPosition(card),
      behavior,
    });
  };

  const snapToClosestCard = (behavior = "smooth") => {
    scrollToCard(getClosestCard(), behavior);
  };

  const updateButtons = () => {
    const maximumScroll = scrollWheel.scrollWidth - scrollWheel.clientWidth;

    const threshold = 2;

    leftButton.disabled =
      maximumScroll <= threshold || scrollWheel.scrollLeft <= threshold;

    rightButton.disabled =
      maximumScroll <= threshold ||
      scrollWheel.scrollLeft >= maximumScroll - threshold;
  };

  const scrollByOneCard = (direction) => {
    const cards = getCards();
    const closestCard = getClosestCard();

    if (!cards.length || !closestCard) {
      return;
    }

    const currentIndex = cards.indexOf(closestCard);

    const nextIndex = Math.max(
      0,
      Math.min(cards.length - 1, currentIndex + direction),
    );

    scrollToCard(cards[nextIndex]);
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
  });

  scrollWheel.addEventListener("pointermove", (event) => {
    if (!isDragging || event.pointerId !== activePointerId) {
      return;
    }

    const distanceMoved = event.clientX - dragStartX;

    if (!hasDragged && Math.abs(distanceMoved) > dragThreshold) {
      hasDragged = true;

      scrollWheel.classList.add("is-dragging");
      scrollWheel.setPointerCapture(event.pointerId);
    }

    if (!hasDragged) {
      return;
    }

    scrollWheel.scrollLeft = dragStartScrollLeft - distanceMoved;
  });

  const finishDragging = (event) => {
    if (!isDragging || event.pointerId !== activePointerId) {
      return;
    }

    const pointerId = activePointerId;

    isDragging = false;
    activePointerId = null;

    scrollWheel.classList.remove("is-dragging");

    if (scrollWheel.hasPointerCapture(pointerId)) {
      scrollWheel.releasePointerCapture(pointerId);
    }

    if (hasDragged) {
      snapToClosestCard();
    }

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
    window.clearTimeout(resizeTimer);

    resizeTimer = window.setTimeout(() => {
      updateButtons();
      snapToClosestCard("auto");
    }, 100);
  });

  updateButtons();
});
