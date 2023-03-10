// Dados da primeira reta
let x1 = 0;
let y1 = 6;
let x2 = 4;
let y2 = 0;

// Cálculo da inclinação e do ponto de intercepção
let m1 = (y2 - y1) / (x2 - x1);
let b1 = y1 - m1 * x1;

// Dados da segunda reta
let x3 = 1;
let y3 = 4;
let x4 = 5;
let y4 = 2;

// Cálculo da inclinação e do ponto de intercepção
let m2 = (y4 - y3) / (x4 - x3);
let b2 = y3 - m2 * x3;

// Criação do gráfico
let canvas = document.getElementById("meuGrafico");
let ctx = canvas.getContext("2d");
let data = {
    labels: [],
    datasets: [
        {
            label: "Reta 1",
            data: [],
            borderColor: "rgba(255, 0, 0, 1)",
            fill: false,
        },
        {
            label: "Reta 2",
            data: [],
            borderColor: "rgba(0, 0, 255, 1)",
            fill: false,
        },
    ],
};

// Adição dos pontos da primeira reta ao gráfico
for (let i = x1; i <= x2; i++) {
    let y = m1 * i + b1;
    data.labels.push(i);
    data.datasets[0].data.push(y);
}

// Adição dos pontos da segunda reta ao gráfico
for (let i = x3; i <= x4; i++) {
    let y = m2 * i + b2;
    data.datasets[1].data.push(y);
}

// Criação do gráfico
let chart = new Chart(ctx, {
    type: "line",
    data: data,
    options: {
        scales: {
            xAxes: [
                {
                    display: true,
                },
            ],
            yAxes: [
                {
                    display: true,
                },
            ],
        },
    },
});
