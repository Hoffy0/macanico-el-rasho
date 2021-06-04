const API_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/";
var MAKE_ID = 0;

$(document).ready(function(){
    
    $.get(API_URL + "getallmakes?format=json", function(data){
        //console.log(data.Results)
        $.each(data.Results, function(i, item){
            //console.log(data.Results[i].Make_Name)
            $('#carsSelect').append($("<option>", {
                value: data.Results[i].Make_ID,
                text: data.Results[i].Make_Name
            }));
            
            
        })
    });

    $('#carsSelect').change(function(){
        MAKE_ID = $(this).val();
        //console.log(MAKE_ID);
    });   


    function mostrar(){
        if(MAKE_ID == 0 || MAKE_ID == null || MAKE_ID == undefined || MAKE_ID == ""){
            alert("Status: 404");

        }else{
            $('#carsTable tbody').empty();
            $.get(API_URL + "GetModelsForMakeId/" + MAKE_ID + "?format=json", function(data){
                //console.log(data.Results);
                $.each(data.Results, function(i, item){
                    var tableHtml = '<tr>'+
                                        '<td scope="row">' + data.Results[i].Model_ID + '</td>'+
                                        '<td>' + data.Results[i].Make_Name + '</td>'+
                                        '<td>' + data.Results[i].Model_Name + '</td>'+
                                    '</tr>';
                    $('#carsTable tbody').append(tableHtml);
                })
            });

        }
        
    }
    
    $("#carbtn").click(mostrar);
    
    // '<tr>'+
    //     '<td>' + Id + '</td>'+
    //     '<td>' + Nombres + '</td>'+
    //     '<td>' + ApellidoP + '</td>'+
    //     '<td>' + AppellidoM + '</td>'+
    // '</tr>';

    // $('#cars').append($("<option>", {
    //     value: "hola",
    //     text: "hola"
    // }));
});