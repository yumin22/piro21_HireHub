$(document).ready(function(){
    $('#load-comment').click(function(){
        var applicantId = $(this).data('applicant-id');
        console.log(applicantId);
        var url = applicantId + "/comment/";

        $.ajax({
            url: url,
            type: "GET",
            success: function(response){
                $('.profile_logo').html(
                    `<span>코멘트 작성</span>`
                );
                $('.profile_section').hide();
                $('#comment-section').show();
                $('#comment-section').html(response);
            },
            error: function(response){
                alert("Error loading comment.");
            }
        });
    });
});

$(document).ready(function(){
    $('#load-profile').click(function(){
        var applicantId = $(this).data('applicant-id');
        console.log(applicantId);
        var url = applicantId;

        $.ajax({
            url: url,
            type: "GET",
            success: function(response){
                $('.profile_logo').html(
                    `<span>지원자 프로필</span>`
                );
                $('.profile_section').show();
                $('#comment-section').hide();
            },
            error: function(response){
                alert("Error loading profile.");
            }
        });
    });
});

// 녹음 ajax
let mediaRecorder;
let recordedChunks = [];
let isRecording = false;


if ('serviceWorker' in navigator) {
navigator.serviceWorker.getRegistrations().then(function(registrations) {
    for(let registration of registrations) {
        registration.unregister();
    }
}).catch(function(error) {
    console.log('ServiceWorker unregistration failed: ', error);
});
}

async function startRecording() {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = event => {
        if (event.data.size > 0) {
            recordedChunks.push(event.data);
        }
    };

    mediaRecorder.onstop = () => {
        const audioBlob = new Blob(recordedChunks, { type: 'audio/webm' });
        const audioUrl = URL.createObjectURL(audioBlob);
        document.getElementById('audioPlayback').src = audioUrl;
        document.getElementById('audioPlayback').style.display = 'block';

        // 녹음 파일 서버 업로드
        uploadRecording(audioBlob);
        showDeleteButton();  // 파일 업로드 후 삭제 버튼 표시
    };

    mediaRecorder.start();
    isRecording = true;
}

function stopRecording() {
    if (mediaRecorder && isRecording) {
        mediaRecorder.stop();
        isRecording = false;
    }
}

document.getElementById('recordBtn').onclick = async () => {
    if (!isRecording) {
        await startRecording();
        document.getElementById('recordBtn').textContent = '녹음 중지';
    } else {
        stopRecording();
        document.getElementById('recordBtn').textContent = '녹음';
    }
};

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

function uploadRecording(blob) {
    const csrftoken = getCookie('csrftoken');
    const formData = new FormData();
    formData.append('audio_data', blob, "{{ applicant.name }}.webm");

    fetch(window.location.href, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': csrftoken,  // CSRF 토큰을 헤더에 포함
        },
        credentials: 'same-origin'  // 쿠키를 포함하기 위해 추가
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.file_url) {
            console.log('File uploaded successfully:', data.file_url);
        } else {
            console.error('File upload failed:', data);
        }
    })
    .catch(error => {
        console.error('Upload error:', error);
    });
}

function goBack() {
    window.history.back();
}

window.addEventListener('beforeunload', function (e) {
    if (isRecording) {
        const confirmationMessage = "녹음 중입니다. 페이지를 떠나면 녹음이 중단됩니다.";
        e.returnValue = confirmationMessage; // 일부 브라우저에서 필요
        return confirmationMessage; // 대부분의 브라우저에서 필요
    }
});

document.getElementById('deleteRecordingBtn').onclick = function() {
    if (confirm('정말로 녹음 파일을 삭제하시겠습니까?')) {
        deleteRecording();
    }
};

function deleteRecording() {
const csrftoken = getCookie('csrftoken');

// 정확한 경로 지정: 슬래시('/') 추가
const deleteUrl = `${window.location.origin}${window.location.pathname}/delete/`;

fetch(deleteUrl, {
    method: 'POST',
    headers: {
        'X-CSRFToken': csrftoken,
    },
    credentials: 'same-origin'
})
.then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
})
.then(data => {
    if (data.success) {
        console.log('File deleted successfully');
        document.getElementById('audioPlayback').style.display = 'none';
        document.getElementById('deleteRecordingBtn').style.display = 'none';
    } else {
        console.error('File deletion failed:', data.error);
    }
})
.catch(error => {
    console.error('Deletion error:', error);
});
}


function showDeleteButton() {
    const deleteBtn = document.getElementById('deleteRecordingBtn');
    deleteBtn.style.display = 'block';
}
