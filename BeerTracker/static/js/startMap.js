//HARDCODED LOCALIZATIONS
var locations = [
['4hops','https://www.facebook.com/4hops', 51.107827, 17.036095, 12],
['12 krok','https://www.facebook.com/pubdwunastykrok/', 51.101097, 17.025036, 25],
['Ale bosco','https://www.facebook.com/AleBoscoWroclaw/', 51.112914, 17.035666, 75],
['Ale browar','https://www.facebook.com/alebrowarwroclaw/', 51.109729, 17.023122, 60],
['Kontynuacja','https://www.facebook.com/kontynuacja', 51.108446, 17.031682, 50],
['La Famiglia Pizzeria','https://www.facebook.com/LaFamigliaRestauracja/', 51.101368, 17.022805, 57],
['LAMUS', 'https://www.facebook.com/pub.lamus', 51.099820, 17.030245, 25],
['Lumberjack', 'https://www.facebook.com/Pub.Lumberjack/', 51.108406, 17.031682, 44],
['Marynka Piwo', 'https://www.facebook.com/marynkapiwoiaperitivo?fref=ts', 51.107297, 17.030098, 30],
['Browar stu mostów', 'https://100mostow.pl/', 51.131708, 17.059535, 57]
];

var beers = [
['</br>Rychtar natur - 11 zł ', '</br>Czarna Manka - 15 zł', '</br>Holiday IPA - 7 zł', '</br>Brauza - 13 zł','</br>Hoppy Meal - 12 zł'],
['</br>Holiday IPA - 6 zł','</br>Rychtar natur - 11 zł ', '</br>Nyskie Przeniczne - 15 zł', '</br>American Beauty - 17 zł','</br>Ranczo - 14 zł'],
['</br>Shark - 15 zł ', '</br>ART+ - 9 zł', '</br>Wild Pale Ale - 11 zł', '</br>Siostra Bożenka	 - 16 zł','</br>Freaky APA - 9 zł'],
['</br>Black Hope - 8 zł ', '</br>Plaza - 12 zł', '</br>Holiday IPA - 11 zł', '</br>Kirek - 11 zł','</br>Pannepot Reserva - 7 zł'],
['</br>Pšeničny Ležák natur - 13 zł ', '</br>Raj APA - 15 zł', '</br>ART+ - 9 zł', '</br>New Wave Gose - 13 zł','</br>Litovel Premium - 6 zł']
];

// GET icon color
function getIcons(popularity){
value = Math.floor(popularity / 10) * 10;
return "../static/img/pin"+value+".png";
}
var map = new google.maps.Map(document.getElementById('map'), {
zoom: 15,
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
                '<p>Link do facebooka: <b><a href="'+locations[i][1]+'">Click</a></b>'+
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
