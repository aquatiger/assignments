$.ajax({

    url: 'https://api.randomuser.me/',
    method: 'GET',
    data: {'results': '5'},
    //Response Callback Below
    success: function(response){
        console.log(response)
    },
    error: function(err){
        "use strict";
        console.log(err);
    },
});