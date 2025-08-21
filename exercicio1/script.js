document.querySelectorAll('nav a').forEach(link => {
  link.addEventListener('click', function(e) {
    e.preventDefault();
    const target = this.getAttribute('data-target');
    document.querySelectorAll('#home, #sobre, #contato').forEach(sec => {
      sec.style.display = 'none';
    });
    document.getElementById(target).style.display = 'flex';
 
  });
});

document.querySelectorAll('[id^="ep"]').forEach(ep => {
  ep.addEventListener('click', function() {
    const detalhes = this.parentElement.querySelector('.detalhes');
    const isOpen = detalhes.style.display === 'flex';


    document.querySelectorAll('[id^="ep"]').forEach(div => {
      div.classList.remove('ep-aberto');
    });
   
    document.querySelectorAll('.detalhes').forEach(div => {
      div.style.display = 'none';
    });

    if (!isOpen) {
      detalhes.style.display = 'flex';
      this.classList.add('ep-aberto');
    }
  });
});