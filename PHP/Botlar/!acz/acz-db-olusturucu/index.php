<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="tr-TR">
<?php include("db-olustur.php"); ?>
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
	<title>acz-db-olusturucu</title>
	<link rel="stylesheet" type="text/css" media="all" href="css/style.css" />
	<meta name="viewport" content="width=device-width" />
	<script type="text/javascript" src="ajax/acz.js"></script>
	<script type="text/javascript">
		function calistir(site){
			JXP(1, 'db-yaz', 'db.php', 'site='+site);
		}
	</script>
</head>
<body>
<!-- acz design -->

<div class="header">
	<div id="acz">
		<div class="logo"><a href=""><h1>acz-db-olusturucu</a></h1></div>
		<div class="ara">
	<!--		<form action="" method="post">
			<input type="text" name="anahtar_kelime" placeholder="Keyword">
			<button type="submit" onclick="calistir()">ÇEK</button>
			</form> -->
		</div>
	</div>
</div><!--header-->


<div id="acz">
	<div class="anasayfa shadow">
		<div class="icerik">
			<form action="" method="post">
			<input type="text" name="icerikbaslik1" placeholder="İçerik 1 Başlık"><input type="text" name="icerik1" placeholder="İçerik 1"><br>
			<input type="text" name="icerikbaslik2" placeholder="İçerik 2 Başlık"><input type="text" name="icerik2" placeholder="İçerik 2"><br>
			<input type="text" name="icerikbaslik3" placeholder="İçerik 3 Başlık"><input type="text" name="icerik3" placeholder="İçerik 3"><br>
			<input type="text" name="icerikbaslik4" placeholder="İçerik 4 Başlık"><input type="text" name="icerik4" placeholder="İçerik 4"><br>
			<input type="text" name="icerikbaslik5" placeholder="İçerik 5 Başlık"><input type="text" name="icerik5" placeholder="İçerik 5"><br>
			<input type="text" name="icerikbaslik6" placeholder="İçerik 6 Başlık"><input type="text" name="icerik6" placeholder="İçerik 6"><br>
			<input type="text" name="icerikbaslik7" placeholder="İçerik 7 Başlık"><input type="text" name="icerik7" placeholder="İçerik 7"><br>
			<input type="text" name="icerikbaslik8" placeholder="İçerik 8 Başlık"><input type="text" name="icerik8" placeholder="İçerik 8"><br>
			<input type="text" name="icerikbaslik9" placeholder="İçerik 9 Başlık"><input type="text" name="icerik9" placeholder="İçerik 9"><br>
			<input type="text" name="icerikbaslik10" placeholder="İçerik 10 Başlık"><input type="text" name="icerik10" placeholder="İçerik 10"><br>
			<input type="text" name="tarih" placeholder="Tarih (2016-02-27)"><br>
			<button type="submit" onclick="calistir()">DB OLUŞTUR</button>
			</form>
		</div><div class="clr"></div>
	</div><!--icerik-->
	
	<div class="gonder shadow">
		<div class="db-yaz">
			<form action="kaydet.php" method="post">
			<div class="blogger-yaz">
			<table>
				<tr><td><b>DB</b></td></tr>
				<tr>
					<td><textarea name="db-icerik" id="db-icerik" style="height:200px;"><?php include("db.php"); ?></textarea></td>
				</tr>
			</table>
				<button name="db-yaz" value="db-yaz">DB OLUŞTUR</button>
			</div>
			</form>
		</div>
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