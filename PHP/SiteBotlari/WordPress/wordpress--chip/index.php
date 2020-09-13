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
	
	<?php
	
	include('../wp-config.php');
	if($_GET["acz"]){
		
		// Yazı nesnesi oluştur
		$my_post = array(
		  'post_title'    => $makalebaslik[0],
		  'post_content'  => '<h1>'.$makaleaciklama[0].'</h1><br><img src="'.$makaleresim[1].'" ><br>'.$makaleicerik[0],
		  'post_status'   => 'publish',
		  'post_author'   => 1,
		);

		// Yazıyı veritabanına ekle
		$id = wp_insert_post( $my_post );
		add_post_meta($id, 'keywords', $keywords);
	}
	
	?>
	
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