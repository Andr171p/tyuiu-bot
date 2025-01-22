document.addEventListener('DOMContentLoaded', () => {
    async function loadData(url, callback) {
        const response = await fetch(url);
        const data = await response.json();
        callback(data.data);
    }

    function formatDates(data) {
        const dates = [];
        const counts = [];
        for (const key in data) {
            dates.push(key);
            counts.push(data[key]);
        }
        return { dates, counts };
    }

    function renderUserGrowthChart(data) {
        const { dates, counts } = formatDates(data);
        new Chart(document.getElementById('userGrowthChart'), {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Рост пользователей',
                    data: counts,
                    fill: false,
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    function renderMessageCountChart(data) {
        const { dates, counts } = formatDates(data);
        new Chart(document.getElementById('messageCountChart'), {
            type: 'bar',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Количество сообщений',
                    data: counts,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    function calculateSubscriberRatio(usersCount, subscribersCount) {
        if (usersCount > 0) {
            return Math.round((subscribersCount / usersCount) * 100);
        } else {
            return 0;
        }
    }

    function renderSubscriberRatioChart(usersCount, subscribersCount) {
        const ratio = calculateSubscriberRatio(usersCount, subscribersCount);
        new Chart(document.getElementById('subscriberRatioChart'), {
            type: 'pie',
            data: {
                labels: ['Подписчики', 'Пользователи'],
                datasets: [{
                    data: [ratio, 100 - ratio],
                    backgroundColor: ['#36A2C3', '#FF6384']
                }],
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });
    }

    async function updateCharts() {
        const usersPromise = fetch('/api/v1/statistics/getUsersCount/');
        const subscribersPromise = fetch('/api/v1/statistics/getSubscribersCount/');

        const [usersResponse, subscribersResponse] = await Promise.all([usersPromise, subscribersPromise]);

        const usersData = await usersResponse.json();
        const subscribersData = await subscribersResponse.json();

        const usersCount = usersData.count;
        const subscribersCount = subscribersData.count;

        renderUserGrowthChart(usersCount);
        renderMessageCountChart(subscribersCount);
        renderSubscriberRatioChart(usersCount, subscribersCount);
    }

    updateCharts();
});