<?php
	$xtitle = 'ATLAS v1.0';

	$netAccess = '<script></script>';

	$xweb = file_get_contents('status.txt');

	if ( $xweb == 1 ) {

		$xConnect = '<font id="webNoteOn" class="webNote" title="You are Connected to the Internet!">(( LIVE ))</font>';
		$netAccess = '<script type="text/javascript">document.addEventListener("click", openURL);</script>';
		
	} else {

		$xConnect = '<font id="webNoteOff" class="webNote" title="You are Not Connected to the Internet..">(( LIVE ))</font>';
		$netAccess = '<script type="text/javascript"></script>';
	}
?>
<html>
<head>
<title>
<?php echo $xtitle; ?>
</title>
<link type="text/css" rel="stylesheet" href="css/main.css">
<script type="text/javascript" src="js/index.js"></script>
</head>
<body>

<?php echo $netAccess; ?>

<img id="htmlButton" class="devTool" src="img/html.png">
<img id="jsButton" class="devTool" src="img/js.png">
<img id="cssButton" class="devTool" src="img/css.png">

<?php echo $xConnect; ?>

<font id="facebookLink" title="Share ATLAS on Facebook..">facebook</font>

<img id="signature">

</body>
</html>
