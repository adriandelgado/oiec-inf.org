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

const btnInformacion = document.getElementById("js-informacion");
const menuInfo = document.getElementById("js-menu-informacion");
const toggleInfoMenu = () => {
  menuInfo.classList.toggle("block");
  menuInfo.classList.toggle("hidden");
};
btnInformacion.addEventListener("click", toggleInfoMenu);

const btnAcademico = document.getElementById("js-academico");
const menuAcad = document.getElementById("js-menu-academico");
const toggleAcadMenu = () => {
  menuAcad.classList.toggle("block");
  menuAcad.classList.toggle("hidden");
};
btnAcademico.addEventListener("click", toggleAcadMenu);

document.addEventListener("click", (event) => {
  if (!btnInformacion.contains(event.target)) {
    menuInfo.classList.remove("block");
    menuInfo.classList.add("hidden");
  }
  if (!btnAcademico.contains(event.target)) {
    menuAcad.classList.remove("block");
    menuAcad.classList.add("hidden");
  }
});
