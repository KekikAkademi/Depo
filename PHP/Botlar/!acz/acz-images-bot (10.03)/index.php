<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="tr-TR">
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
	<title>acz-images-bot</title>
	<link rel="stylesheet" type="text/css" media="all" href="css/style.css" />
	<meta name="viewport" content="width=device-width" />
	<script type="text/javascript" src="ajax/acz.js"></script>
	<script type="text/javascript">
		function calistir(site){
			JXP(1, 'blogger-yaz', 'acz-yaz.php', 'site='+site);
			JXP(1, 'db-bilgi', 'acz-yaz.php', 'site='+site);
		}
	</script>
</head>
<body>
<!-- acz design -->

<div class="header">
	<div id="acz">
		<div class="logo"><h1><a href="">acz-images-bot</a></h1></div>
		<div class="ara">
			<form action="" method="post">
			<input type="text" name="anahtar_kelime" placeholder="Keyword">
			<button type="submit" onclick="calistir()">ÇEK</button>
			</form>
		</div>
	</div>
</div><!--header-->


<div id="acz">
	<div class="anasayfa shadow">
		<div class="icerik">
			<div id="db-bilgi" align="left">
			<?php require "acz-cek.php"; ?>
			<?php require "db-bilgi.php"; ?>
			</div>
		</div><div class="clr"></div>
	</div><!--icerik-->
	
	<div class="gonder shadow">
	<tr>
		<td colspan="2" valign="top" align="center">
		<div id="blogger-yaz" align="left">
		<form action="https://www.blogger.com/blog-this.g" method="get">
			<div class="blogger-yaz" style="display:">
			<table>
			<tr><td><b>Başlık</b></td></tr>
				<tr>
					<td><input class="inp1" type="text" name="n" value="<?php echo $resim_bilgisi[0].' | '.$anahtar_kelime; ?>"></td>
				</tr>
				<tr><td><b>İçerik</b> <i>(15 Başlık Ve Resim)</i></td></tr>
				<tr>
					<td><textarea name="b" class="inp2" style="height:200px;"><?php require"blogger-yaz.php"; ?></textarea></td>
				</tr>
			</table>
					<input class="submit" type="submit" name="gonder" value="Veri Tabanına Kaydet" style="height:50px; width:97%; padding:10px; background:#eee; border:1px solid #ddd; margin:10px; cursor:pointer;" />		
			</div>
			</form>
		</div>
		</td>
	</tr>
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