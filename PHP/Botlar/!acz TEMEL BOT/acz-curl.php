<?php
/*
!!! OYNAŞMA !!!
acz-Bot Curl Kodları
*/

function curl_cek($acz){
	$useragent = 'YahooSeeker-Testing/v3.9 (compatible; Mozilla 4.0; MSIE 5.5; Yahoo! Search - Web Search)';
	$referer = 'http://www.google.com';
	$ch = curl_init();
	curl_setopt ($ch, CURLOPT_URL, $acz);
	curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt ($ch, CURLOPT_REFERER, $referer);
	curl_setopt ($ch, CURLOPT_FOLLOWLOCATION, 1);
	curl_setopt ($ch, CURLOPT_USERAGENT, $useragent);
	$rmx = curl_exec($ch);
	curl_close($ch);
	return $rmx;
}

function ara($bas, $son, $icerik){
	@preg_match_all('/' . preg_quote($bas, '/') .
    '(.*?)'. preg_quote($son, '/').'/i', $icerik, $m);
    return @$m[1];
}

?>