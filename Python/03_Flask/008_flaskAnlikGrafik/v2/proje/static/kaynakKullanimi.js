$(document).ready(function() {
    const config = {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: "RAM Kullanımı",
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: [],
                fill: false,
            }],
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'Flask ile Gerçek Zamanlı Grafikler Oluşturma'
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Zaman'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Değer'
                    }
                }]
            }
        }
    };

    const context = document.getElementById('keyiflerolsun').getContext('2d');

    const cizgiGrafik = new Chart(context, config);

    const kaynak = new EventSource("/grafik-verileri");

    kaynak.onmessage = function(olay) {
        const veri = JSON.parse(olay.data);
        console.log(veri)
        if (config.data.labels.length === 7) {
            config.data.labels.shift();
            config.data.datasets[0].data.shift();
        } // Maksimum 7 Adet
        config.data.labels.push(veri['Zaman']);
        config.data.datasets[0].data.push(veri['kullanilan']);
        cizgiGrafik.update();
    }
});