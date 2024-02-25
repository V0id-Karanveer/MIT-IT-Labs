var fs = 10;
var inc = true
function dyna(){
    if(fs==10){
        
        inc = true;

    }
    if(fs==50){
        
        inc = false;
    }
    if(inc){
        fs+=5;
        document.querySelector("p").style.fontSize = fs.toString() +"pt";
        document.querySelector("p").style.color = "red";
    }
    else{
        fs-=5;
        document.querySelector("p").style.fontSize = fs.toString() +"pt";
        document.querySelector("p").style.color = "blue";
    }
}

setInterval(dyna,100)
