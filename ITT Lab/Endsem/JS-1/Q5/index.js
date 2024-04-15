document.getElementById("btn").addEventListener('click',()=>{
    var table = document.getElementById("tbl")
    for(var i=1;i<=10;i++){
        var newrow = table.insertRow(-1);
        var cell1 = newrow.insertCell(0)
        var cell2 = newrow.insertCell(1)
        var cell3 = newrow.insertCell(2)
        cell1.innerHTML = i.toString()
        cell2.innerHTML = (i*i).toString()
        cell3.innerHTML = (i*i*i).toString()
    }
})