 "use strict";


function initializer() {
    navigator.geolocation.getCurrentPosition(function (position) {
        //initMap(position.coords.latitude, position.coords.longitude);
    console.log("does this work?");
    });

}

function initMap() {
    let uluru = {lat: -25.363, lng: 131.044};
    let map = new google.maps.Map(document.getElementById('map'), {
        zoom: 9,
        center: uluru
    });
    let marker = new google.maps.Marker({
        position: uluru,
        map: map
    });
}


// begin the map with the user's location