const slider = document.querySelector(".carousel");
let isDown = false;
let startX;
let scrollLeft;

slider.addEventListener("mousedown", (event) => {
  isDown = true;
  slider.classList.add("mouse-hold");
  startX = event.pageX - slider.offsetLeft;
  scrollLeft = slider.scrollLeft;
});
slider.addEventListener("mouseleave", (_) => {
  isDown = false;
  slider.classList.remove("mouse-hold");
});
slider.addEventListener("mouseup", (_) => {
  isDown = false;
  slider.classList.remove("mouse-hold");
});
slider.addEventListener("mousemove", (event) => {
  if (!isDown) return;
  event.preventDefault();
  const x = event.pageX - slider.offsetLeft;
  const scrollSpeed = 1;
  const walk = (x - startX) * scrollSpeed;
  slider.scrollLeft = scrollLeft - walk;
});
