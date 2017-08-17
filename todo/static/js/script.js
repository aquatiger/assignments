$("#toDoButton").on('click', function(evt){
    //This is an event handler.
    evt.preventDefault();   // stop page from refreshing
    let x = $('#toDoInput').val();
    let toDoListItem = $("<li>").text(x);
    let toggleButton = $("<span>").text(" X");
    toDoListItem.append(toggleButton);

    toggleButton.on('click', function(){
        "use strict";
        toDoListItem.css({'text-decoration': 'line-through'});

    });



    // console.log(toDoListItem);
    $('#toDoList').append(toDoListItem);

});