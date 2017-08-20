function uploadImage() {
  // anything to preprocess before image uploads
  $('form').submit()
}

function setup() {
  if ($('#preview img').length > 0) {
    $('.submit').text('Check another?')
  }
}

window.onload = setup
