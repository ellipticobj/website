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
    fab.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 1) {
            fab.classList.add('visible');
        } else {
            fab.classList.remove('visible');
        }
    });
    
    fab.classList.remove('visible');
});