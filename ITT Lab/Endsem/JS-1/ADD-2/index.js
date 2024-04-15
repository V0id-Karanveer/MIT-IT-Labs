var rando = Math.floor(Math.random()*15+1)

document.getElementById("btn").addEventListener('click',()=>{
    var num = parseInt(document.getElementById("inp").value)
    if(num==rando){
        alert("Yay correct!")
        rando = Math.floor(Math.random()*15+1)
    }
    else if(num>rando){
        alert("too high")
    }
    else{
        alert("too low")
    }
})