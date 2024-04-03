document.addEventListener('DOMContentLoaded', function () {
    var formVisible = false;
    var toggleFormLink = document.getElementById('form-and-forum-container').querySelector('.sub-link');
    var formContainer = document.getElementById('form-container');
    var forumContainer = document.getElementById('forum-container');

    toggleFormLink.addEventListener('click', function (e) {
        e.preventDefault(); // Prevent the default link behavior
        formContainer.style.display = formVisible ? 'none' : 'block'; // Toggle the form visibility
        forumContainer.style.display = formVisible ? 'block' : 'none'; // Toggle the forum visibility
        formVisible = !formVisible; // Toggle the form visibility flag
    });
});