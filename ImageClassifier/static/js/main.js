function loadImage(){
    var file = document.querySelector('input[type=file]').files[0]
    var reader = new FileReader()

    if (file) {
      console.log(file)
      reader.readAsDataURL(file)
    }

    reader.onloadend = function () {
        src = reader.result;
        $('.submit').text("Try another?")
        $('form').submit()
    }
}
