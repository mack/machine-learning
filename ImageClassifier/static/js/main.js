function loadImage(){
    var file = document.querySelector('input[type=file]').files[0];
    var reader = new FileReader();

    if (file) {
        reader.readAsDataURL(file); //reads the data as a URL
    }

    reader.onloadend = function () {
        src = reader.result;
        $('#preview').append("<img src=" + src + ">")
        $('img').css({
          "vertical-align" : "top",
          "display" : "block",
          "max-width" : "300%",
          "max-height" : "100%",
          "position" : "absolute",
          "top" : "0",
          "bottom" : "0",
          "left" : "0",
          "right" : "0"
        })
        $('.submit').text("Try another?")
    }
}
