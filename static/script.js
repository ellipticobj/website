document.addEventListener('DOMContentLoaded', () => {
    function setupScrollHints(container) {
        const scrollContainer = container.querySelector('.nav-links, .cardlist');
        const leftArrow = container.querySelector('.scroll-arrow.left');
        const rightArrow = container.querySelector('.scroll-arrow.right');
      
        function updateArrows() {
            const scrollLeft = scrollContainer.scrollLeft;
            const maxScroll = scrollContainer.scrollWidth - scrollContainer.clientWidth;
        
            leftArrow.classList.toggle('visible', scrollLeft > 0);
            rightArrow.classList.toggle('visible', scrollLeft < maxScroll);
        }
      
        updateArrows();
        scrollContainer.addEventListener('scroll', updateArrows);
        window.addEventListener('resize', updateArrows);
      
        leftArrow.addEventListener('click', () => {
            scrollContainer.scrollBy({
                left: -200,
                behavior: 'smooth'
            });
        });
      
        rightArrow.addEventListener('click', () => {
            scrollContainer.scrollBy({
                left: 200,
                behavior: 'smooth'
            });
        });
    }
    
    document.querySelectorAll('.scroll-container').forEach(setupScrollHints);
    
    const fab = document.getElementById('fab');
    const footer = document.querySelector('footer');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                fab.classList.remove('visible');
            } else if (window.scrollY > 100) {
                fab.classList.add('visible');
            }
        });
    }, {
        rootMargin: '0px',
        threshold: 0.1
    });

    observer.observe(footer);
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 1) {
            fab.classList.add('visible');
        } else {
            fab.classList.remove('visible');
        }
    });

    fab.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    fab.classList.remove('visible');

    function setActiveNavLink() {
        const sections = document.querySelectorAll('section');
        const navLinks = document.querySelectorAll('.nav-links a');

        sections.forEach(section => {
            const rect = section.getBoundingClientRect();
            if (rect.top < 100 && rect.bottom >= 100) {
                navLinks.forEach(link => {
                    link.removeAttribute('aria-current');
                    if (link.getAttribute('href') == `#${section.id}`) {
                        link.setAttribute('aria-current', 'page');
                    }
                });
            }
        })
    }

    window.addEventListener('resize', setActiveNavLink);
    window.addEventListener('scroll', setActiveNavLink);
});