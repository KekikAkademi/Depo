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
$site = 'http://blogesinti.com/'; // Site Adresi
$site = curl_cek($site); // Site'nin Kaynak Kodları Gelsin

	// parametreler sırasıyla; kod başlangıcı, kod bitişi ($site sabit)
	$link = ara('<span class="detay_tarih"><a href="http://blogesinti.com/','/" title="',$site);
	$baslik = ara('title="Permalink to ','">',$site);
	$icerik = ara('<img width="200" height="150" src="','" class="alignleft tfe wp-post-image"',$site);
	

//--------------------------------------------------------------------------------------------------------------------
/* Haber İçeriği Çek */
for($i=0; $i <count($baslik); $i++){

		$site2 = 'http://blogesinti.com/'.$link[$i].'/'; // Site Adresi
		$site2 = curl_cek($site2); // Site'nin Kaynak Kodları Gelsin
		
		$makalebaslik = ara('<h2 class="title">','</h2>',$site2);
		$makaleicerik = ara('<p style="text-align: justify;">','</p>',$site2);

//--------------------------------------------------------------------------------------------------------------------
/* Haber İçeriği Yayınla */
		// Yazı nesnesi oluştur
		$my_post = array(
		  'post_title'    => $makalebaslik[0],
		  'post_content'  => '<h1>'.$makaleicerik[0].'</h1><p>'.$makaleicerik[2].'<p><p>'.$makaleicerik[1].'<p>'.$makaleicerik[4].'<p>'.$makaleicerik[3],
		  'post_status'   => 'publish',
		  'post_author'   => 1,
		);

		// Yazıyı veritabanına ekle
		$id = wp_insert_post( $my_post );
}

echo 'acz - Hamısını Çektim ☺';
?>
<title>acz - Oto Wordpress Bot</title>