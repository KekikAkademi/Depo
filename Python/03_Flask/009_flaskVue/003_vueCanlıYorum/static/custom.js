Vue.component("yorum", {
  props: ["yorum"],
  template: `
        <div class="row comment"> 
            <div class="col-md-2">
                <img src="https://cdn1.bbcode0.com/uploads/2020/6/4/9fffd963bdebe615daae66c45a90907a-full.png" class="img-responsive" width="90" height="90">
            </div>
            <div class="col-md-10 comment-text text-left" v-html="yorum.yorum">             </div>
            <span style="margin-left: 15px;" v-html='yorum.kAdi'>       </span>
        </div>
    `,
});

var app = new Vue({
  el: "#app",
  delimiters: ["[[", "]]"],
  data: {
    yorumlar: [],
    mutlu: 0,
    uzgun: 0,
    notr: 0,
    kAdi: null,
    yorum: null,
  },
  methods: {
    updateSentiments() {
      // Ruh halini 0 olarak başlat
      let [mutlu, notr, uzgun] = [0, 0, 0];

      // tüm yorumlarda döngü, sonra her ruh halinin toplamını alın
      for (yorum of this.yorumlar) {
        if (yorum.sentiment > 0.4) {
          mutlu++;
        } else if (yorum.sentiment < 0) {
          uzgun++;
        } else {
          notr++;
        }
      }

      const total_comments = this.yorumlar.length;

      // Her ruh halinin yüzdesini alın
      this.uzgun = ((uzgun / total_comments) * 100).toFixed();
      this.mutlu = ((mutlu / total_comments) * 100).toFixed();
      this.notr = ((notr / total_comments) * 100).toFixed();

      // Ruh hali değerlerinin bir nesnesini döndürme
      return { mutlu, notr, uzgun };
    },

    yorumEkle() {
      fetch("/yorum_ekle", {
        method: "post",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id: this.yorumlar.length,
          kAdi: this.kAdi,
          yorum: this.yorum,
        }),
      })
        .then((response) => response.json())
        .then((veri) => {
          // yorumlar verisine yeni yorumu ekle
          this.yorumlar.push({
            id: veri.id,
            kAdi: veri.kAdi,
            yorum: veri.yorum,
            sentiment: veri.sentiment,
          });

          // Duygu puanını güncelle
          this.updateSentiments();
        });
    },
  },
});