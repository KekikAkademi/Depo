<?php
if($_POST) {
$anahtar_kelime = $_POST["anahtar_kelime"];
echo 'Keyword <b>'.$anahtar_kelime.'</b>';
/* Site İsmi */
$site = "http://www.seopuan.com/tr/www/$anahtar_kelime";
$parcala = '@<strong>(.*?)</strong>@si'; /* strong kodu arasındaki bilgileri çek */
/* (.*?) Dinamik */
$cek = file_get_contents($site);
preg_match_all($parcala, $cek, $cikti);

echo '<pre>';
print_r($cikti);
echo '</pre>';

    echo '<b>'.print_r($cikti[0][0]).'</b>'; /* Array 0'ın 0'ını çek yaz */

} 
else { }
?>