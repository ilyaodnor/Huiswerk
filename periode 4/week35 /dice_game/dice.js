const dice = document.getElementById("dice"), log = document.getElementById("log");
let timer, score = 0, currentFace = 0;
const faces = [
    [1, 'dice_face_1.png', "You rolled a 1"],
    [2, 'dice_face_2.png', "You rolled a 2"],
    [3, 'dice_face_3.png', "You rolled a 3"],
    [4, 'dice_face_4.png', "You rolled a 4"],
    [5, 'dice_face_5.png', "You rolled a 5"],
    [6, 'dice_face_6.png', "You rolled a 6"]
];

dice.style.backgroundImage = `url('${faces[0][1]}')`;

dice.onclick = () => {
    if (!timer) return;
    clearInterval(timer);
    timer = null;
    log.prepend(Object.assign(document.createElement("p"), { innerHTML: faces[currentFace][2] }));
    if ((score += faces[currentFace][0]) >= 18) return alert(`You win, score: ${score}`);
    setTimeout(startRoll, 1500);
};

function startRoll() {
    timer = setInterval(() => {
        dice.style.backgroundImage = `url('${faces[currentFace = (currentFace + 1) % 6][1]}')`;
    }, 50);
}

startRoll();