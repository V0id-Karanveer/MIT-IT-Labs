
var size = 10
var para = document.getElementById("para")
flg = 1
function changesize(){
    if(flg==1){
        if(size==50){
            flg = 0
            size -=1
            para.style.fontSize = size.toString() +'pt';
            para.style.color = "green"
        }
        else{
            size+=1
            para.style.fontSize = size.toString() +'pt';
        }
    }
    else{
        if(size==10){
            flg = 1
            size +=1
            para.style.fontSize = size.toString() +'pt';
            para.style.color = "red"
        }
        else{
            size-=1
            para.style.fontSize = size.toString() +'pt';
        }
    }
    
}
setInterval(changesize,10)