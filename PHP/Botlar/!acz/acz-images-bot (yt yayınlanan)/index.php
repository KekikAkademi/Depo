<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="tr">
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
	<title>acz-images-bot</title>
	<link rel="stylesheet" href="css/style.css" type="text/css" />
	<script type="text/javascript" src="ajax/eyceks.js"></script>
	<script type="text/javascript">
		function calistir(site){
			JXP(1, 'sonuclar', 'acz-yaz.php', 'site='+site);
		}
	</script>
</head>
<body>
<!-- acz-bot -->

<table border="1" bordercolor="#990000" >
	<tr>
		<!-- Çekme Alanı -->
		<td align="left" valign="top">
		<form action="" method="post">
		<center>
			<input type="text" name="anahtar_kelime" placeholder="Keyword"> <br>
			<button type="submit" onclick="calistir()">ÇEK</button>
		</center>
		</form>
		</td>
		<!-- #Çekme Alanı -->
		
		<!-- Listeleme Alanı -->
		<td valign="top" align="left" width="80%">
		<div id="sonuclar" align="left">
		<form name="db-yaz" method="post">
		<?php require "acz-cek.php"; ?>
		<?php require "db-bilgi.php"; ?>
		</form>
		</div>
		</td>
		<!-- #Listeleme Alanı -->	
	</tr>
	
	<!-- Blog Post -->
	<tr>
		<td colspan="2" valign="top" align="center">
		<div id="sonuclar" align="left">
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
	<!-- #Blog Post -->
	
</table>
<!--#acz-bot -->

</body>
</html>