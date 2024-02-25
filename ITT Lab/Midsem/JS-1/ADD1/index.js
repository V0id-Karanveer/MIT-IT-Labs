var numofcust = 0;

document.getElementById("btn").addEventListener("click",()=>{
    var cont = document.getElementById("container1");
    numofcust = parseInt(document.getElementById("noofcust").value);
    for(var i=1;i<=numofcust;i++){
        var textbox = document.createElement('input');
        var break1 = document.createElement('br');
        var p = document.createElement("label");
        textbox.id = i.toString();
        textbox.type = "text";
        p.innerHTML = "Customer "+i.toString() + " ";
        cont.appendChild(p);
        cont.appendChild(textbox);
        cont.appendChild(break1);

    }
    var btn_submit = document.createElement("button");
    btn_submit.id = "btn2";
    btn_submit.innerHTML = "calc"
    cont.appendChild(btn_submit);
    document.getElementById("btn2").addEventListener("click",()=>{
        var table = document.getElementById("anstable");
        for(var i=1;i<=numofcust;i++){
            var hours = parseInt(document.getElementById(i.toString()).value);
            var cost = 2.00;
            if(hours>3){
                cost+= 0.5*(hours-3);
            }
            var newrow = table.insertRow(-1);
            var cell1 = newrow.insertCell(0);
            var cell2 = newrow.insertCell(1);
            cell1.innerHTML = i.toString();
            cell2.innerHTML = cost.toString();
    
        }
    })
})

