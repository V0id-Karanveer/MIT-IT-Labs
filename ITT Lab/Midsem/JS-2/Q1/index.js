var n = parseInt(prompt("enter n"));
var fibo = [0,1];

for(var i=2;i<=n;i++){
    fibo.push(fibo[i-1]+fibo[i-2]);
}




var table1 = document.getElementById("tble");
for(var i=0;i<fibo.length;i++){
    var newrow = table1.insertRow(-1);
    var cell1 = newrow.insertCell(0);
    var cell2 = newrow.insertCell(1);
    cell1.innerHTML = i.toString();
    cell2.innerHTML = fibo[i].toString();
}

n = parseInt(prompt("enter n"));
var s = " ";

for(var i=0;i<n;i++){
    s += i.toString() + "   "+(i*i).toString()+"\n";
}

alert(s)