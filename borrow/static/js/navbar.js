const navList = document.querySelector("nav>ul");
const navButton = document.querySelector("nav>button");
const navButtonIcon = navButton.querySelector("img");
let isNavOpen = true;
const navButtonIcons = {
  open: "/static/icons/navbutton-open.svg",
  close: "/static/icons/navbutton-close.svg",
};

navButton.addEventListener("click", (event) => {
  // toggle navigation bar button's state
  isNavOpen = !isNavOpen;
  console.log(isNavOpen);
  console.log(navButtonIcon.src);
  // change the navbutton's icon based on the isNavOpen variable
  navButtonIcon.src = navButtonIcons[isNavOpen ? "close" : "open"];
  navList.classList.toggle("hidden");
});
