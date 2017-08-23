// image URL entered by the user will be displayed in the album


"use strict";


$('#go').on('click', function(){

    /*
    1. take input and store to a variable
    2. create <img src> with input from step 1
    3. display in album


     */

    let URL = $('#userinput').val();

    let pictureadd = $('<img>', {'src': URL});
    // division the image is in
    let imgdiv = $('<div>', {'class': 'col-lg-3 col-md-4 col-xs-6'});
    // anchor the image is in
    let imganc = $('<a>', {'class': 'd-block mb-4 h-100'});
    //class the image is in
    let imgpic = $('<img>', {'class': 'img-fluid img-thumbnail'});

    // $('#borderdiv>#borderanc').append();

    //append img to anc
    imganc.append(pictureadd);

    // append anc to img container
    imgdiv.append(imganc);

    // append img cont to gallery


    $('#Gallery').append(imgdiv);


    /*
    put borders around each picture


     */

});