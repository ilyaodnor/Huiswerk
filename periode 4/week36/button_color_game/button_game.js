const amount_of_buttons = 1;
const buttons = [];
const buttonColors = [];
const buttonsLooping = Array(amount_of_buttons).fill(true);
let win = false;
const colors = ["magenta", "cyan", "greenyellow", "blue", "yellow"];

for (let i = 0; i < amount_of_buttons; i++) {
    const button = document.createElement("button");
    button.id = `colorPicker${i + 1}`;
    button.style.margin = "5px";
    container.appendChild(button);
    buttons.push(button);
    
    const colorIndex = Math.floor(Math.random() * colors.length);
    buttonColors.push(colors[colorIndex]);
    button.style.backgroundColor = colors[colorIndex];
    
    button.onclick = function () {
        if (!win) {
            const position = buttons.indexOf(this);
            buttonsLooping[position] = !buttonsLooping[position];
            checkWin();
        }
    };
}

function getNextColor(color) {
    let position = colors.indexOf(color);
    return colors[(position + 1) % colors.length];
}

function checkWin() {
    if (buttonsLooping.every(state => state === false) && buttonColors.every(color => color === buttonColors[0])) {
        let winText = "WIN";
        if (amount_of_buttons % 2 === 0) winText += "!";
        
        let startIndex = Math.floor((amount_of_buttons - winText.length) / 2);
        buttons.forEach((button, index) => button.innerHTML = (index >= startIndex && index < startIndex + winText.length) ? winText[index - startIndex] : "");
        
        win = true;
    }
}

setInterval(() => {
    for (let i = 0; i < buttons.length; i++) {
        if (buttonsLooping[i]) {
            buttonColors[i] = getNextColor(buttonColors[i]);
            buttons[i].style.backgroundColor = buttonColors[i];
        }
    }
}, 500);
