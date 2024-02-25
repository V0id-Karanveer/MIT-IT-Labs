document.querySelector("button").addEventListener("click",()=>{
    var str = document.querySelector("#word").value;
    document.querySelector("p").innerHTML = str.slice(1,str.length) + str[0]+"ay";

})