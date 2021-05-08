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
    var inputs = document.getElementsByClassName('js-icon-favorite icon icon-favorite icon-favorite-toggle txt-center pull-left');
    for (var i = 0; i <= inputs.length; i--) {
        inputs[i].click();
    }
}, 2000);