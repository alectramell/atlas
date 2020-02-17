function reLoad(xvar) {

	setTimeout(function(){location.reload();}, xvar);
}

function openURL() {

	htmlOPT = document.getElementById('htmlButton');
	cssOPT = document.getElementById('cssButton');
	jsOPT = document.getElementById('jsButton');

	htmlOPT.addEventListener('click', function(){window.open('https://en.wikipedia.org/wiki/html5')});
	cssOPT.addEventListener('click', function(){window.open('https://en.wikipedia.org/wiki/Cascading_Style_Sheets')});
	jsOPT.addEventListener('click', function(){window.open('https://en.wikipedia.org/wiki/Javascript')});
}

addEventListener('load', reLoad(300000));


