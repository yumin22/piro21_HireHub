sdocument.addEventListener('DOMContentLoaded', function() {
    const animatedElement = document.getElementById('animateElement');

    // 포커스 상태가 되었을 때 애니메이션 클래스를 추가
    window.addEventListener('focus', function() {
        animatedElement.classList.add('animate-on-focus');
    });

    // 포커스가 해제되었을 때 애니메이션 클래스를 제거
    window.addEventListener('blur', function() {
        animatedElement.classList.remove('animate-on-focus');
    });
});