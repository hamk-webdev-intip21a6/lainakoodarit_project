const readMoreButton = document.querySelector("button#readmore");
const description = document.querySelector("p#description");

// check if desciption is fully visible
function countLines() {
  const lines = description.getClientRects().length;
  description.classList.remove("inline");
  return lines;
}

readMoreButton.addEventListener("click", (event) => {
  description.classList.toggle("inline");
});

if (countLines() <= 3) {
  readMoreButton.classList.add("hidden");
  document.querySelector("hr#description_line").classList.add("hidden");
}
