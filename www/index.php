<?php
	$xtitle = 'ATLAS v1.0';

	$xweb = file_get_contents('status.txt');

	if ( $xweb == 1 ) {

		$xConnect = '<font id="webNoteOn">(( www ))</font>';

	} else {

		$xConnect = '<font id="webNoteOff">-- www --</font>';
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

<img id="htmlButton" class="devTool" src="img/html.png">
<img id="jsButton" class="devTool" src="img/js.png">
<img id="cssButton" class="devTool" src="img/css.png">

<?php echo $xConnect; ?>

<img id="signature">

</body>
</html>
