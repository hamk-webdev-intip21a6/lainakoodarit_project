const alertBox = document.querySelector("section.alert");
const cancelAlertButton = document.querySelector(".alert>div>button");

// await function for adding delay
function delay(ms = 200) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

cancelAlertButton.addEventListener("click", () => {
  removeAlertButton();
});

// show the alert box right when DOM is loaded
// if the view got the required GET requests
fadeAndMove();

async function removeAlertButton() {
  fadeAndMove();
  await delay(500);
  // remove from visible/interactable DOM
  alertBox.classList.add("hidden");
}

function fadeAndMove() {
  // looks like the alert box moves up and fades away
  alertBox.classList.toggle("-translate-y-6");
  alertBox.classList.toggle("opacity-0");
}
