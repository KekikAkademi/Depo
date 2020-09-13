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

		$site2 = 'http://www.bisikletizm.com/'.$acz.'/'; // Site Adresi
		$site2 = curl_cek($site2); // Site'nin Kaynak Kodları Gelsin
		
		$makalebaslik = ara("data-title='","' data-link='",$site2);
		$makaleicerik = ara('<p style="text-align: justify;">','</p>',$site2);
	
	}

	
	// ha burda dene daha sonra index'de "sonuclar" div'i içerisinde değişim yap (array değeri)
/*
echo '<pre>';
print_r($makalebaslik);
print_r($makaleicerik);
echo '</pre>';
*/
	
?>