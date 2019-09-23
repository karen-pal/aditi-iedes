
/*let quotes=[
    "If you tell the truth, you don't have to remember anything.",
    "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.",
    "1lorem",
    "Quote2",
    "qUoTe3",
    "Quote 444444444444"
];

/*function getQuote{
    let indiceRandom= Math.floor(Math.random() * quotes.length)

};*/

//let getQuote = () => quotes[Math.floor(Math.random() * quotes.length)];

//document.getElementById("random-quote").textContent= getQuote();

/* MODAL 1*/ 
var button1 = document.getElementById("button-modal-1");
var modal1 = document.getElementById("page-modal1");
var close1= document.getElementsByClassName("delete")[0];



button1.onclick = function() {
    modal1.style.display= "flex";
}

close1.onclick = function(){
    modal1.style.display = "none";
}

// ---------------------------MODAL 2 --------------------------------
var button2 = document.getElementById("button-modal-2");
var modal2 = document.getElementById("page-modal2");
var close2= document.getElementsByClassName("delete")[1];



button2.onclick = function() {
    modal2.style.display= "flex";
}

close2.onclick = function(){
    modal2.style.display = "none";
}

/* -------------------- MODAL 3------------------------------------- */

var button3 = document.getElementById("button-modal-3");
var modal3 = document.getElementById("page-modal3");
var close3 = document.getElementsByClassName("delete")[2];

button3.onclick = function() {
    modal3.style.display= "flex";
}

close3.onclick = function() {
    modal3.style.display= "none";
}

//-----------------MODAL FORM -------------------
var button4 = document.getElementById("button-modal-form");
var modal4 = document.getElementById("page-modal-form");
var close4 = document.getElementsByClassName("modal-close")[0];

button4.onclick = function() {
    modal4.style.display= "flex";
}

close4.onclick = function() {
    modal4.style.display= "none";
}

//-----------------------------------------------------------
window.onclick = function(event){
    if( event.target.className == "modal-background") {
        this.modal1.style.display = "none";
        this.modal2.style.display = "none";
        this.modal3.style.display = "none";
        this.modal4.style.display = "none"
    }
}

//--------------------------------------------------------


