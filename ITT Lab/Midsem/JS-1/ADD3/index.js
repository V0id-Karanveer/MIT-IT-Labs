document.getElementById("btn").addEventListener("click",()=>{
    var container = document.getElementById("container");
    var cnt = parseInt(document.getElementById("inp1").value);
    for(var i=1;i<=cnt;i++){
        var text = document.createElement('input');
        var break1 = document.createElement('br');
        var name = document.createElement('label');
        text.type = "text";
        text.id = i.toString();
        name.innerHTML = "salesman "+i.toString();
        container.appendChild(name);
        container.appendChild(text);
        container.appendChild(break1);
    }
    var btn = document.createElement("button"); 
    container.appendChild(btn);
    btn.id = "btn2";
    btn.innerHTML = "lets go";
    document.getElementById("btn2").addEventListener("click",()=>{
        var cntA = 0;
        var cntB = 0;
        for(var i=1;i<=parseInt(document.getElementById("inp1").value);i++){
            var income = 200+parseInt(document.getElementById(i.toString()).value);
            console.log(income);
            if(income<500){
                cntA++;
                
            }
            if(income>=500){
                cntB++;
                
            }
        }
        document.getElementById("a").innerHTML = cntA.toString();
        document.getElementById("b").innerHTML = cntB.toString();
    })
})