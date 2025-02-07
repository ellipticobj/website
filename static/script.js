document.addEventListener("DOMContentLoaded", () => {
  // scoll hints
  function setupScrollHints(container) {
    const scrollContainer = container.querySelector(".nav-links, .cardlist");
    const leftArrow = container.querySelector(".scroll-arrow.left");
    const rightArrow = container.querySelector(".scroll-arrow.right");

    function updateArrows() {
      const scrollLeft = scrollContainer.scrollLeft;
      const maxScroll =
        scrollContainer.scrollWidth - scrollContainer.clientWidth;

      leftArrow.classList.toggle("visible", scrollLeft > 0);
      rightArrow.classList.toggle("visible", scrollLeft < maxScroll);
    }

    updateArrows();
    scrollContainer.addEventListener("scroll", updateArrows);
    window.addEventListener("resize", updateArrows);

    leftArrow.addEventListener("click", () => {
      scrollContainer.scrollBy({
        left: -300,
        behavior: "smooth",
      });
    });

    rightArrow.addEventListener("click", () => {
      scrollContainer.scrollBy({
        left: 300,
        behavior: "smooth",
      });
    });
  }

  document.querySelectorAll(".scroll-container").forEach(setupScrollHints);

  // fab
  const fab = document.getElementById("fab");
  const footer = document.querySelector("footer");

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          fab.classList.remove("visible");
        } else if (window.scrollY > 100) {
          fab.classList.add("visible");
        }
      });
    },
    {
      rootMargin: "-50% 0px 0px 0px",
      threshold: 1,
    },
  );

  observer.observe(footer);

  fab.addEventListener("click", () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });

  fab.classList.remove("visible");

  // navbar
  function setActiveNavLink() {
    const sections = document.querySelectorAll("section");
    const navLinks = document.querySelectorAll(".nav-links a");

    sections.forEach((section) => {
      const rect = section.getBoundingClientRect();
      if (rect.top < 100 && rect.bottom >= 100) {
        navLinks.forEach((link) => {
          link.removeAttribute("aria-current");
          if (link.getAttribute("href") == `#${section.id}`) {
            link.setAttribute("aria-current", "page");
          }
        });
      }
    });
  }

  window.addEventListener("scroll", () => {
    if (window.scrollY > 1) {
      fab.classList.add("visible");
    } else {
      fab.classList.remove("visible");
    }
  });

  window.addEventListener("resize", setActiveNavLink);
  window.addEventListener("scroll", setActiveNavLink);
});
