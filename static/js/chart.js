// ChatGPT helped with logic for chart.js

document.addEventListener("DOMContentLoaded", function() {

    const labels = JSON.parse(document.getElementById("labels-data").textContent);
    const counts = JSON.parse(document.getElementById("counts-data").textContent);


    const data = {
    labels: labels,
    datasets: [{
        label: 'Total logs',
        data: counts,
        backgroundColor: [
        '#31c500',
        '#6366f1',
        '#3b82f6',
        '#ec4899'
        ],
        hoverOffset: 4
    }]
    };

    const config = {
    type: 'doughnut',
    data: data,
    options: {
        responsive: true,
        maintainAspectRatio: true
    }
    };


    const ctx = document.getElementById('myChart');
    new Chart(ctx, config);
});