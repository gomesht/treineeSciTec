const divClique = document.querySelector('.clique');
const divHide = document.querySelector('.hide');
divClique.addEventListener('click', () => {
  if (divClique.style.backgroundColor === 'blueviolet') { 
    divClique.style.backgroundColor = 'blue';
    divClique.style.width = "200px";
    divClique.style.height = "200px";
    divHide.style.display = 'flex';
  } else {
    divClique.style.backgroundColor = 'blueviolet';
    divClique.style.width = "100px";
    divClique.style.height = "100px";
       divHide.style.display = 'none';
  }
})