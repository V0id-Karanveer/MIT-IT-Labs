document.getElementById("btn").addEventListener('click',()=>{

    var user = document.getElementById("inp").value
    var pass = document.getElementById("pass").value
    if(user==="yo" && pass==="yo"){
        localStorage.setItem("key",user)
        location.href = "index2.html"
    }
    else{
        alert('wrong pass/user')
    }
    
})