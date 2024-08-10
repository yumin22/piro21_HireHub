
document.addEventListener('DOMContentLoaded', function() {
    // 공통 질문 클릭 이벤트
    const commonQuestionTitle = document.getElementById('commonQuestionTitle');
    if (commonQuestionTitle) {
        commonQuestionTitle.addEventListener('click', function() {
            console.log('공통 질문 클릭됨'); // 콘솔 로그 출력
            const commonQuestionContent = document.getElementById('commonQuestionContent');
            const applicationContent = document.getElementById('applicationContent');
            if (commonQuestionContent && applicationContent) {
                commonQuestionContent.style.display = 'block'; // 공통 질문 내용 보이기
                applicationContent.style.display = 'none'; // 지원서 내용 숨기기
            }
        });
    }

    // 지원서 클릭 이벤트
    const applicationTitle = document.getElementById('applicationTitle');
    if (applicationTitle) {
        applicationTitle.addEventListener('click', function() {
            console.log('지원서 클릭됨'); // 콘솔 로그 출력
            const commonQuestionContent = document.getElementById('commonQuestionContent');
            const applicationContent = document.getElementById('applicationContent');
            if (commonQuestionContent && applicationContent) {
                applicationContent.style.display = 'block'; // 지원서 내용 보이기
                commonQuestionContent.style.display = 'none'; // 공통 질문 내용 숨기기
            }
        });
    }
});


$('#questionForm').submit(function(e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: $('#questionForm').attr('action'),
        data: $('#questionForm').serialize(),
        success: function(response) {
            if (response.success) {
                $('#questionList').append('<li>' + response.question.text + ' (' + response.question.created_at + ')</li>');
                $('#questionForm')[0].reset();
            } else {
                alert('Failed to add question');
            }
        }
    });
});

$('.answerForm').submit(function(e) {
    e.preventDefault();
    var form = $(this);
    $.ajax({
        type: 'POST',
        url: form.attr('action'),
        data: form.serialize(),
        success: function(response) {
            if (response.success) {
                form.closest('li').find('ul').append('<li>' + response.answer.text + ' (' + response.answer.created_at + ')</li>');
                form[0].reset();
            } else {
                alert('Failed to add answer');
            }
        }
    });
});