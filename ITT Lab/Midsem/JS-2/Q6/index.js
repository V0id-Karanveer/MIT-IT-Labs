for(var i=0;i<2;i++){
    document.getElementById(i.toString()).addEventListener("mouseover",(event)=>{
        var ele = event.target;
        if(ele.id==="0"){
            document.querySelector("body").style.backgroundColor = "green";
        }
        else{
            document.querySelector("body").style.backgroundColor = "blue";
        }
        
    })
}