var list = ""

document.getElementById("btn").addEventListener('click',()=>{
    var inp = document.getElementById("inp").value 
    for(var i=0;i<3;i++){
        var a = inp[i]
        for(var j=i+1;j<4;j++){
            var b = inp[j]
            for(var k=j+1;k<5;k++){
                var c=inp[k]
                list = list + a + b + c +", "
                list = list + a + c + b +", "
                list = list + b + a + c +", "
                list = list + b + c + a +", "
                list = list + c + b + a +", "
                list = list + c + a + b +", "
            }
        }
    }
    document.getElementById("out").innerHTML = list
})