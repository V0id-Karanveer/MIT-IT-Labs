var num = 0
document.getElementById("btn").addEventListener('click',()=>{
    num = parseInt(document.getElementById("numcust").value)
    var cont = document.getElementById("container")
    for(var i=0;i<num;i++){
        var textbox = document.createElement('input')
        var name = document.createElement('p')
        textbox.type = 'text'
        textbox.id = i.toString()
        name.innerHTML = "Customer "+i.toString()
        cont.appendChild(name)
        cont.appendChild(textbox)
    }
    document.getElementById("btn2").hidden = false    
})

document.getElementById("btn2").addEventListener('click',()=>{
    var table = document.getElementById("tbl")
    for(var i=0;i<num;i++){
        var newrow = table.insertRow(-1)
        var cell1 = newrow.insertCell(0)
        var cell2 = newrow.insertCell(1)
        var hours = parseInt(document.getElementById(i.toString()).value)
        if(hours>3){
            var price = 2.00+0.5*(hours-3)
        }
        else{
            var price = 2.00
        }
        cell1.innerHTML = i.toString()
        cell2.innerHTML = price.toString()
        
    }
})