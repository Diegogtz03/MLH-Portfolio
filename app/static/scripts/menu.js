// ON HOVER MENU BUTTON
let buttons = document.getElementsByClassName('menu-button');

Array.from(buttons).forEach((button) => {
  button.addEventListener('mouseover', (e) => {
    // Get span element inside button
    const spanElement = button.getElementsByClassName('hover-label')[0];

    if (!spanElement.classList.contains('visible-label')) {
      // Save text inside span and set text to empty, add class that will make it visible
      let label = spanElement.getAttribute('data-label');
      spanElement.innerHTML = '';
      spanElement.classList.add('visible-label');

      // send it to function that will write the text console like
      writeLabel(spanElement, label);
    }
  });

  button.addEventListener('mouseleave', (e) => {
    const spanElement = button.getElementsByClassName('hover-label')[0];

    if (spanElement.classList.contains('visible-label')) {
      let label = spanElement.innerHTML;
      deleteLabel(spanElement, label);
    }
  });
});


function writeLabel(element, label) {
  // Split label into array of characters
  element.innerHTML = '';
  let labelArray = label.split('');

  // For each character, write it to the span element
  labelArray.forEach((char, index) => {
    setTimeout(() => {
      element.innerHTML += char;
    }, 100 * index);
  });
}

function deleteLabel(element, label) {
  // Split label into array of characters
  let labelArray = label.split('');

  // For each character, write it to the span element
  labelArray.forEach((char, index) => {
    setTimeout(() => {
      label = label.slice(0, -1);
      element.innerHTML = label;
    }, 100 * index);
  });

  // when done remove class
  setTimeout(() => {
    element.classList.remove('visible-label');
    element.innerHTML = '';
  }, 100 * labelArray.length);
}