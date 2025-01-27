var btn = document.createElement('button');
btn.style.margin = '10px';
btn.innerHTML = 'light off';
document.body.appendChild(btn);

var body = document.body;

btn.addEventListener('click', function() {
    if (body.style.backgroundColor === 'yellow') {
        body.style.backgroundColor = 'white';
        btn.innerHTML = 'light off'; ;
    } else if (body.style.backgroundColor === 'green') {
        body.style.backgroundColor = 'white';
        
    } else {
        body.style.backgroundColor = 'yellow';
        btn.innerHTML = 'light on';
    }
});