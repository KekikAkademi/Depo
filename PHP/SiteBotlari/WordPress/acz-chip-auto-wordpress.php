<?php
include('wp-config.php');
//--------------------------------------------------------------------------------------------------------------------
/* Curl'e Dokunma */
function curl_cek($aczumuhayyel){
	$useragent = 'YahooSeeker-Testing/v3.9 (compatible; Mozilla 4.0; MSIE 5.5; Yahoo! Search - Web Search)';
	$referer = 'http://www.google.com';
	$ch = curl_init();
	curl_setopt ($ch, CURLOPT_URL, $aczumuhayyel);
	curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt ($ch, CURLOPT_REFERER, $referer);
	curl_setopt ($ch, CURLOPT_FOLLOWLOCATION, 1);
	curl_setopt ($ch, CURLOPT_USERAGENT, $useragent);
	$rmx = curl_exec($ch);
	curl_close($ch);
	return $rmx;
}

function ara($bas, $son, $icerik){
	@preg_match_all('/' . preg_quote($bas, '/') .
    '(.*?)'. preg_quote($son, '/').'/i', $icerik, $m);
    return @$m[1];
}

//--------------------------------------------------------------------------------------------------------------------
/* Tek Tek Haberleri Çek */
$site = 'http://www.chip.com.tr/haber/'; // Site Adresi
$site = curl_cek($site); // Site'nin Kaynak Kodları Gelsin

	// parametreler sırasıyla; kod başlangıcı, kod bitişi ($site sabit)
	$link = ara('<div class="col-clistinfo"><a href="/haber/','.html"  target="_blank">',$site);
	$baslik = ara('.html"  target="_blank"><h3>','</h3>',$site);
	$icerik = ara('<span class="clistaciklama">','</span>',$site);


//--------------------------------------------------------------------------------------------------------------------
/* Haber İçeriği Çek */
for($i=0; $i <count($baslik); $i++){

		$site2 = 'http://www.chip.com.tr/haber/'.$link[$i].'.html'; // Site Adresi
		$site2 = curl_cek($site2); // Site'nin Kaynak Kodları Gelsin
		
		$makalebaslik = ara('<h1 itemprop="headline">','</h1>',$site2);
		$makaleaciklama = ara('<p class="article-desc" itemprop="description">','</p>',$site2);
		$makaleresim = ara('<meta itemprop="url" content="','">',$site2);
		$makaleicerik = ara('<p>','</p><div>',$site2);
		$keyword = ara('<dd>','</dd>',$site2);



		// Keyword Çekerken "</a>" kodunu alma
		for($p=0; $p <count($keyword); $p++){
			$keyword[$p] = strip_tags($keyword[$p],"</a>");
		}
		$keywords = '<b>Etiketler :</b>'.$keyword[0].', '.$keyword[1].', '.$keyword[2];

//--------------------------------------------------------------------------------------------------------------------
/* Haber İçeriği Yayınla */
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

echo 'acz - Hamısını Çektim ☺';
?>
<title>acz - Oto Wordpress Bot</title>