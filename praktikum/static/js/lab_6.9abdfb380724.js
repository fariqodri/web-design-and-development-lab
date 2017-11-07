// Calculator
var sender = true;
$('textarea').keypress(function(e){
    if(e.keyCode == 13 && !e.shiftKey) {
        var c = String.fromCharCode(e.which);
        var textValue = $('textarea').val();
        var fulltext = textValue + c;
        $('textarea').val('');
    
        if(sender){
            $('.msg-insert').append('<p class="msg-send">' + fulltext + '</p>');
            sender = false;
        }else{
            $('.msg-insert').append('<p class="msg-receive">' + fulltext + '</p>');
            sender = true;
        }

        e.preventDefault();
    };
});

$('.chat-head').click(function(){
    $('.chat-body').toggle();
})

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
  } else if (x == '0') {
	  if(print.value != '') {
		  print.value += x;
	  }
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
    {"id":1,"text":"Pink","bcgColor":"#E91E63","fontColor":"#FAFAFA"},
    {"id":2,"text":"Purple","bcgColor":"#9C27B0","fontColor":"#FAFAFA"},
    {"id":3,"text":"Indigo","bcgColor":"#3F51B5","fontColor":"#FAFAFA"},
    {"id":4,"text":"Blue","bcgColor":"#2196F3","fontColor":"#212121"},
    {"id":5,"text":"Teal","bcgColor":"#009688","fontColor":"#212121"},
    {"id":6,"text":"Lime","bcgColor":"#CDDC39","fontColor":"#212121"},
    {"id":7,"text":"Yellow","bcgColor":"#FFEB3B","fontColor":"#212121"},
    {"id":8,"text":"Amber","bcgColor":"#FFC107","fontColor":"#212121"},
    {"id":9,"text":"Orange","bcgColor":"#FF5722","fontColor":"#212121"},
    {"id":10,"text":"Brown","bcgColor":"#795548","fontColor":"#FAFAFA"}
];

var selectedTheme =  {"id":3,"text":"Indigo","bcgColor":"#3F51B5","fontColor":"#FAFAFA"};

themeObj = JSON.parse(JSON.stringify(themes));

localStorage.setItem("themes", JSON.stringify(themes));
object = localStorage.getItem("themes");
var colors = JSON.parse(object);

$.each(colors, function(index){
	var id = colors[index].id;
	var text = colors[index].text;
	var bcgColor = colors[index].bcgColor;
	var fontColor = colors[index].fontColor;
	localStorage.setItem(id, text.concat("," + bcgColor + "," + fontColor));
});

$(document).ready(function(){
	$('.my-select').select2({
		data : themes
	});
	
	if(localStorage.getItem("selectedItem") == null){
        localStorage.setItem("selectedItem",3);
        var themeDefault = localStorage.getItem(localStorage.getItem("selectedItem"));
        var applyDefault = themeDefault.split(",");
        
        document.body.style.backgroundColor = applyDefault[1];
        document.getElementById('texthead').style.color = applyDefault[2];
    }else{
        var themeSaved = localStorage.getItem(localStorage.getItem("selectedItem"));
        var applySaved = themeSaved.split(",");
        
        document.body.style.backgroundColor = applySaved[1];
        document.getElementById('texthead').style.color = applySaved[1];
    }
	
	$(".apply-button").on("click", function(){
		var picked = localStorage.getItem($('.my-select').val());
		var apply = picked.split(",");
		document.body.style.backgroundColor = apply[1];
		document.getElementById(texthead).style.color(apply[2]);
		localStorage.setItem("selectedTheme", $('.my-select').val());
		return false;
	});
});


