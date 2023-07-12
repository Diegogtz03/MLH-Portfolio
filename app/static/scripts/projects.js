function openModal(id) {
  document.getElementsByClassName('opaque-body')[0].classList.add('opaque-body-shown');
  document.getElementsByTagName('body')[0].style.overflow = 'hidden';
  document.getElementsByClassName('projects-wrapper')[0].style.pointerEvents = 'none';
  document.getElementById('modal-' + id).classList.add('open');
}

function closeModal(id) {
  document.getElementById('modal-' + id).classList.add('close');
  document.getElementsByClassName('opaque-body')[0].classList.remove('opaque-body-shown');
  document.getElementsByClassName('projects-wrapper')[0].style.pointerEvents = 'all';
  document.getElementsByTagName('body')[0].style.overflow = 'scroll';

  setTimeout(function() {
    document.getElementById('modal-' + id).classList.remove('open');
    document.getElementById('modal-' + id).classList.remove('close');
  }, 600);
}