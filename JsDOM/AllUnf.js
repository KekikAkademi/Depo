/*
------------------------------------
ixakblt - ibrahim AKBULUT
------------------------------------
Web Site :ixakblt
------------------------------------
All Sites : @ixakblt
------------------------------------
*/
setInterval(function(){
        var anadiv = document.getElementsByClassName('css-1dbjc4n r-1ila09b r-qklmqi r-1adg3ll')
        var inputs = document.getElementsByClassName('css-18t94o4 css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1w2pmg r-1vsu8ta r-aj3cln r-1ny4l3l r-1fneopy r-o7ynqc r-6416eg r-lrvibr');
        var bira = document.getElementsByClassName('css-18t94o4 css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-16y2uox r-1w2pmg r-1vuscfd r-1dhvaqw r-1ny4l3l r-1fneopy r-o7ynqc r-6416eg r-lrvibr')
        for(var i=0; i<=inputs.length;i--) {
        inputs[i].click();
        bira[i].click();
        anadiv[i].remove();
        }
    },100);
