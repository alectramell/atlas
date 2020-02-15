function reLoad(xvar) {

	setTimeout(function(){location.reload();}, xvar);
}

addEventListener('load', reLoad(30000));


