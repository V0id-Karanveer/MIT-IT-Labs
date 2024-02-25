document.querySelector("#enter").addEventListener("click",()=>{
    var inp = document.querySelector("#imp").value;
    var splt = inp.split("(")[1].split(")");
    
    document.getElementById("area").value = splt[0];
    var no = splt[1].split("-");
    document.getElementById("phone").value = no[0]+no[1];
    

})




