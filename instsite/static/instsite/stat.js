var log_button = document.getElementsByClassName("login_button")[0];
var nav_ul = document.getElementById("nav_ul");
var ham=document.getElementById("ham");
function nav_ul_check() {
	if (window.innerWidth <= 1080) {
		nav_ul.style.display = "none";
		log_button.style.display = "none";
		ham.style.display="flex";
		return true;
	}
	else {
		nav_ul.style.display = "flex";
		log_button.style.display = "flex";
		ham.style.display="none";
		return false;
	}
}
window.addEventListener("resize", nav_ul_check);
nav_ul_check();