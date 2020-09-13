<?php
/* ------------------------------------------------------------------------- */
/*																			 */
/*					    	coded by aczumuhayyel				 			 */
/*		    		 aczumuhayyel [at] gmail [nokta] com					 */
/*				         kodlarla fazla oynaşmayın           				 */
/*																			 */
/* ------------------------------------------------------------------------- */

$acz = $_GET["acz"];

if($acz == ""){}
	else{

		$site2 = 'http://www.chip.com.tr/haber/'.$acz.'.html'; // Site Adresi
		$site2 = curl_cek($site2); // Site'nin Kaynak Kodları Gelsin
		
		$makalebaslik = ara('<h1 itemprop="headline">','</h1>',$site2);
		$makaleaciklama = ara('<p class="article-desc" itemprop="description">','</p>',$site2);
		$makaleresim = ara('<meta itemprop="url" content="','">',$site2);
		$makaleicerik = ara('<p>','</p><div>',$site2);
	
	}

	
	// ha burda dene daha sonra index'de "sonuclar" div'i içerisinde değişim yap (array değeri)
/*
echo '<pre>';
print_r($makalebaslik);
print_r($makaleaciklama);
print_r($makaleresim);
print_r($makaleicerik);
echo '</pre>';
*/
	
?>