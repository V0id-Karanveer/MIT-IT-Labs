var regex = /[1-4]{1}[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{3}/
function validate(){
    var usn = document.getElementById("usn").value;
    var res = regex.test(usn);
    if(!res){
        alert("error in usn");
    }
    else{
        alert("your usn is "+usn);
    }
}