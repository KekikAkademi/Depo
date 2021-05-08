<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="tr-TR">
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
	<title>acz taslak</title>
	<link rel="stylesheet" type="text/css" media="all" href="css/style.css" />
	<meta name="viewport" content="width=device-width" />
	<script type="text/javascript" src="ajax/acz.js"></script>
	<script type="text/javascript">
		function calistir(site){
			JXP(1, 'sonuclar', 'acz-yaz.php', 'site='+site);
		}
	</script>
</head>
<body>
<!-- acz design -->

<div class="header">
	<div id="acz">
		<div class="logo"><a href=""><h1>acz taslak</a></h1></div>
		<div class="ara">
	<!--		<form action="" method="post">
			<input type="text" name="anahtar_kelime" placeholder="Keyword"> -->
			<button type="submit" onclick="calistir()">ÇEK</button>
	<!--		</form> -->
		</div>
	</div>
</div><!--header-->


<div id="acz">
	<div class="anasayfa shadow">
		<div class="icerik">
		
			<b>Burası Botun listeleme yapacagı alan<br><br></b><div id="sonuclar" align="left"></div> <!-- Sonuçlar -->
			
		</div><div class="clr"></div>
	</div><!--icerik-->
	
	<div class="gonder shadow">

	Ekleme yaparken kullanacağımız alan<!-- Ekleme -->
	
	</div><!--gonder-->
</div><!--acz-->

<div class="footer">
	<div id="acz">
	© aczumuhayyel Her Hakkı Saklıdır.
	</div>
</div>

<!-- #acz design -->
</body>
</html>