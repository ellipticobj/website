window.addEventListener('DOMContentLoaded', function() {
    // initial fade-in animation
    setTimeout(function() {
        document.body.style.opacity = '1';
        
        setTimeout(function() {
            const mainContent = document.querySelector('main');
            mainContent.style.opacity = '1';
            
            setTimeout(function() {
                const footer = document.querySelector('footer');
                footer.style.opacity = '1';
            }, 600);
        }, 600);
    }, 300);

    // section visibility animation
    const sections = document.querySelectorAll('section');
    
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15 // triggers when 15% of the section is visible
    };

    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                entry.target.classList.remove('visible');
            } else {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        sectionObserver.observe(section);
    });

    // direct links to sections
    if (window.location.hash) {
        const targetId = window.location.hash;
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            setTimeout(() => {
                targetElement.scrollIntoView({ behavior: 'smooth' });
            }, 1000);
        }
    }

    // scroll arrow functionality (down arrow & back to top button)
    const scrollArrow = document.querySelector('.scroll-arrow');
    const heroContainer = document.querySelector('.hero-container');
    
    function handleScroll() {
        if (!heroContainer) return;
        
        const heroBottom = heroContainer.offsetTop + heroContainer.offsetHeight;
        
        if (window.scrollY > heroBottom) {
            scrollArrow.classList.add('show-top');
            scrollArrow.querySelector('a').setAttribute('href', '#');
        } else {
            scrollArrow.classList.remove('show-top');
            scrollArrow.querySelector('a').setAttribute('href', '#projects');
        }
    }

    window.addEventListener('scroll', handleScroll);
    
    // handle scroll arrow clicks (now with firefox support! wow!)
    function smoothScroll(target) {
        const targetPosition = target.getBoundingClientRect().top + window.pageYOffset;
        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
    }

    function handleArrowClick(e) {
        e.preventDefault();
        
        if (scrollArrow.classList.contains('show-top')) {
            smoothScroll(heroContainer);
        } else {
            const firstSection = document.querySelector('section');
            if (firstSection) {
                smoothScroll(firstSection);
            }
        }
    }

    // apply click handler 
    scrollArrow.addEventListener('click', handleArrowClick);
    scrollArrow.querySelector('a').addEventListener('click', handleArrowClick);

    handleScroll();
});

// smooth scroll for all anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            targetElement.scrollIntoView({ 
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// contact form validation
const contactForm = document.getElementById('contactForm');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const messageInput = document.getElementById('message');
const nameError = document.getElementById('name-error');
const emailError = document.getElementById('email-error');
const messageError = document.getElementById('message-error');

contactForm.addEventListener('submit', (event) => {
    let hasErrors = false;

    if (!nameInput.value.trim()) {
        nameError.style.display = 'block';
        hasErrors = true;
    } else {
        nameError.style.display = 'none';
    }

    if (!emailInput.value.trim() || !isValidEmail(emailInput.value.trim())) {
        emailError.style.display = 'block';
        hasErrors = true;
    } else {
        emailError.style.display = 'none';
    }

    if (!messageInput.value.trim()) {
        messageError.style.display = 'block';
        hasErrors = true;
    } else {
        messageError.style.display = 'none';
    }

    if (hasErrors) {
        event.preventDefault();
    }
});

// email validation helper function
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}
