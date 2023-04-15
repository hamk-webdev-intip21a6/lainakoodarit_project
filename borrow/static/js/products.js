const readMoreButton = document.querySelector("button#readmore");
const description = document.querySelector("div#description");

// check if desciption is fully visible
function countLines() {
  // const lines = description.getClientRects().length;
  // description.classList.remove("inline");
  // console.log(lines);
  const lineHeight = parseInt(
    window
      .getComputedStyle(description.firstElementChild)
      .getPropertyValue("line-height")
  );
  const height = description.offsetHeight;
  const numLines = Math.ceil(height / lineHeight);
  console.log(`Number of lines: ${numLines}`);
  return numLines;
}

readMoreButton.addEventListener("click", (event) => {
  description.classList.toggle("line-clamp-3");
});

if (countLines() <= 3) {
  readMoreButton.classList.add("hidden");
  document.querySelector("hr#description_line").classList.add("hidden");
} else {
  description.classList.toggle("line-clamp-3");
}
