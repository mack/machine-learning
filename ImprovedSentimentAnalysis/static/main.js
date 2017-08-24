
function setup() {
  console.log('test')
  $('#submit').click(function() {
    $('form').submit()
  })
}

window.onload = setup
