  //HARDCODED LOCALIZATIONS
var locations = [
  ['SKS', 51.108709, 17.059791, 12],
  ['Cyber', 51.113023, 17.05571, 70]
];

// GET icon color
function getIcons(popularity){
  value = Math.floor(popularity / 10) * 10;
  return "../img/pin"+value+".png";
}
var map = new google.maps.Map(document.getElementById('map'), {
  zoom: 13,
  center: {lat: 51.1071467, lng: 17.040798},
});

  var infowindow = new google.maps.InfoWindow();

  var marker, i;
  // get JSON with parsed ("NAME",Latitude, Longitude, current_popular)
  for (i = 0; i < locations.length; i++) {
    marker = new google.maps.Marker({
      position: new google.maps.LatLng(locations[i][1], locations[i][2]),
      icon: getIcons(locations[i][3]),
      map: map
    });

    google.maps.event.addListener(marker, 'click', (function(marker, i) {
      return function() {
        infowindow.setContent(locations[i][0]);
        infowindow.open(map, marker);
      }
    })(marker, i));
  }
