(function() {
  function main() {
    // initialize the drawing app
    drawing = new window.app.Drawing();

    $('#clear').click(function() {
        drawing.reset()
    })

    drawing.onChange = function() {
      map = drawing.mnistIntensities()
        
    }
  }


  window.addEventListener('load', main);
})()
