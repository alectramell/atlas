function reLoad(xvar) {

	setTimeout(function(){location.reload();}, xvar);
}

function openURL() {

	htmlOPT = document.getElementById('htmlButton');
	cssOPT = document.getElementById('cssButton');
	jsOPT = document.getElementById('jsButton');
	fbOPT = document.getElementById('facebookLink');

	htmlOPT.addEventListener('click', function(){window.open('https://en.wikipedia.org/wiki/html5')});
	cssOPT.addEventListener('click', function(){window.open('https://en.wikipedia.org/wiki/Cascading_Style_Sheets')});
	jsOPT.addEventListener('click', function(){window.open('https://en.wikipedia.org/wiki/Javascript')});
	fbOPT.addEventListener('click', function(){window.open('https://www.facebook.com/sharer/sharer.php?u=https://github.com/alectramell/atlas')});
}

addEventListener('load', reLoad(300000));


