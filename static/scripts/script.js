// Функция переключения видимости поля для ввода номера телефона
function toggleRecipientInput() {
    const recipientSelect = document.getElementById('recipient');
    const phoneInput = document.getElementById('phone-input');

    if (recipientSelect.value === 'phone') {
        phoneInput.style.display = 'block';
    } else {
        phoneInput.style.display = 'none';
    }
}

// Функция для обновления статистики
async function updateStatisticalData() {
    try {
        const usersResponse = await fetch('/api/v1/statistics/getUsersCount/');
        const usersData = await usersResponse.json();

        const subscribersResponse = await fetch('/api/v1/statistics/getSubscribersCount/');
        const subscribersData = await subscribersResponse.json();

        document.getElementById('users-count').innerText = usersData.count;
        document.getElementById('subscribers-count').innerText = subscribersData.count;
    } catch (error) {
        console.error('Ошибка при обновлении статистики:', error);
    }
}

// Функция загрузки данных для графиков
async function loadData(url, callback) {
    try {
        const response = await fetch(url);
        const data = await response.json();
        callback(data.data);
    } catch (error) {
        console.error(`Ошибка загрузки данных с ${url}:`, error);
    }
}

// Форматирование данных для графиков
function formatDates(responseData) {
    const data = responseData.data; // Извлекаем объект "data"
    const dates = [];
    const counts = [];
    for (const key in data) {
        dates.push(key);
        counts.push(data[key]);
    }
    return { dates, counts };
}

// Функция для отрисовки графика роста пользователей
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

// Функция для отрисовки графика количества сообщений
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

// Функция обновления графиков
async function updateCharts() {
    try {
        const usersPromise = fetch('/api/v1/statistics/getUserCountPerDay/');
        const messagesPromise = fetch('/api/v1/statistics/getMessagesCountPerDay/');

        const [usersResponse, messagesResponse] = await Promise.all([usersPromise, messagesPromise]);

        const usersData = await usersResponse.json();
        const messagesData = await messagesResponse.json();

        const usersPerDayCount = formatDates(usersData);
        const messagesPerDayCount = formatDates(messagesData);

        renderUserGrowthChart(usersPerDayCount);
        renderMessageCountChart(messagesPerDayCount);
    } catch (error) {
        console.error('Ошибка при обновлении графиков:', error);
    }
}

// Обработчик отправки сообщений
document.querySelector('.message-form').addEventListener('submit', async (e) => {
    e.preventDefault(); // Останавливает перезагрузку страницы

    const recipientType = document.getElementById('recipient').value;
    const phone = document.getElementById('phone').value;
    const message = document.getElementById('message').value;

    let url;
    let payload;

    if (recipientType === 'all') {
        url = '/api/v1/notification/sendAll/';
        payload = { message };
    } else if (recipientType === 'phone') {
        if (!phone) {
            alert('Пожалуйста, укажите номер телефона!');
            return;
        }
        url = '/api/v1/notification/sendByPhoneNumber/';
        payload = { phone, message };
    } else {
        alert('Выбран неверный тип получателя!');
        return;
    }

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload),
        });

        if (response.ok) {
            alert('Сообщение успешно отправлено!');
        } else {
            const errorData = await response.json();
            alert(`Ошибка: ${errorData.error || 'Не удалось отправить сообщение'}`);
        }
    } catch (error) {
        console.error('Ошибка при отправке сообщения:', error);
        alert('Произошла ошибка при отправке сообщения.');
    }
});

// Инициализация страницы
window.onload = async function () {
    await updateStatisticalData(); // Обновление статистики
    setInterval(async function () {
        await updateStatisticalData(); // Автоматическое обновление статистики каждые 30 секунд
    }, 30000);

    await updateCharts(); // Обновление графиков
};
