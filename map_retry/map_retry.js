"use strict";



function initMap(lat, lng) {
    let center = {lat: lat, lng: lng};

    let map = new google.maps.Map(document.getElementById('map'), {
      zoom: 9,
      center: center
    });

    let marker = new google.maps.Marker({
      position: center,
      map: map
    });
}



function initializer() {
    // Get current position from browser
    navigator.geolocation.getCurrentPosition(function (position) {
        initMap(position.coords.latitude, position.coords.longitude);
    });
}
