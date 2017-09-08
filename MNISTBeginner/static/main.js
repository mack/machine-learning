(function() {
  function main() {
    // initialize the drawing app
    drawing = new window.app.Drawing();
  
    $('#clear').click(function() {
        drawing.reset()
    })
  }

  window.addEventListener('load', main);

})()
