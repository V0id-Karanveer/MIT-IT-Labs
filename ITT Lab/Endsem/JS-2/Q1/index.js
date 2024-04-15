function fibo(n){
    var list = [0,1]
    for(var i=2;i<n;i++){
        list.push(list[i-1]+list[i-2])
    }
    return list;
}

function sqr(n){
    var list = []
    for(var i=1;i<=n;i++){
        list.push(i*i)
    }
    return list
}

document.getElementById("btn").addEventListener('click',()=>{
    var n = parseInt(document.getElementById("inp").value)
    var l1 = fibo(n)
    var s = ""
    for(var i=0;i<n;i++){
        s+=(i+1).toString()+"  "+l1[i].toString()+"\n";
    }
    alert(s)
})

document.getElementById("btn2").addEventListener('click',()=>{
    var n = parseInt(document.getElementById("inp").value)
    var l1 = sqr(n)
    s = ""
    for(var i=0;i<n;i++){
        s+=(i+1).toString()+"  "+l1[i].toString()+"\n"
    }
    alert(s)
})