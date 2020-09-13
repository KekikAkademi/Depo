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
$site = 'http://www.chip.com.tr/haber/'; // Site Adresi
$site = curl_cek($site); // Site'nin Kaynak Kodları Gelsin

// parametreler sırasıyla; kod başlangıcı, kod bitişi ($site sabit)
$link = ara('<div class="col-clistinfo"><a href="/haber/','.html"  target="_blank">',$site);
$baslik = ara('.html"  target="_blank"><h3>','</h3>',$site);
$icerik = ara('<span class="clistaciklama">','</span>',$site);

?>