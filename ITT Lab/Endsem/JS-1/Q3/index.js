document.querySelector("#btn").addEventListener('click',()=>{
    var inp = document.getElementById("inp").value
    document.getElementById("area").value = inp.slice(1,4)
    document.getElementById("phoneno").value = inp.slice(5,inp.length)
})