function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

$(document).ready(function() {
    $('#questionForm').submit(function(e) {
        e.preventDefault();

        // 기존 폼 데이터를 가져옴
        var formData = $('#questionForm').serializeArray();

        // 폼 데이터에 question_submit 항목 추가
        formData.push({ name: 'question_submit', value: 'Add Question' });

        $.ajax({
            type: 'POST',
            url: $('#questionForm').attr('action'),
            data: $.param(formData),
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(response) {
                if (response.success) {
                    $('#questionList').append('<li>' + response.question.text + ' (' + response.question.created_at + ')</li>');
                    $('#questionForm')[0].reset();
                } else {
                    alert('Failed to add question: ' + response.error);
                    console.error(response.form_errors);  // 폼 오류 메시지 출력
                }
            },
            error: function(xhr, status, error) {
                alert('An error occurred: ' + error);
                console.error('AJAX request failed:', error);
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
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(response) {
                if (response.success) {
                    form.closest('li').find('ul').append('<li>' + response.answer.text + ' (' + response.answer.created_at + ')</li>');
                    form[0].reset();
                } else {
                    alert('Failed to add answer: ' + response.error);
                    console.error(response.form_errors);  // 폼 오류 메시지 출력
                }
            },
            error: function(xhr, status, error) {
                alert('An error occurred: ' + error);
                console.error('AJAX request failed:', error);
            }
        });
    });
    

    // $('.answerForm').submit(function(e) {
    //     e.preventDefault();
    //     var form = $(this);
    //     $.ajax({
    //         type: 'POST',
    //         url: form.attr('action'),
    //         data: form.serialize(),
    //         headers: {
    //             'X-CSRFToken': csrftoken
    //         },
    //         success: function(response) {
    //             if (response.success) {
    //                 form.closest('li').find('ul').append('<li>' + response.answer.text + ' (' + response.answer.created_at + ')</li>');
    //                 form[0].reset();
    //             } else {
    //                 alert('Failed to add answer: ' + response.error);
    //                 console.error(response.form_errors);  // 폼 오류 메시지 출력
    //             }
    //         },
    //         error: function(xhr, status, error) {
    //             alert('An error occurred: ' + error);
    //             console.error('AJAX request failed:', error);
    //         }
    //     });
    // });
});





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
