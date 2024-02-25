var cnt = 0;
var num = 0;
var chem = 0;
var phy = 0;

document.getElementById("sub").addEventListener("click",()=>{
    num = parseInt(document.getElementById("num").value);
    document.getElementById("name").textContent = cnt.toString()+"/"+num.toString();
})

document.getElementById("next").addEventListener("click",()=>{
    for(var i=1;i<=2;i++){
        if(document.getElementById(i.toString()).checked){
            
            if(i==1){
                phy+=1;
                document.getElementById("t"+i.toString()).innerHTML = phy.toString();
            }
            else{
                chem+=1;
                document.getElementById("t"+i.toString()).innerHTML = chem.toString();
            }
            
        }
    }
    cnt++;
    document.getElementById("name").textContent = cnt.toString()+"/"+num.toString();
    if(cnt>=num){
        document.getElementById("name").textContent = "done";

        document.getElementById("next").hidden = true;

    }
})