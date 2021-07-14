$(document).ready(function(){
    currentURL = window.location.pathname
    if(currentURL.includes("delete")){
        console.log("OK!");
        superpass = "Are you sure?"
        $("#confirmar").on("click",function(){
            pass = $("#passadmin").val()
            if(pass == superpass){
                $("#borrar").removeAttr('hidden');
                $('#modal').modal('toggle'); 
            }else{
                alert("Contraseña incorrecta!");
            }
        })
        
    }
});