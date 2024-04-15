document.getElementById("para").innerHTML = localStorage.getItem("key")

document.getElementById("btn").addEventListener('click',()=>{
    var rad1 = document.getElementById('rd1')
    var rad2 = document.getElementById('rd2')
    var cb1 = document.getElementById('cb1')
    var cb2 = document.getElementById('cb2')
    if(rad1.checked){
        document.getElementById('o1').innerHTML = rad1.value 
    }
    else{
        document.getElementById('o1').innerHTML = rad2.value 
    }
    s = ""
    if(cb1.checked){
        s+= cb1.value 
    }
    
    if(cb2.checked){
        s+=cb2.value
    }
    document.getElementById('o2').innerHTML = s
    var selected = document.getElementById("sel").value
    document.getElementById('o4').innerHTML = selected
    var datetime = document.getElementById("date").value
    document.getElementById('o3').innerHTML = datetime
    document.getElementById('tbl').hidden = false
})