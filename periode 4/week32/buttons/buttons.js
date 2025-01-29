var kleur1 = "blue";
var kleur2 = "red";
var kleur3 = "green";
var kleur4 = "yellow";
var kleur5 = "cyan";
var kleur6 = "magenta";

function makeButton1() {
    var button1 = document.createElement('button');
    button1.style.backgroundColor = kleur1;
    button1.id = "button1";
    button1.innerText = "Button 1";
    document.getElementById("container").appendChild(button1);
}

function onClickButton1(){
    document.body.style.backgroundColor = kleur1;
    alert("Je hebt op Button 1 gekilkt");
}

function makeButton2() {
    var button2 = document.createElement('button');
    button2.style.backgroundColor = kleur2;
    button2.innerText = "Button 2";
    button2.id = "button2";
    button2.className = "hoger";
    document.getElementById("container").appendChild(button2);
}

function onClickButton2(){
    document.body.style.backgroundColor = kleur2;
    alert("Je hebt op Button 2 gekilkt");
}

function makeButton3() {
    var button3 = document.createElement('button');
    button3.style.backgroundColor = kleur3;
    button3.innerText = "Button 3";
    button3.id = "button3";
    button3.className = "groter";
    document.getElementById("container").appendChild(button3);
}

function onClickButton3(){
    document.body.style.backgroundColor = kleur3;
    alert("Je hebt op Button 3 gekilkt");
}

function makeButton4() {
    var button4 = document.createElement('button');
    button4.style.backgroundColor = kleur4;
    button4.style.color = "black";
    button4.innerText = "Button 4";
    button4.id = "button4";
    button4.className = "groter";
    document.getElementById("container").appendChild(button4);
}

function onClickButton4(){
    document.body.style.backgroundColor = kleur4;
    alert("Je hebt op Button 4 gekilkt");
}

function makeButton5() {
    var button5 = document.createElement('button');
    button5.style.backgroundColor = kleur5;
    button5.style.color = "black";
    button5.innerText = "Button 5";
    button5.id = "button5";
    document.getElementById("container").appendChild(button5);
}

function onClickButton5(){
    document.body.style.backgroundColor = kleur5;
    alert("Je hebt niet op Button 1, Button 2, Button 3 of Button 4 gekilkt");
}

function makeButton6() {
    var button6 = document.createElement('button');
    button6.style.backgroundColor = kleur6;
    button6.innerText = "Button 6";
    button6.id = "button6";
    document.getElementById("container").appendChild(button6);
}

function onClickButton6(){
    document.body.style.backgroundColor = kleur6;
    alert("Je hebt niet op Button 6 gekilkt");
}


makeButton1();
makeButton2();
makeButton3();
makeButton4();
makeButton5();

document.getElementById("button1").onclick = onClickButton1;
document.getElementById("button2").onclick = onClickButton2;
document.getElementById("button3").onclick = onClickButton3;
document.getElementById("button4").onclick = onClickButton4;
document.getElementById("button5").onclick = onClickButton5;