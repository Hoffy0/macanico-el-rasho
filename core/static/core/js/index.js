//##### Slider #####
if(document.getElementsByClassName("slider").length > 0){
    //console.log("hay un slider")
    const slider = document.querySelector("#slider");
    var sliderSection = document.querySelectorAll(".slider-section");
    var sliderSectionLast = sliderSection[sliderSection.length - 1]

    const btnRight = document.querySelector("#btn-right");
    const btnLeft = document.querySelector("#btn-left");

    slider.insertAdjacentElement('afterbegin', sliderSectionLast);

    //Slider move right
    function moveRight(){
        let sliderSectionFirst = document.querySelectorAll(".slider-section")[0];
        slider.style.marginLeft = "-200%";
        slider.style.transition = "all 0.5s";
        setTimeout(function(){
            slider.style.transition = "none";
            slider.insertAdjacentElement('beforeend', sliderSectionFirst);
            slider.style.marginLeft = "-100%";
        }, 500);

    }

    btnRight.addEventListener('click', function(){
        moveRight();
    });

    //Slider move left
    function moveLeft(){
        var sliderSection = document.querySelectorAll(".slider-section");
        var sliderSectionLast = sliderSection[sliderSection.length - 1]
        slider.style.marginLeft = "0";
        slider.style.transition = "all 0.5s";
        setTimeout(function(){
            slider.style.transition = "none";
            slider.insertAdjacentElement('afterbegin', sliderSectionLast);
            slider.style.marginLeft = "-100%";
        }, 500);

    }

    btnLeft.addEventListener('click', function(){
        moveLeft();
    });

    //Move auto
    setInterval(function(){
        moveRight();
    }, 4000);

    }else{
        //console.log("no hay un slider")

    }


//###############################################