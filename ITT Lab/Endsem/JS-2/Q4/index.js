var regex = /[1-4]{1}[A-Z]{2}[0-9]{2}[A-Z]{2}[1-9]{3}/

document.getElementById("btn").addEventListener('click',()=>{
    var usn = document.getElementById("inp").value 
    var res = regex.test(usn)
    if(!res){
        alert("wrong input")
    }
    else{
        alert("Correct!")
    }
})