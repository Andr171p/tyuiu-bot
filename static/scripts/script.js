// static/scripts/script.js
function toggleRecipientInput() {
    const recipientSelect = document.getElementById('recipient');
    const phoneInput = document.getElementById('phone-input');

    if (recipientSelect.value === 'phone') {
        phoneInput.style.display = 'block';
    } else {
        phoneInput.style.display = 'none';
    }
}


async function updateStatisticalData() {
    const usersResponse = await fetch('/api/v1/statistics/getUsersCount/')
    const usersData = await usersResponse.json();

    const subscribersResponse = await fetch('/api/v1/statistics/getSubscribersCount/')
    const subscribersData = await subscribersResponse.json();

    document.getElementById('users-count').innerText = usersData.count;
    document.getElementById('subscribers-count').innerText = subscribersData.count;
}

window.onload = async function () {
    await updateStatisticalData();
    setInterval(async function () {
        await updateStatisticalData();
    }, 30000);
}

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

    async function updateCharts() {
        const usersPromise = fetch('/api/v1/statistics/getUserCountPerDay/');
        const messagesPromise = fetch('/api/v1/statistics/getMessagesCountPerDay/');

        const [usersResponse, messagesResponse] = await Promise.all([usersPromise, messagesPromise]);

        const usersData = await usersResponse.json();
        const messagesData = await messagesResponse.json();

        const usersPerDayCount = usersData.data;
        const messagesPerDayCount = messagesData.data;

        renderUserGrowthChart(usersPerDayCount);
        renderMessageCountChart(messagesPerDayCount);
    }

    updateCharts();
});