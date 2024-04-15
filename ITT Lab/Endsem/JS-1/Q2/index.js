document.getElementById("btn1").addEventListener('click' , ()=>{
    var s = document.getElementById("inp").value;
    document.getElementById("out").innerHTML = s.slice(1,s.length) + s[0]+"ay";
})