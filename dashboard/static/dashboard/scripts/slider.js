$(document).ready(function(){
    currentURL = window.location.pathname
    if(currentURL.includes("slider" && "detail" )){
        console.log("OK!");
        imgURL = $("#imgURL").text();
        imgURL = imgURL.slice(12)
        console.log(imgURL);
        $("#imgSlider").attr("src", "{% static" + "'" + imgURL + "'" + "%}")

        
    }
});