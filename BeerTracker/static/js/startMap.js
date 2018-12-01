  //HARDCODED LOCALIZATIONS
var locations = [
  ['4hops','https://www.facebook.com/4hops', 51.107827, 17.036095, 33],
  ['12 krok','https://www.facebook.com/pubdwunastykrok/', 51.101097, 17.025036, 70]
];

var beers = [
  ['</br>Piwo1 - Cena zł ', '</br>Piwo2 - Cena zł', '</br>Piwo3 - Cena zł', '</br>Piwo4 - Cena zł'],
  ['</br>Piwo1 - Cena zł ', '</br>Piwo2 - Cena zł', '</br>Piwo3 - Cena zł', '</br>Piwo4 - Cena zł']
];

// GET icon color
function getIcons(popularity){
  value = Math.floor(popularity / 10) * 10;
  return "../static/img/pin"+value+".png";
}
var map = new google.maps.Map(document.getElementById('map'), {
  zoom: 13,
  center: {lat: 51.1071467, lng: 17.040798}
});

  var infowindow = new google.maps.InfoWindow();

  var marker, i;
  // get JSON with parsed ("NAME",Latitude, Longitude, current_popular)
  for (i = 0; i < locations.length; i++) {
    marker = new google.maps.Marker({
      position: new google.maps.LatLng(locations[i][2], locations[i][3]),
      icon: getIcons(locations[i][4]),
      map: map
    });

    google.maps.event.addListener(marker, 'click', (function(marker, i) {
      return function() {
        $.ajax({
          type:"GET",
          url: "https://url.pl/apiget",
          complete: function(data) {
            var beer = beers[i].toString();
              infowindow.setContent('<div id="content">'+
                  '<div id="siteNotice">'+
                  '</div>'+
                  '<h1 id="firstHeading" class="firstHeading">'+locations[i][0]+'</h1>'+
                  '<div id="bodyContent">'+
                  '<p><b>Popularność: '+ locations[i][4]+
                  '</b></p>'+
                  '<p>Piwa:'+beer+'</p>'+
                  '<p>Link do facebooka: <b><a href="'+locations[i][2]+'">Click</a></b>'+
                  '</div>'+
                  '</div>');
              infowindow.open(map, marker);
          },
          error: function(jqXHR, textStatus, errorThrown) {
            },
          dataType: "jsonp"
        });

      }
    })(marker, i));
  }
