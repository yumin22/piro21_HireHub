function adjustFontSize() {
    const teamScores = document.querySelectorAll('.team_score');
    
    teamScores.forEach(score => {
        // 각 team_score 요소의 너비를 가져옴
        const scoreWidth = score.clientWidth;

        // 폰트 크기 계산: 원하는 비율에 따라 계산하고, 최대 크기를 20px로 제한
        const fontSize = Math.min(scoreWidth / 20, 20);  // 최대 20px로 제한

        // 테이블의 th와 td에 적용
        const ths = score.querySelectorAll('th');
        const tds = score.querySelectorAll('td');
        
        ths.forEach(th => {
            th.style.fontSize = fontSize + 'px';
        });
        
        tds.forEach(td => {
            td.style.fontSize = (fontSize * 0.8) + 'px'; // td는 th보다 작게, 최대 16px로 제한됨
        });
    });
}

// 페이지 로드 시 폰트 크기 조정
window.addEventListener('load', adjustFontSize);

// 창 크기가 조정될 때마다 폰트 크기 조정
window.addEventListener('resize', adjustFontSize);
