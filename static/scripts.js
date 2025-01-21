// static/script.js
function validateForm() {
    let valid = true;
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.querySelectorAll('input, textarea').forEach(input => {
            if (!input.value.trim()) {
                input.style.borderColor = 'red';
                valid = false;
            }
        });
    });
    return valid;
}