var rooms = ["bedroom","hall","kitchen","lol"];

document.getElementById("sub1").addEventListener("click",()=>{
    for(var i=1;i<=4;i++){
        if(document.getElementById(i.toString()).checked){
            alert("selected room is "+rooms[i-1]);
            window.location.href = "index2.html";
        }
    }
})