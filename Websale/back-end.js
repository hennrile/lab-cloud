let btn = document.querySelector(".mainBtn");
let mbtn = document.querySelector(".minusBtn");
let pbtn = document.querySelector(".plusBtn");

btn.addEventListener("click", ()=>{
    if(btn.innerText == "ADD TO CART") {
        btn.innerText = 1;
        pbtn.style.display = "inline-block";
        mbtn.style.display = "inline-block";
    }
});
mbtn.addEventListener("click", ()=>{
    if(btn.innerText == 5){
        pbtn.style.visibility = "hidden";
    }
    if(btn.innerText < 2) {
        btn.innerText = "ADD TO CART";
        pbtn.style.visibility = "visible";
        pbtn.style.display = "none";
        mbtn.style.display = "none";
    }
    else{
        btn.innerText = btn.innerText - 1;
    }
});
pbtn.addEventListener("click", ()=>{
    btn.innerText = +btn.innerText + +1;
    if(btn.innerText == 5){
        pbtn.style.visibility = "hidden";
    }
});
