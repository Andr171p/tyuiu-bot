document.addEventListener('DOMContentLoaded', () => {
    const userGrowthCtx = document.getElementById('userGrowthChart').getContext('2d');
    const messageCountCtx = document.getElementById('messageCountChart').getContext('2d');

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
        new Chart(userGrowthCtx, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Новые пользователи',
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
        new Chart(messageCountCtx, {
            type: 'bar',
            data: {
                labels: dates,
                datasets: [{
                    label: 'Количество сообщений за каждый день',
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

    loadData('/api/v1/statistics/getUserCountPerDay/', renderUserGrowthChart);
    loadData('/api/v1/statistics/getMessagesCountPerDay/', renderMessageCountChart);
});


document.addEventListener('DOMContentLoaded', () => {
    async function fetchAndDisplayData(endpoint, elementId) {
        try {
            const response = await fetch(`/api/v1/statistics/${endpoint}`);
            const data = await response.json();

            if (data.status === 'ok') {
                document.getElementById(elementId).innerText = data.count;
            } else {
                console.error(`Ошибка при получении данных: ${data.message}`);
            }
        } catch (error) {
            console.error(`Ошибка при выполнении запроса: ${error}`);
        }
    }

    fetchAndDisplayData('getUsersCount/', 'usersCount');
    fetchAndDisplayData('getSubscribersCount/', 'subscribersCount');
});