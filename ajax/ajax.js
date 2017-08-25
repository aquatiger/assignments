"use strict";

function displayer(data){
        //
        // <div class="col-lg-3 col-md-4 col-xs-6" id="borderdiv">
        //     <a href="#" class="d-block mb-4 h-100" id="borderanc" id="card">
        //         <p>phil</p>
        //         <p>unk</p>
        //         <p>k@io.io</p>
        //         <img src=<url>
        //     </a>
        // </div>

    for (let i = 0; i<data.length; i++){
        let person = data[i];    // each person

        let name = $('<p>').text(`Name: ${person.name.first}`);
        let gender = $('<p>').text(`Gender: ${person.gender}`);
        let email = $('<p>').text(`Email: ${person.email}`);
        let pict = $('<img>', {'src': person.picture.thumbnail});

        let anchor = $('<a>', {'class': 'd-block mb-4 h-100'});

        let formatting = $('<div>', {'class': 'col-lg-3 col-md-4 col-xs-6'});

       formatting.append(name, gender, email, pict);

    $('#container').append(formatting);
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
