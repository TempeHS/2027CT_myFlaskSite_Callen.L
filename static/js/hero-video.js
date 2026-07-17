(() => {
  const video = document.getElementById("hero-video");
  const audioToggle = document.getElementById("audio-toggle");
  const icon = audioToggle?.querySelector("i");
  const loadingText = document.getElementById("video-loading-text");
  const bg = document.querySelector(".hero-video");

  const loadingFrames = [
    "Waiting for video to load",
    "Waiting for video to load.",
    "Waiting for video to load..",
    "Waiting for video to load...",
  ];
  let loadingTimer = null;
  let loadingIndex = 0;

  function startLoadingText() {
    if (!loadingText) return;
    loadingText.style.display = "";
    loadingText.textContent = loadingFrames[0];
    loadingTimer = setInterval(() => {
      loadingIndex = (loadingIndex + 1) % loadingFrames.length;
      loadingText.textContent = loadingFrames[loadingIndex];
    }, 450);
  }

  function stopLoadingText() {
    if (loadingTimer) clearInterval(loadingTimer);
    loadingTimer = null;
    if (loadingText) loadingText.style.display = "none";
  }

  if (video) {
    video.addEventListener("loadeddata", stopLoadingText, { once: true });
    video.addEventListener("error", () => {
      if (loadingTimer) clearInterval(loadingTimer);
      if (loadingText) loadingText.textContent = "Video failed to load.";
    });
  }

  if (video && audioToggle && icon) {
    audioToggle.setAttribute("aria-pressed", String(!video.muted));
    audioToggle.setAttribute(
      "aria-label",
      video.muted ? "Unmute video audio" : "Mute video audio",
    );
    icon.className = video.muted
      ? "bi bi-volume-mute-fill fs-5"
      : "bi bi-volume-up-fill fs-5";

    const handleAudioToggle = () => {
      video.muted = !video.muted;
      const isMuted = video.muted;

      icon.className = isMuted
        ? "bi bi-volume-mute-fill fs-5"
        : "bi bi-volume-up-fill fs-5";

      audioToggle.setAttribute("aria-pressed", String(!isMuted));
      audioToggle.setAttribute(
        "aria-label",
        isMuted ? "Unmute video audio" : "Mute video audio",
      );
    };

    audioToggle.removeEventListener("click", handleAudioToggle);
    audioToggle.addEventListener("click", handleAudioToggle);
  }

  const DB_NAME = "HeroVideoCacheDB";
  const STORE_NAME = "videos";
  const VIDEO_KEY = "hero-video-file";
  const VIDEO_URL = "{{ url_for('static', filename='videos/hero.mp4') }}";

  let objectUrl = null;

  function setVideoSrcFromBlob(blob) {
    if (!video) return;
    if (objectUrl) URL.revokeObjectURL(objectUrl);
    objectUrl = URL.createObjectURL(blob);
    video.src = objectUrl;
    video.play?.().catch(() => {});
  }

  function startVideoLoad() {
    if (!video || !("indexedDB" in window)) {
      if (video) video.src = VIDEO_URL;
      return;
    }

    const request = indexedDB.open(DB_NAME, 1);

    request.onupgradeneeded = (e) => {
      const db = e.target.result;
      if (!db.objectStoreNames.contains(STORE_NAME)) {
        db.createObjectStore(STORE_NAME);
      }
    };

    request.onerror = () => {
      video.src = VIDEO_URL;
    };

    request.onsuccess = (e) => {
      const db = e.target.result;
      const tx = db.transaction([STORE_NAME], "readonly");
      const store = tx.objectStore(STORE_NAME);
      const getRequest = store.get(VIDEO_KEY);

      getRequest.onsuccess = async () => {
        if (getRequest.result) {
          setVideoSrcFromBlob(getRequest.result);
          return;
        }

        video.src = VIDEO_URL;
        try {
          const response = await fetch(VIDEO_URL, { cache: "force-cache" });
          if (!response.ok) return;
          const blob = await response.blob();
          const wtx = db.transaction([STORE_NAME], "readwrite");
          wtx.objectStore(STORE_NAME).put(blob, VIDEO_KEY);
        } catch {}
      };

      getRequest.onerror = () => {
        video.src = VIDEO_URL;
      };
    };
  }

  function scheduleVideoLoad() {
    const connection =
      navigator.connection ||
      navigator.mozConnection ||
      navigator.webkitConnection;
    const isSlow = Boolean(
      connection?.saveData || /(^|-)2g$/.test(connection?.effectiveType || ""),
    );

    const start = () => {
      if ("requestIdleCallback" in window) {
        requestIdleCallback(() => startVideoLoad(), {
          timeout: isSlow ? 5000 : 2500,
        });
      } else {
        setTimeout(startVideoLoad, isSlow ? 2500 : 800);
      }
    };

    const hero = document.querySelector(".hero");
    if ("IntersectionObserver" in window && hero) {
      const io = new IntersectionObserver(
        (entries, observer) => {
          if (entries.some((e) => e.isIntersecting)) {
            observer.disconnect();
            start();
          }
        },
        { rootMargin: "200px 0px" },
      );
      io.observe(hero);
    } else {
      start();
    }
  }

  window.addEventListener(
    "load",
    () => {
      startLoadingText();
      scheduleVideoLoad();
    },
    { once: true },
  );

  window.addEventListener("beforeunload", () => {
    if (objectUrl) URL.revokeObjectURL(objectUrl);
  });
})();

const bg = document.querySelector(".hero-video");
let ticking = false;

window.addEventListener(
  "scroll",
  () => {
    if (!bg || ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      const offset = window.pageYOffset || 0;
      bg.style.transform = `translateY(${offset * 0.35}px)`;
      ticking = false;
    });
  },
  { passive: true },
);
