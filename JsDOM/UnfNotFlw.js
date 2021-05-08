/*
------------------------------------
ixakblt - ibrahim AKBULUT
------------------------------------
Web Site :ixakblt
------------------------------------
All Sites : @ixakblt
------------------------------------
*/
var kontrol = 0
setInterval(function () {
    setTimeout(function () {
        var anadiv = document.getElementsByClassName("css-1dbjc4n r-1ila09b r-qklmqi r-1adg3ll");
        for (var i = 0; i <= anadiv.length; i++) {
            var tik1 = document.getElementsByClassName('css-18t94o4 css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1w2pmg r-1vsu8ta r-aj3cln r-1ny4l3l r-1fneopy r-o7ynqc r-6416eg r-lrvibr');
            var tik2 = document.getElementsByClassName('css-18t94o4 css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-16y2uox r-1w2pmg r-1vuscfd r-1dhvaqw r-1ny4l3l r-1fneopy r-o7ynqc r-6416eg r-lrvibr');
            var kont = anadiv[i].getElementsByClassName("css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")[3].innerText
            if (kont == "Takip ediliyor") {
                tik1[0].click();
                tik2[0].click();
                kontrol++
                document.getElementsByClassName("css-4rbku5 css-901oao css-bfa6kz r-jwli3a r-1qd0xha r-1b6yd1w r-1vr29t4 r-ad9z0x r-bcqeeo r-qvutc0")[0].innerText = kontrol
                anadiv[0].remove();
            } else {
                anadiv[0].remove();
            }
        }
    }, 700);
    window.scrollTo(0, 570);
}, 3500);