var old_index = -1

document.getElementById("c1").addEventListener('mouseover',(event)=>{
    var cont = event.target
    old_index = cont.style.zIndex 
    cont.style.zIndex = 3

})

document.getElementById("c1").addEventListener('mouseout',(event)=>{
    var cont = event.target
    cont.style.zIndex = old_index
})

document.getElementById("c2").addEventListener('mouseover',(event)=>{
    var cont = event.target
    old_index = cont.style.zIndex 
    cont.style.zIndex = 3

})

document.getElementById("c2").addEventListener('mouseout',(event)=>{
    var cont = event.target
    cont.style.zIndex = old_index
})

document.getElementById("c3").addEventListener('mouseover',(event)=>{
    var cont = event.target
    old_index = cont.style.zIndex 
    cont.style.zIndex = 3

})

document.getElementById("c3").addEventListener('mouseout',(event)=>{
    var cont = event.target
    cont.style.zIndex = old_index
})