<?php
include("acz-curl.php");

/*
acz bot
*/
$site = 'http://www.gencprogramci.net/'; // Site Adresi
$site = curl_cek($site); // Site'nin Kaynak Kodları Gelsin

// parametreler sırasıyla; kod başlangıcı, kod bitişi ($site sabit)
$baslik = ara('<span class="madde-im">✚</span>','</a>',$site);

?>