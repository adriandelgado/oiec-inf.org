// Mobile menu
const button = document.getElementById("js-menu-button");
const iconOpen = document.getElementById("js-menu-open");
const iconClosed = document.getElementById("js-menu-closed");
const menu = document.getElementById("js-menu-list");
button.addEventListener("click", () => {
  iconOpen.classList.toggle("block");
  iconOpen.classList.toggle("hidden");
  iconClosed.classList.toggle("block");
  iconClosed.classList.toggle("hidden");
  menu.classList.toggle("hidden");
});

// Desktop Navbar
const btnInformacion = document.getElementById("js-informacion");
const btnAcademico = document.getElementById("js-academico");

let opened = null;

const toggleVisibility = (e) => {
  e.classList.toggle("block");
  e.classList.toggle("hidden");
};

const handleDropdown = (e) => {
  const clickedItem = e.parentElement.lastChild.previousSibling;

  toggleVisibility(clickedItem);

  if (!opened) {
    opened = clickedItem;
  } else if (opened === clickedItem) {
    opened = null;
  } else {
    toggleVisibility(opened);
    opened = clickedItem;
  }
};

const handleClick = (e) => {
  if (btnInformacion.contains(e.target)) {
    handleDropdown(btnInformacion);
  } else if (btnAcademico.contains(e.target)) {
    handleDropdown(btnAcademico);
  } else if (opened) {
    toggleVisibility(opened);
    opened = null;
  }
};

document.addEventListener("click", handleClick);
