// Beyond Limits site behavior. Plain JavaScript, no build step.
// Each feature below is independent and only runs if its data- attribute is on
// the page. The site works without JavaScript; the "js" class on <html> turns
// on JS-only styles (base.html adds it before the page draws). Motion respects
// prefers-reduced-motion, here or in site.css.
(function () {
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

  document.querySelectorAll("[data-print]").forEach(function (btn) {
    btn.addEventListener("click", function () { window.print(); });
  });

  // Home slider. Rotates slowly, pauses on hover or focus, has a Pause button,
  // and never rotates on its own for visitors who prefer reduced motion.
  var slider = document.querySelector("[data-slider]");
  if (slider) {
    var slides = slider.querySelectorAll("[data-slide]");
    var dots = slider.querySelectorAll("[data-slider-dot]");
    var pauseBtn = slider.querySelector("[data-slider-pause]");
    var current = 0, timer = null, paused = false, hovering = false;
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var frame = slider.querySelector("[data-slider-frame]");
    var visuals = slider.querySelectorAll("[data-slider-visual]");
    var tiles = null, tilesTimer = null;
    var clearTiles = function () {
      clearTimeout(tilesTimer);
      if (tiles) { tiles.remove(); tiles = null; }
    };
    // Break the outgoing picture into a grid of tiles that shrink away in a
    // checkerboard wave, revealing the incoming picture underneath.
    var swapVisual = function (from, to) {
      clearTiles();
      if (!from || !to || from === to) return;
      if (!reduce && frame) {
        var cols = 6, rows = 6, w = frame.clientWidth, h = frame.clientHeight;
        tiles = document.createElement("div");
        tiles.className = "slider__tiles";
        for (var r = 0; r < rows; r++) {
          for (var c = 0; c < cols; c++) {
            var x = Math.floor(c * w / cols), y = Math.floor(r * h / rows);
            var tile = document.createElement("div");
            tile.className = "slider__tile";
            tile.style.cssText = "left:" + x + "px;top:" + y + "px;width:" + (Math.ceil(w / cols) + 1) + "px;height:" + (Math.ceil(h / rows) + 1) + "px;" +
              "animation-delay:" + ((r + c) * 70 + ((r + c) % 2) * 220) + "ms";
            var slice = from.cloneNode(true);
            slice.removeAttribute("data-slider-visual");
            slice.style.cssText = "position:absolute;inset:auto;left:" + (-x) + "px;top:" + (-y) + "px;width:" + w + "px;height:" + h + "px";
            tile.appendChild(slice);
            tiles.appendChild(tile);
          }
        }
        frame.appendChild(tiles);
        tilesTimer = setTimeout(clearTiles, 1900);
      }
      // Under the tiles, the incoming picture shows at once; without tiles it fades.
      if (tiles) { from.style.transition = to.style.transition = "none"; }
      from.classList.remove("is-current");
      to.classList.add("is-current");
      if (tiles) { void to.offsetWidth; from.style.transition = to.style.transition = ""; }
    };
    var show = function (i) {
      var before = current;
      current = (i + slides.length) % slides.length;
      if (visuals.length) swapVisual(visuals[before], visuals[current]);
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
      slider.classList.toggle("is-paused", p); // also stills the butterflies
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

  // Form finder: step 1 picks a path, step 2 (if any) picks one option, or several on
  // a "pick several" path, and the path's list shows only the forms for those answers.
  // A link such as /get-started/#adding (the front-desk QR code) opens that path at once.
  document.querySelectorAll("[data-finder]").forEach(function (finder) {
    var update = function (panel, moveFocus) {
      var picked = Array.prototype.filter.call(panel.querySelectorAll("[data-finder-option]"), function (b) {
        return b.getAttribute("aria-pressed") === "true";
      }).map(function (b) { return b.getAttribute("data-finder-option"); });
      var result = panel.querySelector("[data-finder-result]");
      var hasOptions = !!panel.querySelector("[data-finder-option]");
      result.querySelectorAll("[data-finder-for]").forEach(function (el) {
        el.hidden = !el.getAttribute("data-finder-for").split(" ").some(function (n) { return picked.indexOf(n) > -1; });
      });
      var list = result.querySelector("[data-finder-list]");
      var count = list ? list.querySelectorAll("li:not([hidden])").length : 0;
      if (list) list.hidden = !count;
      var ret = result.querySelector("[data-finder-return]");
      if (ret) ret.hidden = !count;
      result.classList.toggle("is-open", !hasOptions || picked.length > 0);
      if (count) result.querySelector("[data-finder-status]").textContent = count + (count === 1 ? " form" : " forms") + " on your list.";
      if (moveFocus && result.classList.contains("is-open")) result.focus();
    };
    var pathButtons = finder.querySelectorAll("[data-finder-path]");
    pathButtons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        pathButtons.forEach(function (b) { b.setAttribute("aria-pressed", String(b === btn)); });
        finder.querySelectorAll("[data-finder-panel]").forEach(function (panel) {
          var on = panel.getAttribute("data-finder-panel") === btn.getAttribute("data-finder-path");
          panel.classList.toggle("is-open", on);
          if (!on) return;
          var options = panel.querySelectorAll("[data-finder-option]");
          options.forEach(function (b) { b.setAttribute("aria-pressed", "false"); });
          update(panel, !options.length);
          if (options.length) options[0].focus();
        });
      });
    });
    finder.querySelectorAll("[data-finder-option]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var panel = btn.closest("[data-finder-panel]");
        var multi = panel.hasAttribute("data-finder-multi");
        if (multi) btn.setAttribute("aria-pressed", String(btn.getAttribute("aria-pressed") !== "true"));
        else panel.querySelectorAll("[data-finder-option]").forEach(function (b) { b.setAttribute("aria-pressed", String(b === btn)); });
        update(panel, !multi);
      });
    });
    var linked = location.hash && Array.prototype.find.call(pathButtons, function (b) {
      return b.getAttribute("data-finder-link") === location.hash.slice(1);
    });
    if (linked) {
      // After the page's own jump to #adding (which clears focus), open the path and focus its first answer.
      window.addEventListener("load", function () { setTimeout(function () { linked.click(); linked.scrollIntoView(); }, 0); });
    }
  });

  // "Who we help": filter the list of conditions as the visitor types
  document.querySelectorAll("[data-conditions]").forEach(function (box) {
    var input = box.querySelector("[data-conditions-filter]");
    var rows = box.querySelectorAll("[data-condition]");
    var empty = box.querySelector("[data-conditions-empty]");
    var count = box.querySelector("[data-conditions-count]");
    if (!input) return;
    input.addEventListener("input", function () {
      var words = input.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
      var shown = 0;
      rows.forEach(function (row) {
        var text = row.getAttribute("data-condition");
        var match = words.every(function (w) { return text.indexOf(w) !== -1; });
        row.hidden = !match;
        if (match) shown += 1;
      });
      empty.hidden = shown !== 0;
      count.textContent = words.length ? shown + (shown === 1 ? " match" : " matches") : "";
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
