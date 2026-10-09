(function () {
  document.documentElement.classList.add("js");

  // Mobile navigation
  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      document.body.classList.toggle("nav-open", !open);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && document.body.classList.contains("nav-open")) {
        toggle.setAttribute("aria-expanded", "false");
        document.body.classList.remove("nav-open");
        toggle.focus();
      }
    });
  }

  // Shadow on the sticky header once the page scrolls
  var header = document.querySelector("[data-header]");
  if (header) {
    var onScroll = function () { header.classList.toggle("is-scrolled", window.scrollY > 8); };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  // Team filter
  var filter = document.querySelector("[data-filter]");
  if (filter) {
    var buttons = filter.querySelectorAll("[data-filter-value]");
    var groups = document.querySelectorAll("[data-filter-group]");
    filter.addEventListener("click", function (e) {
      var btn = e.target.closest("[data-filter-value]");
      if (!btn) return;
      var value = btn.getAttribute("data-filter-value");
      buttons.forEach(function (b) {
        var on = b === btn;
        b.classList.toggle("is-active", on);
        b.setAttribute("aria-pressed", String(on));
      });
      groups.forEach(function (g) {
        g.hidden = value !== "all" && g.getAttribute("data-filter-group") !== value;
      });
    });
  }

  // Home slider. Rotates slowly, pauses on hover or focus, has a Pause button,
  // and never rotates on its own for visitors who prefer reduced motion.
  var slider = document.querySelector("[data-slider]");
  if (slider) {
    var slides = slider.querySelectorAll("[data-slide]");
    var dots = slider.querySelectorAll("[data-slider-dot]");
    var pauseBtn = slider.querySelector("[data-slider-pause]");
    var current = 0, timer = null, paused = false, hovering = false;
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var show = function (i) {
      current = (i + slides.length) % slides.length;
      slides.forEach(function (s, n) {
        var on = n === current;
        s.classList.toggle("is-current", on);
        s.setAttribute("aria-hidden", String(!on));
        s.querySelectorAll("a, button").forEach(function (el) { el.tabIndex = on ? 0 : -1; });
      });
      dots.forEach(function (d, n) {
        if (n === current) d.setAttribute("aria-current", "true"); else d.removeAttribute("aria-current");
      });
    };
    var stop = function () { clearInterval(timer); timer = null; };
    var start = function () {
      stop();
      if (!paused && !hovering && slides.length > 1) timer = setInterval(function () { show(current + 1); }, 7000);
    };
    var setPaused = function (p) {
      paused = p;
      if (pauseBtn) { pauseBtn.textContent = p ? "Play" : "Pause"; pauseBtn.setAttribute("aria-pressed", String(p)); }
      p ? stop() : start();
    };
    var prev = slider.querySelector("[data-slider-prev]");
    var next = slider.querySelector("[data-slider-next]");
    if (prev) prev.addEventListener("click", function () { show(current - 1); start(); });
    if (next) next.addEventListener("click", function () { show(current + 1); start(); });
    dots.forEach(function (d) { d.addEventListener("click", function () { show(+d.getAttribute("data-slider-dot")); start(); }); });
    if (pauseBtn) pauseBtn.addEventListener("click", function () { setPaused(!paused); });
    slider.addEventListener("mouseenter", function () { hovering = true; stop(); });
    slider.addEventListener("mouseleave", function () { hovering = false; start(); });
    slider.addEventListener("focusin", function () { hovering = true; stop(); });
    slider.addEventListener("focusout", function () { hovering = false; start(); });
    if (reduce) setPaused(true); else start();
  }

  // Form finder: step 1 picks a path, step 2 (if any) picks an option, then the forms show.
  document.querySelectorAll("[data-finder]").forEach(function (finder) {
    var press = function (buttons, active) {
      buttons.forEach(function (b) { b.setAttribute("aria-pressed", String(b === active)); });
    };
    var showResult = function (result) {
      finder.querySelectorAll("[data-finder-result]").forEach(function (r) { r.classList.toggle("is-open", r === result); });
      if (result) result.focus({ preventScroll: false });
    };
    var pathButtons = finder.querySelectorAll("[data-finder-path]");
    pathButtons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var id = btn.getAttribute("data-finder-path");
        press(pathButtons, btn);
        var panel = null;
        finder.querySelectorAll("[data-finder-panel]").forEach(function (p) {
          var on = p.getAttribute("data-finder-panel") === id;
          p.classList.toggle("is-open", on);
          if (on) panel = p;
        });
        if (!panel) return;
        var options = panel.querySelectorAll("[data-finder-option]");
        press(options, null);
        if (options.length) { showResult(null); options[0].focus(); }
        else showResult(panel.querySelector("[data-finder-result]"));
      });
    });
    finder.querySelectorAll("[data-finder-option]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var panel = btn.closest("[data-finder-panel]");
        press(panel.querySelectorAll("[data-finder-option]"), btn);
        showResult(finder.querySelector('[data-finder-result="' + btn.getAttribute("data-finder-option") + '"]'));
      });
    });
  });

  // Back to top button
  var toTop = document.querySelector("[data-to-top]");
  if (toTop) {
    window.addEventListener("scroll", function () { toTop.classList.toggle("is-shown", window.scrollY > 600); }, { passive: true });
  }

  // Gentle reveal on scroll (skipped when the visitor prefers reduced motion)
  if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var items = document.querySelectorAll(".block, .service-card, .team-card");
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("is-visible"); io.unobserve(entry.target); }
      });
    }, { rootMargin: "0px 0px -60px 0px" });
    items.forEach(function (el) { el.classList.add("reveal"); io.observe(el); });
  }
})();
