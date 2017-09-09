(function() {
  // taken from https://stackoverflow.com/questions/133925/javascript-post-request-like-a-form-submit
  function post(path, params, method) {
    method = method || "post";
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);
    for(var key in params) {
        if(params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);

            form.appendChild(hiddenField);
         }
    }
    document.body.appendChild(form);
    form.submit();
  }

  function main() {
    // initialize the drawing app
    drawing = new window.app.Drawing();

    // Removed clear button because post request clears form
    // $('#clear').click(function() {
    //     drawing.reset()
    // })

    drawing.onChange = function() {
      map = drawing.mnistIntensities()
      map = JSON.stringify(map);
      post('/', {img: map});
    }
  }


  window.addEventListener('load', main);
})()
