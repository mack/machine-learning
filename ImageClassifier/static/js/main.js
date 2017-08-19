function loadImage(){
    var file = document.querySelector('input[type=file]').files[0]
    var reader = new FileReader()

    if (file) {
      console.log(file)
      reader.readAsDataURL(file)
    }

    reader.onloadend = function () {
        src = reader.result; // send this input with post request then return it
        $('.submit').text("Try another?")
        $('form').submit()
    }
}
