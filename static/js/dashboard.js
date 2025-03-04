document.addEventListener("DOMContentLoaded", function () {
  const tempCtx = document.getElementById('temperatureChart').getContext('2d');
  const humidityCtx = document.getElementById('humidityChart').getContext('2d');

  const labels = ["0:00 AM", "1:00 AM", "2:00 AM", "3:00 AM", "4:00 AM", "5:00 AM", "6:00 AM", "7:00 AM", "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 AM"];

  // Dummy Data
  const temperatureData = [22, 24, 21, 26, 23, 25, 27, 30, 45];
  const humidityData = [60, 55, 70, 65, 80, 75, 85];

  // Temperature Chart
  new Chart(tempCtx, {
      type: 'line',
      data: {
          labels: labels,
          datasets: [{
              label: 'Temperature (°C)',
              data: temperatureData,
              borderColor: '#e74c3c',
              backgroundColor: 'rgba(231, 76, 60, 0.2)',
              borderWidth: 2,
              fill: true
          }]
      },
      options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
              y: {
                  beginAtZero: false
              }
          }
      }
  });

  // Humidity Chart
  new Chart(humidityCtx, {
      type: 'bar',
      data: {
          labels: labels,
          datasets: [{
              label: 'Humidity (g/kg)',
              data: humidityData,
              backgroundColor: '#3498db',
              borderWidth: 1
          }]
      },
      options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
              y: {
                  beginAtZero: true,
                  max: 100
              }
          }
      }
  });
});
