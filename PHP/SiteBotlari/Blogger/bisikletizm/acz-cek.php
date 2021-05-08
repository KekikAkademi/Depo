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
$site = 'http://www.bisikletizm.com/'; // Site Adresi
$site = curl_cek($site); // Site'nin Kaynak Kodları Gelsin

// parametreler sırasıyla; kod başlangıcı, kod bitişi ($site sabit)
$link = ara('<h2 class="entry-title"><a href="http://www.bisikletizm.com/','/" rel="bookmark">',$site);
$baslik = ara(' rel="bookmark">','</a>',$site);
$icerik = ara('<img width="450" height="450" src="','" class',$site);

?>