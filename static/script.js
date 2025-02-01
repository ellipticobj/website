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