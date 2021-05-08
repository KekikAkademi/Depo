/*
------------------------------------
ixakblt - ibrahim AKBULUT
------------------------------------
Web Site :ixakblt
------------------------------------
All Sites : @ixakblt
------------------------------------
*/

setInterval(function () {
  var in2 = document.getElementsByClassName('css-1dbjc4n r-1777fci');
  var inputs = document.getElementsByClassName('css-901oao r-1awozwy r-nw8l94 r-6koalj r-1qd0xha r-a023e6 r-16dba41 r-1h0z5md r-ad9z0x r-bcqeeo r-o7ynqc r-clp7b1 r-3s2u2q r-qvutc0');
  for (var i = 0; i <= inputs.length; i--) {
    inputs[i].click();
    in2[i].click();
  }
}, 2000);
setInterval(function () {
  window.scrollTo(0, document.body.scrollHeight);
}, 5000);