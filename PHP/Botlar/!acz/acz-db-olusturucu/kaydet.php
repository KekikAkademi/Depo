<?php
/* ------------------------------------------------------------------------- */
/*																			 */
/*					    	coded by aczumuhayyel				 			 */
/*		    		 aczumuhayyel [at] gmail [nokta] com					 */
/*				         kodlarla fazla oynaşmayın           				 */
/*																			 */
/* ------------------------------------------------------------------------- */


$dosya_adi = "acz.xml";
$dosya = fopen ($dosya_adi , 'w') or die ("Dosya
açılamadı!");
$metin = $_POST["db-icerik"];
fwrite($dosya,$metin ) ;
fclose ($dosya);

?>