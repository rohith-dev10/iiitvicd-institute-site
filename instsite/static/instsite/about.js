var lastScrollTop = 0;
var st = 0
var ham=document.getElementById("ham");
var log_button = document.getElementsByClassName("login_button")[0];
var nav_ul = document.getElementById("nav_ul");
function nav_ul_check() {
	if (window.innerWidth <= 1080) {
		nav_ul.style.display = "none";
		log_button.style.display = "none";
		ham.style.display="flex";
		return true;
	}
	else {
		ham.style.display="none";
		nav_ul.style.display = "flex";
		log_button.style.display = "flex";
		return false;
	}
}
window.addEventListener("resize", nav_ul_check);
nav_ul_check();

window.addEventListener("scroll", function(){
    var st = window.pageYOffset ;
    if(st<lastScrollTop) {
        navbar.style.display="flex";
        // upscroll code
    }
    else{
        navbar.style.display="none";
    }
    lastScrollTop = st <= 0 ? 0 : st;
}, false);