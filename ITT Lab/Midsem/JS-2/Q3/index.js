oldval = -1;

document.querySelector("#box1").addEventListener("mouseover",(event)=>{
    var triger = event.target;
    var id = triger.id;
    oldval = document.getElementById(id).style.zIndex;
    document.getElementById(id).style.zIndex = 4;


})

document.querySelector("#box1").addEventListener("mouseout",(event)=>{
    var ele = event.target;
    ele.style.zIndex = oldval;
})

document.querySelector("#box2").addEventListener("mouseover",(event)=>{
    var triger = event.target;
    var id = triger.id;
    oldval = document.getElementById(id).style.zIndex;
    document.getElementById(id).style.zIndex = 4;


})

document.querySelector("#box2").addEventListener("mouseout",(event)=>{
    var ele = event.target;
    ele.style.zIndex = oldval;
})

document.querySelector("#box3").addEventListener("mouseover",(event)=>{
    var triger = event.target;
    var id = triger.id;
    oldval = document.getElementById(id).style.zIndex;
    document.getElementById(id).style.zIndex = 4;


})

document.querySelector("#box3").addEventListener("mouseout",(event)=>{
    var ele = event.target;
    ele.style.zIndex = oldval;
})