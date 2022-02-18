// check
console.log("hello word");

function opennavbar(){
    document.getElementById("navbar").style.display="block";
    document.getElementById("main").style.marginRight = "200px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.5)";
}

function closenavbar(){
    document.getElementById("navbar").style.display="none";
    document.getElementById("main").style.marginRight = "0";
    document.body.style.backgroundColor = "white";

}
