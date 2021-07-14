const weatherURL = "https://api.openweathermap.org/data/2.5/weather?";
const apiKey = "55bc2ec5979b0c7d4bec981ae5b5a0b5";
const lang = "es"; 
var iconWeather = "";
var latUser = 0;
var lngUser = 0;



function getLocation() {
  if (navigator.geolocation) {
    //console.log("OK!")
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    alert("Geolocation is not supported by this browser.");
  }
}

function showPosition(position) {
    //console.log("Entra")
    latUser = position.coords.latitude;
    lngUser = position.coords.longitude;
  }

//Llamado
this.getLocation();

//JQuery
$(document).ready(function(){
    $.get(weatherURL + "lat=" + latUser + "&lon="+ lngUser+ "&units=metric" + "&lang" + lang +"&appid=" + apiKey, function(data){
        // console.log(latUser + " // " + lngUser)
        // console.log(data.weather[0]);
        // console.log(data);
        let weather = (data.weather[0].main)
        
        //Tiempo textual
        $('#weatherText').text(data.weather[0].description)
        
        //Grados actuales
        let currentWeather = (data.main.temp.toFixed() + " ºC")
        $('#currentWeather').text(currentWeather)
        
        //Icono
        icon = data.weather[0].icon;
        iconWeather = "http://openweathermap.org/img/wn/"+ icon +"@2x.png"
        $('#iconWeather').attr("src", iconWeather);
    });

});

