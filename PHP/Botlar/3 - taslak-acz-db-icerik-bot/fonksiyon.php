<?php
if($_POST) {
$anahtar_kelime = $_POST["anahtar_kelime"];
echo '<center><h1>Keyword: <u>"'.$anahtar_kelime.'"</u></h1></center><p>';

function getir($baslangic, $son, $cekilmek_istenen)
{
    @preg_match_all('/' . preg_quote($baslangic, '/') .
    '(.*?)'. preg_quote($son, '/').'/i', $cekilmek_istenen, $m);
    return @$m[1];
}

$url = "https://yandex.com.tr/gorsel/search?text=$anahtar_kelime";

$icerik = file_get_contents($url);

$resim_bilgisi = getir('snippet":{"title":"','","hasTitle',$icerik);
$resim_linki = getir(',"img_href":"','","useProxy"',$icerik);

echo "<b>Resim Bilgisi :</b> " . $resim_bilgisi[0] . "<br />";
echo "<b>Resim Linki :</b> " . $resim_linki[0];
echo "<p>";

} 
else { }
?>