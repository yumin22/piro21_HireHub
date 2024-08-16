document.addEventListener('DOMContentLoaded', function () {
    const titleBoxes = document.querySelectorAll('#title_box');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // 애니메이션이 한 번만 적용되도록 관찰 중지
            }
        });
    });

    titleBoxes.forEach(box => {
        observer.observe(box);
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const finalButtons = document.querySelectorAll('#final_btn');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target); // 애니메이션이 한 번만 적용되도록 관찰 중지
                }, 600); // 딜레이
            }
        });
    });

    finalButtons.forEach(button => {
        observer.observe(button);
    });
});
