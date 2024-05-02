function toggleFaq(index) {
    var answer = document.getElementById('answer-' + index);
    var button = answer.previousElementSibling; // This targets the button element
    var expanded = button.getAttribute('aria-expanded') === 'true';
    answer.style.display = expanded ? 'none' : 'block';
    button.setAttribute('aria-expanded', !expanded);
}