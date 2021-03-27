AOS.init({
  easing: 'ease',
  duration: 1800,
  once: true
})

const links = document.querySelectorAll("nav a, .landing-page a");

for (const link of links) {
  link.addEventListener("click", clickHandler);
}

function clickHandler(e) {
  e.preventDefault();
  const href = this.getAttribute("href");
  const offsetTop = document.querySelector(href).offsetTop;

  scroll({
    top: offsetTop,
    behavior: "smooth"
  });
}