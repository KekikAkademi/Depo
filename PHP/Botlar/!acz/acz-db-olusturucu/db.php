<?php
/* ------------------------------------------------------------------------- */
/*																			 */
/*					    	coded by aczumuhayyel				 			 */
/*		    		 aczumuhayyel [at] gmail [nokta] com					 */
/*				         kodlarla fazla oynaşmayın           				 */
/*																			 */
/* ------------------------------------------------------------------------- */


echo '<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet href="http://www.blogger.com/styles/atom.css" type="text/css"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:openSearch="http://a9.com/-/spec/opensearchrss/1.0/" xmlns:blogger="http://schemas.google.com/blogger/2008" xmlns:georss="http://www.georss.org/georss" xmlns:gd="http://schemas.google.com/g/2005" xmlns:thr="http://purl.org/syndication/thread/1.0">
<id>tag:blogger.com,1999:blog-2762370030649176926</id>
<updated>'.$tarih.'T21:03:23.618-08:00</updated>
<category term="acz-bot"/>
<title type="text">aczumuhayyel</title>
<subtitle type="html"></subtitle>
<link rel="http://schemas.google.com/g/2005#feed" type="application/atom+xml" href="http://zinciriminpimi.com/feeds/posts/default"/>
<link rel="self" type="application/atom+xml" href="http://www.blogger.com/feeds/2762370030649176926/posts/default"/>
<link rel="alternate" type="text/html" href="http://zinciriminpimi.com/"/>
<link rel="hub" href="http://pubsubhubbub.appspot.com/"/>
<author>
<name>aczumuhayyel</name><email>aczumuhayyel@gmail.com</email>
<gd:image rel="http://schemas.google.com/g/2005#thumbnail" width="32" height="32" src="//lh6.googleusercontent.com/-Cpoje669pgQ/AAAAAAAAAAI/AAAAAAAABCw/IaHHMrEp6M4/s512-c/photo.jpg"/>
</author>
<generator version="7.00" uri="http://www.blogger.com">Blogger</generator>
<openSearch:totalResults>1</openSearch:totalResults>
<openSearch:startIndex>1</openSearch:startIndex>
<openSearch:itemsPerPage>25</openSearch:itemsPerPage>';

include('db-yaz.php');

echo '</feed>';

?>