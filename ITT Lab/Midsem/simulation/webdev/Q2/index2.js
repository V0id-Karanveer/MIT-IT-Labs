var furn = ["bed","sofa","table"];

document.getElementById("sub2").addEventListener("click",()=>{
    var table = document.getElementById("table1");
    for(var i=1;i<=3;i++){
        if(document.getElementById(i.toString()).checked){
            var total = document.getElementById("q"+i.toString()).value*document.getElementById("a"+i.toString()).value;
            console.log(total);
            var newrow = table.insertRow(-1);
            var cell1 = newrow.insertCell(0);

            var cell2 = newrow.insertCell(1);
            cell1.innerHTML = furn[i-1];
            cell2.innerHTML = total.toString();
        }
    }
})