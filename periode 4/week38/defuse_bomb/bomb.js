var stoped = false;
var exploded = false;
var countdown;

function start() {
    document.getElementById("timer").innerHTML = "00:05";
    document.getElementById("wire_good").onclick = stopTimer;
    document.getElementById("wire_bad").onclick = explode;

    let timeLeft = 5;

    countdown = setInterval(() => {
        if (stoped || exploded) {
            clearInterval(countdown);
            return;
        }

        timeLeft--;
        document.getElementById("timer").innerHTML = `00:0${timeLeft}`;

        if (timeLeft === 0) {
            clearInterval(countdown);
            explode();
        }
    }, 1000);
}

function stopTimer() {
    stoped = true;
    if (!exploded) {
        document.getElementById("wire_good").style.backgroundColor = "white";
        document.getElementById("timer").classList.add("blinking");
    }
}

function explode() {
    exploded = true;
    clearInterval(countdown);

    if (!stoped) {
        document.getElementById("timer").innerHTML = "";
        document.getElementById("container").style.backgroundImage = "url('explosion.png')";
        document.getElementById("container").style.height = "600px";
    } else {
        document.getElementById("timer").innerHTML = "";
        document.getElementById("wire_bad").style.backgroundColor = "#DFDFDF";
        alert("Bomb defused!");
    }
}

document.addEventListener("DOMContentLoaded", start);
