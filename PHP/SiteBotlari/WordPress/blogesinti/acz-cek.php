<?php
/* ------------------------------------------------------------------------- */
/*																			 */
/*					    	coded by aczumuhayyel				 			 */
/*		    		 aczumuhayyel [at] gmail [nokta] com					 */
/*				         kodlarla fazla oynaşmayın           				 */
/*																			 */
/* ------------------------------------------------------------------------- */

include("acz-curl.php");

/*
acz bot
*/
$site = 'http://blogesinti.com/'; // Site Adresi
$site = curl_cek($site); // Site'nin Kaynak Kodları Gelsin

// parametreler sırasıyla; kod başlangıcı, kod bitişi ($site sabit)
$link = ara('<span class="detay_tarih"><a href="http://blogesinti.com/','/" title="',$site);
$baslik = ara('title="Permalink to ','">',$site);
$icerik = ara('<img width="200" height="150" src="','" class="alignleft tfe wp-post-image"',$site);

?>