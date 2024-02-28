var navbar = document.getElementById("navbar");
var nav_ul = document.getElementById("nav_ul");
var nav_img = document.getElementById("nav-img");
var log_button = document.getElementsByClassName("login_button")[0];

var sticky = 60;
var lastScrollTop = 0;
window.addEventListener("scroll", function(){
    var st = window.pageYOffset ;

   if (st > sticky){
      navbar.style.display="none";
      nav_img.setAttribute("src","static/instsite/IIITV-ICD_Logo_nobg_no111.png")
      nav_img.classList.replace("nav_img","new_nav_img");
      navbar.classList.add("new_nav");
      log_button.style.fontSize="24px";
      nav_ul.style.display="flex";
      // change
    }
    else if(st==0){
        nav_img.setAttribute("src","static/instsite/IIITV-ICD_Logo_nobg.png")
        navbar.classList.remove("new_nav");
        nav_img.classList.replace("new_nav_img","nav_img");
        log_button.style.fontSize="30px";
        nav_ul.style.display="none";
        // nav_img.classList.remove()
        // reset
    } 
    if(st<lastScrollTop) {
        navbar.style.display="flex";
      // upscroll code
   }
   lastScrollTop = st <= 0 ? 0 : st;
}, false);


// window.onscroll = function() {myFunction()};

// // Get the navbar
// var navbar = document.getElementById("navbar");

// // Get the offset position of the navbar
// var sticky = navbar.offsetTop;

// // Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
// function myFunction() {
//   if (window.pageYOffset >= sticky) {
//     // navbar.classList.add("sticky") Change class to apply new style
    
//   } else {
//     navbar.classList.remove("sticky");
//   }
// }