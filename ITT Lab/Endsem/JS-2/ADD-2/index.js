document.addEventListener('click',(event)=>{
    if(event.ctrlKey){
        alert("ctrl pressed")
    }
    else if(event.shiftKey){
        alert("shift pressed")
    }
    else{
        alert("just mouse")
    }
})