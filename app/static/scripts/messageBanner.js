bannerActive = false;

// types: 1 -> Successful (Green), 2 -> Warning (Yellow), 3 -> Error (Red)
bannerColors = {
  1: 'rgb(43 172 79)',
  2: '#FAC854',
  3: 'rgb(204 25 13)'
};

async function alertBanner(msg, type) {
  // check if banner is already shown
  if (bannerActive) {
    await hideBanner()
  }

  // show banner
  $('#banner-content').html(msg);
  $('.banner-wrapper').css('background-color', bannerColors[type]);
  $('.banner-wrapper').addClass('show');
  bannerActive = true;

  // hide banner after 7 seconds
  setTimeout(() => {
    hideBanner();
  }, 5000);
}

async function hideBanner() {
  // hide banner
  $('.banner-wrapper').removeClass('show');
  bannerActive = false;
  return;
}