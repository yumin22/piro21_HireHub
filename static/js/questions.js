$(document).ready(function() {
    $('#question-form').submit(function(e) {
        e.preventDefault();
        // 기존 폼 데이터를 가져옴
        var formData = $('#question-form').serializeArray();

        // 폼 데이터에 question_submit 항목 추가
        formData.push({ name: 'question_submit', value: 'Add Question' });

        $.ajax({
            type: 'POST',
            url: $('#question-form').attr('action'),
            data: $.param(formData),
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(response) {
                if (response.success) {
                    $('#question_list').append(
                        '<li class="individualquestion" data-question-id="' + response.question.id + '">' +
                        '<div class="question" data-question-id="' + response.question.id + '">' +
                        '질문: ' + response.question.text +
                        '<ul></ul>' + // 새 질문에 대한 답변 리스트
                        '<button class="deleteQuestionBtn" data-question-id="' + response.question.id + '">삭제</button>' +
                        '</div></li>'
                    );
                    $('#question-form')[0].reset();
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
