var kleuren = ["blue", "red", "green", "yellow", "cyan"];

var container = document.getElementById('container')
var body = document.body

kleuren.forEach((color, index) => {
    var button = document.createElement("button");
    button.className = "color-button";
    button.style.backgroundColor = color;
    button.textContent = `Button ${index + 1}`;
    container.appendChild(button);
    if(index ===2 || index ===3 ){
        button.style.width = '150px'
        button.style.fontSize = '30px'
    }
});


const buttons = document.querySelectorAll('#container button');

buttons.forEach((button) => {
    button.addEventListener('click', function() {
        if (button.textContent != `Button 5`){
        alert(`Je hebt op ${button.textContent} geklikt`)
        }else{
            alert('Je hebt niet op Button 1, Button 2, Button 3 of Button 4 gekilkt')
        }
        body.style.background = button.style.backgroundColor

    });
});