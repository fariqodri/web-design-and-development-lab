// Calculator
var print = document.getElementById('print');
var erase = false;

var go = function(x) {
  if (x === 'ac') {
    /* implemetnasi clear all */
    print.value = '';
    erase  = true;
  } else if (x === 'eval') {
      print.value = Math.round(evil(print.value) * 10000) / 10000;
      erase = true;
  } else {
    print.value += x;
  }
};

function evil(fn) {
  return new Function('return ' + fn)();
}
// END
var themes, object, themeObj;
themes = [
    {"id":0,"text":"Red","bcgColor":"#F44336","fontColor":"#FAFAFA"},
    {"id":0,"text":"Pink","bcgColor":"#E91E63","fontColor":"#FAFAFA"},
    {"id":0,"text":"Purple","bcgColor":"#9C27B0","fontColor":"#FAFAFA"},
    {"id":0,"text":"Indigo","bcgColor":"#3F51B5","fontColor":"#FAFAFA"},
    {"id":0,"text":"Blue","bcgColor":"#2196F3","fontColor":"#212121"},
    {"id":0,"text":"Teal","bcgColor":"#009688","fontColor":"#212121"},
    {"id":0,"text":"Lime","bcgColor":"#CDDC39","fontColor":"#212121"},
    {"id":0,"text":"Yellow","bcgColor":"#FFEB3B","fontColor":"#212121"},
    {"id":0,"text":"Amber","bcgColor":"#FFC107","fontColor":"#212121"},
    {"id":0,"text":"Orange","bcgColor":"#FF5722","fontColor":"#212121"},
    {"id":0,"text":"Brown","bcgColor":"#795548","fontColor":"#FAFAFA"}
];

/*localStorage.setItem("themes", JSON.stringify(themes));

object = localStorage.getItem("themes");

$(document).ready(function() {
    $('.my-select').select2();
});

$('.my-select').select2({
    'data': JSON.parse(object);
})

//Retrieve applied theme when browser re-opened
    var applied = JSON.parse(localStorage.getItem("selected"));
    $("body").css({"background-color":applied.themeObj.bcgColor, "color":applied.themeObj.fontColor});


$('.apply-button-class').on('click', function(){  // sesuaikan class button
    // [TODO] ambil value dari elemen select .my-select
    var data = JSON.parse(object);
	var id = $(".my-select").select2("val");

    // [TODO] cocokan ID theme yang dipilih dengan daftar theme yang ada
    $.each(data, function(i, theme) {
		if(id == theme.id) {
			// [TODO] ambil object theme yang dipilih
			themeObj = theme.text;
    
		    // [TODO] aplikasikan perubahan ke seluruh elemen HTML yang perlu diubah warnanya
		    $("body").css({"background-color" : theme.bcgColor, "color" : theme.fontColor});
		    // [TODO] simpan object theme tadi ke local storage selectedTheme
		    var selectedTheme = {themeObj:{"bcgColor":theme.bcgColor, "fontColor" : theme.fontColor}};
			localStorage.setItem("selected", JSON.stringify(selectedTheme));
			return false; //to break loop
		}
	});
});*/