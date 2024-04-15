document.getElementById("btn").addEventListener('click',()=>{
    for(var i=0;i<3;i++){
        if(document.getElementById("rd"+(i+1).toString()).checked){
            localStorage.setItem("key",document.getElementById("rd"+(i+1).toString()).value)
            break;
        }
    }
    s = ""
    for(var i=0;i<2;i++){
        
        if(document.getElementById("cb"+(i+1).toString()).checked){
            s+=document.getElementById("cb"+(i+1).toString()).value
        }
    }
    localStorage.setItem("key2",s)
    location.href = "index2.html"
})