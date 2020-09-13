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

		$site2 = 'http://blogesinti.com/'.$acz.'/'; // Site Adresi
		$site2 = curl_cek($site2); // Site'nin Kaynak Kodları Gelsin
		
		$makalebaslik = ara('<h2 class="title">','</h2>',$site2);
		$makaleicerik = ara('<p style="text-align: justify;">','</p>',$site2);
	
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