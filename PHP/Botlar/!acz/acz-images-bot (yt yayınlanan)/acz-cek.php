<?php 
if($_POST) { //Eğer POST girdisi varsa kodları çalıştırmaya başla
$anahtar_kelime = $_POST["anahtar_kelime"];
echo '<center><h1>Keyword: <u>"'.$anahtar_kelime.'"</u></h1></center><p>';


// Curl
function ara($bas, $son, $icerik){
	@preg_match_all('/' . preg_quote($bas, '/') .
    '(.*?)'. preg_quote($son, '/').'/i', $icerik, $m);
    return @$m[1];
}
// #Curl


$site = "https://yandex.com/images/search?text=$anahtar_kelime"; // Site Adresi
$icerik = file_get_contents($site); // Site'nin Kaynak Kodları Gelsin



// Ha Bunları Çek İşte :)
$resim_bilgisi = ara('snippet":{"title":"','","hasTitle',$icerik);
$resim_linki = ara(',"img_href":"','","useProxy"',$icerik);

} else {} //POST girdisi yoksa dur
?>