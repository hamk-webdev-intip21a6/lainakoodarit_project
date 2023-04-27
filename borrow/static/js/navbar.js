const navList = document.querySelector("nav>ul");
const navButton = document.querySelector("nav>button");
const navButtonIcon = navButton.querySelector("img");
let isNavOpen = true;
const navButtonIcons = {
  open: "/static/icons/navbutton-open.svg",
  close: "/static/icons/navbutton-close.svg",
};

// await function for adding delay
function delay(ms = 200) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

navButton.addEventListener("click", (event) => {
  // toggle navigation bar button's state
  isNavOpen = !isNavOpen;
  console.log(isNavOpen);
  console.log(navButtonIcon.src);
  // change the navbutton's icon based on the isNavOpen variable
  navButtonIcon.src = navButtonIcons[isNavOpen ? "open" : "close"];
  // navList.classList.toggle("hidden");
  toggleNavigation();
});

async function toggleNavigation() {
  if (!isNavOpen) {
    navList.classList.toggle("hidden");
    await delay();
    navList.classList.toggle("opacity-0");
    return;
  }
  navList.classList.toggle("opacity-0");
  await delay();
  navList.classList.toggle("hidden");
}
