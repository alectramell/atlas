function reLoad(xvar) {

	setTimeout(function(){location.reload();}, xvar);
}

function openURL() {

	htmlOPT = document.getElementById('htmlButton');
	cssOPT = document.getElementById('cssButton');
	jsOPT = document.getElementById('jsButton');
	fbOPT = document.getElementById('facebookLink');

	htmlOPT.addEventListener('click', function(){window.open('https://en.wikipedia.org/wiki/html5');location.reload();});
	cssOPT.addEventListener('click', function(){window.open('https://en.wikipedia.org/wiki/Cascading_Style_Sheets');location.reload();});
	jsOPT.addEventListener('click', function(){window.open('https://en.wikipedia.org/wiki/Javascript');location.reload();});
	fbOPT.addEventListener('click', function(){window.open('https://www.facebook.com/sharer/sharer.php?u=https://github.com/alectramell/atlas');location.reload();});
}


