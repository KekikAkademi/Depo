var uyg = new Vue({
    el: "#uygulama",
    data: {
      mesaj: "Merhaba Vue!",
      link: "https://google.com.tr",
      duzYazi: "lorem impsum sit amet",
      detaylar: "<b>Bu bir yazı detayıdır..</b>",
      yapilacaklar: [
        { is: "JavaScript Öğren" },
        { is: "Vue Öğren" },
        { is: "Harika Bişey Yap" },
        { is: "yeni veri için; uyg.yapilacaklar.push({ is: 'yeni iş' })"}
      ],
    },
    delimiters: ['^*', '*^']
  });