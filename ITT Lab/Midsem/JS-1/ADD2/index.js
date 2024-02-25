var randomno = Math.floor(Math.random()*15)+1;
console.log(randomno);

document.getElementById("btn").addEventListener("click",()=>{
    var userinp = parseInt(document.getElementById("inp1").value);
    var res = document.querySelector("#res");
    if(userinp===randomno){
        res.innerHTML = "Guessed!";
    }
    else if(userinp<randomno){
        res.innerHTML = "too low";
    }
    else{
        res.innerHTML = "too high";
    }

})