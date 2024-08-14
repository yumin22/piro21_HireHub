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
    // 질문 폼 생성
    $(document).on('submit', '#question-form', function(event){
        event.preventDefault();

        var formData = $('#question-form').serializeArray();
        formData.push({name: 'question_submit', value: 'Add Question'});

        var applicantId = $('#load-question').data('applicant-id');
        var url = applicantId + "/question/";

        $.ajax({
            url: url,
            type: 'POST',
            data: $.param(formData),
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(data) {
                console.log('Server response:', data);
                if (data.success) {
                    $('#question_list').append('<li class="individualquestion">' + data.question.text + ' (' + data.question.created_at + ')</li>');
                    $('#id_text').val('');
                } else {
                    alert('Failed to add question: ' + data.error);
                    console.error(data.form_errors);  // 폼 오류 메시지 출력
                }
            },
            error: function(xhr, status, error) {
                alert('An error occurred: ' + error);
                console.error('AJAX request failed:', error);
            }
        });
    });
});

$(document).ready(function() {
    // 질문 삭제
    $(document).on('click', '.deleteQuestionBtn', function() {
        if (!confirm('정말로 이 질문을 삭제하시겠습니까?')) {
            return;
        }

        var questionId = $(this).data('question-id');
        var applicantId = $('#load-question').data('applicant-id');
        var url = applicantId + "/question/" + questionId + "/delete/";

        $.ajax({
            url: url,
            type: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(data) {
                if (data.success) {
                    $('.individualquestion[data-question-id="' + questionId + '"]').remove();
                } else {
                    alert('Failed to delete question: ' + data.error);
                }
            },
            error: function(xhr, status, error) {
                alert('An error occurred: ' + error);
                console.error('AJAX request failed:', error);
            }
        });
    });
});

$(document).ready(function() {
    // 답변 폼 생성
    $(document).on('submit', '.answerForm', function(event){
        event.preventDefault();

        var applicantId = $('#load-question').data('applicant-id');
        console.log(applicantId);
        var url = applicantId + "/question/";
        var form = $('.answerForm');

        $.ajax({
            url: url,
            type: 'POST',
            data: $('.answerForm').serialize(),
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(data) {
                console.log('Server response:', data);
                if (data.success) {
                    form.closest('li').find('ul.answerList').append('<li>' + data.answer.text + ' (' + data.answer.created_at + ')</li>');
                    form[0].reset();
                } else {
                    alert('Failed to add question: ' + data.error);
                    console.error(data.form_errors);  // 폼 오류 메시지 출력
                }
            },
            error: function(xhr, status, error) {
                alert('An error occurred: ' + error);
                console.error('AJAX request failed:', error);
            }
        });
    });
});
