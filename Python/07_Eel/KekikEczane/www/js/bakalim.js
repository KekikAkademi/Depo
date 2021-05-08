function js_eczane() {
    var il = document.getElementById('il').value;
    var ilce = document.getElementById('ilce').value;

    eel.py_eczane(il, ilce)
}

eel.expose(eczaneVer);
function eczaneVer(bilgiler) {
    $('#eczane-ara').hide();
    $('#eczane-buldum').show();
    var mesaj = document.getElementById('eczane-buldum');
    mesaj.innerHTML = bilgiler;
}