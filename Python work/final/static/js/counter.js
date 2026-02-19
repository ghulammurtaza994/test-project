document.addEventListener('DOMContentLoaded', function() {
    function countUp(element, target, duration = 2000) {
        let current = 0;
        const increment = target / (duration / 16); // 60 FPS
        
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                element.textContent = target;
                clearInterval(timer);
            } else {
                element.textContent = Math.floor(current);
            }
        }, 16);
    }

    // Start animation when page loads (for elements already visible)
    const counters = document.querySelectorAll('.counter');
    counters.forEach(counter => {
        const target = parseInt(counter.dataset.target);
        countUp(counter, target);
    });
});

