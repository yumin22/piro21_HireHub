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
    // POST
    $(document).on('submit', '#comment-form', function(event){
        event.preventDefault();

        var applicantId = $('#load-comment').data('applicant-id');
        console.log(applicantId);
        var url = applicantId + "/comment/";

        $.ajax({
            url: url, //$('#comment-form').attr('action'), // 폼의 액션 URL을 사용
            type: 'POST',
            data: $('#comment-form').serialize(),
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(data) {
                console.log('Server response:', data); // 응답 데이터 로그 출력
                if (data.success) {
                    $('#comment_list').append(
                        `<div class="comment"><small><strong>작성자:</strong> ${data.comment.interviewer}</small><p>| ${data.comment.text}</p></div>`
                    );
                    $('#id_text').val(''); // 입력 필드를 비웁니다.
                } else {
                    alert(data.error);
                    console.error(data.form_errors); // 폼 오류 메시지 출력
                }
            },
            error: function(xhr, status, error) {
                console.error('AJAX request failed: ' + error);
            }
        });
    })
})



// $(document).ready(function() {
//     console.log('Document is ready'); // JavaScript 코드 실행 확인

//     function getCookie(name) {
//         let cookieValue = null;
//         if (document.cookie && document.cookie !== '') {
//             const cookies = document.cookie.split(';');
//             for (let i = 0; i < cookies.length; i++) {
//                 const cookie = cookies[i].trim();
//                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                     break;
//                 }
//             }
//         }
//         return cookieValue;
//     }
//     const csrftoken = getCookie('csrftoken');

//     $('#comment-form').submit(function(event) {
//         event.preventDefault();
//         console.log('Form submitted'); // 폼 제출 확인
//         $.ajax({
//             url: $(this).attr('action'), // 폼의 액션 URL을 사용
//             type: 'POST',
//             data: $(this).serialize(),
//             headers: {
//                 'X-CSRFToken': csrftoken
//             },
//             success: function(data) {
//                 console.log('Server response:', data); // 응답 데이터 로그 출력
//                 if (data.success) {
//                     $('#comment-list').append(
//                         `<div class="comment"><p>${data.comment.text}</p><small>By ${data.comment.interviewer} on ${data.comment.created_at}</small></div>`
//                     );
//                     $('#id_text').val(''); // 입력 필드를 비웁니다.
//                 } else {
//                     alert(data.error);
//                     console.error(data.form_errors); // 폼 오류 메시지 출력
//                 }
//             },
//             error: function(xhr, status, error) {
//                 console.error('AJAX request failed: ' + error);
//             }
//         });
//     });
// });
