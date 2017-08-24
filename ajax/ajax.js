"use strict";

function displayer(data){
    for (let i = 0; i<data.length; i++){
        let person = data[i];
        let name = $('<p>').text(`Name: ${person.name.first}`);
        let gender = $('<p>').text(`Gender: ${person.gender}`);
        let email = $('<p>').text(`Email: ${person.email}`);
        let pict = $('<img>', {'src': person.picture.thumbnail});
        // let idCard = `Name: ${name}
        //               Gender: ${gender}
        //               Email: ${email}
        //               ${pict}`;
       let formatting = $('<div>');

       formatting.append(name, gender, email, pict);

    $('#card').append(formatting);
    }

}


function getter(desire) {

    $.ajax({

        url: 'https://api.randomuser.me/',
        method: 'GET',
        data: {'results': desire},
        //Response Callback Below
        success: function (response) {
            displayer(response.results);
            console.log(response);
        },
        error: function (err) {
            console.log(err);
        }
    });
}


// loop over results which are an array to get name, username, email

//need to create a button to get information from a URL

$('#getdata').on('click', function(){
    //read value from input and get
    let d = $('#desired').val();
    getter(d);

});
