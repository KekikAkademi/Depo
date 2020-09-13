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
for($i=0; $i < 14; $i++){
	echo '
	<div class="dokum">
	<h2><a href="?acz='.$link[$i].'"/>'.$baslik[$i].'</h2>
	<img width="50" height="50" src="'.$icerik[$i].'"></a>
	</div>';
}

?>