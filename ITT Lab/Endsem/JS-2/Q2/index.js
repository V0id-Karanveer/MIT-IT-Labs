document.getElementById("btn2").addEventListener('click',()=>{
    var str = document.getElementById("inp").value 
    var str2 = ""
    for(var i=str.length-1;i>=0;i--){
        str2+=str[i]
    }
    document.getElementById("para").innerHTML = str2
})

document.getElementById("btn1").addEventListener('click',()=>{
    var str = document.getElementById("inp").value 
    var str2 = ""
    for(var i=0;i<str.length;i++){
        if(str[i]=='a' || str[i]=='e' || str[i]=='i' || str[i]=='o' || str[i]=='u'){
            document.getElementById("para").innerHTML = str[i]
            break
        }
    }
    
})