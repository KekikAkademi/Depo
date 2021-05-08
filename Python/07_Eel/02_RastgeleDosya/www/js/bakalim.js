async function js_dosya_sec() {
    let dizin = document.getElementById('input-kutusu').value;
    let dosya_div = document.getElementById('dosya-adi');
    
    // python ile dosya sistemine erişelim
    let rastgele_dosya = await eel.py_dosya_sec(dizin)();
    dosya_div.innerHTML = rastgele_dosya;
}