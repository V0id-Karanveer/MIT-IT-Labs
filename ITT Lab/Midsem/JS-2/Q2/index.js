document.getElementById("btn1").addEventListener("click",()=>{
    var str = document.getElementById("txt1").value;
    for(var i=0;i<str.length;i++){
        if(str[i] === 'a' || str[i] === 'e' || str[i] === 'i' || str[i] === 'o' || str[i] === 'u'){
            document.querySelector("p").innerHTML = i.toString();
            break;
        }
    }
})

document.getElementById("btn2").addEventListener("click",()=>{
    var str = document.getElementById("txt1").value;
    var str2 = "";
    for(var i = str.length-1;i>=0;i--){
        str2+=str[i];
    }
    document.querySelector("p").innerHTML = str2;
})
