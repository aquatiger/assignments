$('#foo').click(function() {
    "use strict";

    alert('This works');

    $('#foo').animate({
        right: "+=500",
        height: "toggle"
    }, 'fast', function(){
        // Animation complete
    });

});