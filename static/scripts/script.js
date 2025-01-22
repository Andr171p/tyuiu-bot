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

    document.getElementById('users-count').innerText = usersData['data']['count'];
    document.getElementById('subscribers-count').innerText = subscribersData['data']['count'];
}

window.onload = async function () {
    await updateStatisticalData();
    setInterval(async function () {
        await updateStatisticalData();
    }, 30000);
}