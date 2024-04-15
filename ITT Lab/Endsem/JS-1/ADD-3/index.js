var num = 0
document.getElementById("btn").addEventListener('click',()=>{
    num = parseInt(document.getElementById("inp").value)
    var cont = document.getElementById("cont")
    for(var i=0;i<num;i++){
        var textbox = document.createElement('input')
        textbox.id = i.toString()
        textbox.type = "text"
        var name = document.createElement('p')
        name.innerHTML = "Salesman "+(i+1).toString()
        cont.appendChild(name)
        cont.appendChild(textbox)
    }
    document.getElementById("btn2").hidden = false
})

document.getElementById("btn2").addEventListener('click',()=>{
    var r0 = 0
    var r1 = 0
    for(var i=0;i<num;i++){
        price = 200+0.09*parseFloat(document.getElementById(i.toString()).value)
        console.log(price)
        if(price > 500){
            r1+=1
        }
        if(price<=500){
            r0+=1
        }
    }
    console.log(r1)
    console.log(r0)
    document.getElementById("r1").innerHTML = r1.toString()
    document.getElementById("r0").innerHTML = r0.toString()
})