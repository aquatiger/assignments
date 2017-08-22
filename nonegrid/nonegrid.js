"use strict";



function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function randomColor() {
    let hexdig = 'abcdef0123456789'.split('');
    let color = '#';
    for (let i=0;i<6;i++){
        // get random number between 0 and len of hexdig
        // use random number to get hexdigit
        // concatenate to the color string
        let x = getRandomInt(0, hexdig.length);
        let hexdigit = hexdig[x];
        color += hexdigit;
    }
    return color
}


$('.subbox').hover(function(){

    // Mouseenter
    // alert('This works');
    // change background color to random color
    // change heading text to match subbox text

}, function(){

    // Mouseleave
    // change text back to default
});