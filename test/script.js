function tick(bool){
if(bool){
    document.getElementsByClassName("yes")[0].style.color="lightgreen";
    document.getElementsByClassName("no")[0].style.color="aqua";
}
else{
    document.getElementsByClassName("yes")[0].style.color="aqua";
    document.getElementsByClassName("no")[0].style.color="red";
}
}