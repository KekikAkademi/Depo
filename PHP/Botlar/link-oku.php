<?php
function getLinks($link)
{
	/*** return array ***/
	$ret = array();
	/*** a new dom object ***/
	$dom = new domDocument;
	/*** get the HTML (sumress errors) ***/
	@$dom->loadHTML(file_get_contents($link));
	/*** remove silly white space ***/
	$dom->preserveWhiteSpace = false;
	/*** get the links from the HTML ***/
	$links = $dom->getElementsByTagName('a');
	/*** loop over the links ***/
	foreach ($links as $tag)
	{
		$ret[$tag->getAttribute('href')] = $tag->childNodes->item(0)->nodeValue;
	}
	return $ret;
}

$link='http://filmakinesi.org/'; /* Link */

$urls = getLinks($link);
if(sizeof($urls) > 0)
{
	foreach($urls as $key=>$value)
	{
	if(!strstr($key,"category") and strstr($key,"izle.html")){ /* "category" geçiyorsa alma "izle.html" geçiyorsa al */
		echo $key."<br>";
	}
	}
}	
?>