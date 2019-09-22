
let quotes=[
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

let getQuote = () => quotes[Math.floor(Math.random() * quotes.length)];

document.getElementById("random-quote").textContent= getQuote();