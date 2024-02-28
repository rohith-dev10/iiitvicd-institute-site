var sticky = 60;
var st = 0
var ham=document.getElementById("ham");
var ham1=document.getElementById("ham1");
var navbar = document.getElementById("navbar");
var nav_img = document.getElementById("nav-img");
var log_button = document.getElementsByClassName("login_button")[0];
var nav_ul = document.getElementById("nav_ul");
function nav_ul_check() {
	if (window.innerWidth <= 1080) {
		if (st) { nav_ul.style.display = "none"; }
		if (st > sticky) {log_button.style.display = "none";ham.style.display="flex";}
		return true;
	}
	else {
		ham.style.display="none";
		if (st) { nav_ul.style.display = "flex"; }
		log_button.style.display = "flex";
		return false;
	}
}
window.addEventListener("resize", nav_ul_check);
nav_ul_check();

var lastScrollTop = 0;
window.addEventListener("scroll", function () {
	st = window.pageYOffset;

	if (st > sticky) {
		navbar.style.display = "none";
		nav_img.setAttribute("src", "/static/instsite/IIITV-ICD_Logo_nobg_no111.png")
		nav_img.classList.replace("nav_img", "new_nav_img");
		navbar.classList.add("new_nav");
		log_button.style.fontSize = "24px";
		if (!nav_ul_check()){
			nav_ul.style.display = "flex";
		}
	}
	else if (st == 0) {
		nav_img.setAttribute("src", "/static/instsite/IIITV-ICD_Logo_nobg.png")
		navbar.classList.remove("new_nav");
		nav_img.classList.replace("new_nav_img", "nav_img");
		log_button.style.fontSize = "30px";
		log_button.style.display = "flex";
		nav_ul.style.display = "none";
		ham.style.display="none";
	}
	if (st < lastScrollTop) {
		navbar.style.display = "flex";
	}
	lastScrollTop = st <= 0 ? 0 : st;
}, false);

ham.addEventListener("click",()=>{
	ham.style.display="none";
	ham1.style.display="flex";
})
ham1.addEventListener("click",()=>{
	ham1.style.display="none";
	ham.style.display="flex";
})