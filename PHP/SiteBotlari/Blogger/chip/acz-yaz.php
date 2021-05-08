<?php
/* ------------------------------------------------------------------------- */
/*																			 */
/*					    	coded by aczumuhayyel				 			 */
/*		    		 aczumuhayyel [at] gmail [nokta] com					 */
/*				         kodlarla fazla oynaşmayın           				 */
/*																			 */
/* ------------------------------------------------------------------------- */
include ("acz-cek.php");


// ha burda dene
/*
echo '<pre>';
print_r($baslik);
print_r($link);
print_r($icerik);
echo '</pre>';
*/


//ha burda dök
for($i=0; $i < 10; $i++){ //0-29 Gideri var!
	echo '
	<div class="dokum">
	<h2><a href="?acz='.$link[$i].'"/>'.$baslik[$i].'</a></h2>
	<b>'.$icerik[$i].'</b>
	</div>';
}

?>