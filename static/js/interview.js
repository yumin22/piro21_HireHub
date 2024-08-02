const requestUserSearch = new XMLHttpRequest();

const searchApplicant = () => {
    const query = document.getElementById('applicant-search-input').value;
    const url = `{% url 'applicants:search_applicant' %}?search_txt=${query}`;
    requestUserSearch.open('GET', url, true);
    requestUserSearch.onreadystatechange = () => {
        if (requestUserSearch.readyState === XMLHttpRequest.DONE) {
            if (requestUserSearch.status < 400) {
                const data = JSON.parse(requestUserSearch.responseText);
                const userSearchResults = document.getElementById('applicant-search-results');
                userSearchResults.innerHTML = '';
                data.forEach(user => {
                    const li = document.createElement('li');
                    li.textContent = user.name;
                    userSearchResults.appendChild(li);
                });
            }
        }
    };
    requestUserSearch.send();
};