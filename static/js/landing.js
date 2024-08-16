document.addEventListener('DOMContentLoaded', function () {
    const titleBoxes = document.querySelectorAll('#title_box, #final_btn');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                if (entry.target.id === 'final_btn') {
                    setTimeout(() => {
                        entry.target.classList.add('visible');
                    }, 600); 
                } else {
                    entry.target.classList.add('visible');
                }
                observer.unobserve(entry.target); // 애니메이션이 한 번만 적용되도록 관찰 중지
            }
        });
    });

    titleBoxes.forEach(box => {
        observer.observe(box);
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const images = document.querySelectorAll('.left, .right, #info');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                if (entry.target.id === 'info') {
                    setTimeout(() => {
                        entry.target.classList.add('visible');
                    }, 500); 
                } else {
                    entry.target.classList.add('visible');
                }

                observer.unobserve(entry.target); // 애니메이션이 한 번만 적용되도록 관찰 중지
            }
        });
    });

    images.forEach(image => {
        observer.observe(image);
    });
});
