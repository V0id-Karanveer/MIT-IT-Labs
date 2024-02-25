document.getElementById("sub").addEventListener("click",()=>{
    document.querySelector("p").innerHTML = "printing";

    var inp = document.getElementById("five").value;
    var temp = "";
    var ans = [];
    for (var i = 0; i < 5; i++) {
        for (var j = 0; j < 5; j++) {
            for (var k = 0; k < 5; k++) {
                if (i != j && j != k && i != k) {
                    var temp = inp[i] + inp[j] + inp[k];
                    ans.push(temp);
                }
            }
        }
    }
    document.querySelector("p").innerHTML = ans.toString();
})


