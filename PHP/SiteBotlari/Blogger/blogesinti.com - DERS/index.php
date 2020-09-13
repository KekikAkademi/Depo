<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="tr-TR">
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
	<title>acz - Chip Botu</title>
	<link rel="stylesheet" type="text/css" media="all" href="css/style.css" />
	<meta name="viewport" content="width=device-width" />
	<script type="text/javascript" src="ajax/acz.js"></script>
	<script type="text/javascript">
		function calistir(site){
			JXP(1, 'sonuclar', 'acz-gonder.php', 'site='+site);
		}
	</script>
</head>
<body>
<!-- acz design -->

<div class="header">
	<div id="acz">
		<div class="logo"><a href=""><h1>acz - Chip Botu</a></h1></div>
		<div class="menu">
		<ul>
			<li><a href="http://www.zinciriminpimi.com">Zincirimin Pimi</a></li>
		</ul>
		</div>
	</div>
</div><!--header-->


<div id="acz">
	<div class="anasayfa shadow">
		<div class="icerik">
		
			<?php include('acz-yaz.php'); ?> 	<!-- Çekilen Konular Dökümü -->
		
		</div><div class="clr"></div>
	</div><!--icerik-->
	
	<div class="gonder shadow">
	
	<?php include('acz-gonder.php'); ?> 	<!-- Konu içeriği çekimi -->
	
	<div class="sonuclar">
	
	<tr>
		<td colspan="2" valign="top" align="center">
		<div id="blogger-yaz" align="left">
		<form action="https://www.blogger.com/blog-this.g" method="get">
			<div class="blogger-yaz" style="display:">
			<table>
			<tr><td><b>Başlık</b></td></tr>
				<tr>
					<td><input class="inp1" type="text" name="n" value="<?php if($_GET) { echo $makalebaslik[0]; } else { echo 'Seçim Yapın...'; }?>"></td>
				</tr>
				<tr><td><b>İçerik</b></td></tr>
				<tr>
					<td>
					
					<textarea name="b" class="inp2" style="height:200px;"><?php if($_GET) { echo '<h1>'.$makaleicerik[0].'</h1><p>'.$makaleicerik[2].'<p><p>'.$makaleicerik[1].'<p>'.$makaleicerik[4].'<p>'.$makaleicerik[3];} else { echo 'Seçim Yapın...'; }?></textarea>
					
					</td>
				</tr>
			</table>
					<input class="submit" type="submit" name="gonder" value="Veri Tabanına Kaydet" style="height:50px; width:97%; padding:10px; background:#eee; border:1px solid #ddd; margin:10px; cursor:pointer;" />		
			</div>
			</form>
		</div>
		</td>
	</tr>
	
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