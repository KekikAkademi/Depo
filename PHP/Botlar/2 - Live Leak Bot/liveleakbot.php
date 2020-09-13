<?php
function bot($link){
	$gelen = file_get_contents($link);
	
		preg_match('#<title>LiveLeak.com - (.*?)</title>#si', $gelen, $baslik);
		$veri ["baslik"] = $baslik[1];
		preg_match('#<meta property="og:description" content="(.*?)"#si', $gelen, $aciklama);
		$veri ["aciklama"] = $aciklama[1];
		preg_match('#file: "(.*?)"#si', $gelen, $video);
		$veri ["video"] = $video[1];
	return $veri;
}

print_r (bot ("http://www.liveleak.com/view?i=a85_1457127517"));

?>