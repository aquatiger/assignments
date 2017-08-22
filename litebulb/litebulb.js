

$("#myButton").on('click', function(evt){
    "use strict";
    //This is an event handler
    let state = $(this).attr('data-state');
    if (state === "on") {
        $(this).attr('data-state', "off");
        $('img').attr('src', 'tworabbits.jpg');
    } else if (state === "off") {
        $(this).attr('data-state', "on");
        $('img').attr('src', 'onerabbit.jpg');
    }



});

