document.addEventListener('DOMContentLoaded', function () {
    const editButton = document.getElementById('edit-button');
    const saveButton = document.getElementById('save-button');
    const editableSpans = document.querySelectorAll('.info span[contenteditable]');

    function loadSavedData() {
        editableSpans.forEach(span => {
            const id = span.id;
            const savedValue = localStorage.getItem(id);
            if (savedValue) {
                span.textContent = savedValue;
            }
        });
    }

    function saveData() {
        editableSpans.forEach(span => {
            const id = span.id;
            const value = span.textContent;
            localStorage.setItem(id, value);
        });
    }

    loadSavedData();

    editButton.addEventListener('click', function () {
        editableSpans.forEach(span => {
            span.setAttribute('contenteditable', 'true');
        });
        editButton.style.display = 'none';
        saveButton.style.display = 'inline-block';
    });

    saveButton.addEventListener('click', function () {
        editableSpans.forEach(span => {
            span.setAttribute('contenteditable', 'false');
        });
        editButton.style.display = 'inline-block';
        saveButton.style.display = 'none';

        saveData();
    });
});
