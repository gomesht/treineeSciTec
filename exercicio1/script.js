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