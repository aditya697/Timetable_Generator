async function generateTimetable() {
    fetch('http://localhost:3005/generate-timetable')
      .then(response => response.text())
      .then(html => {
        document.getElementById('timetable-container').innerHTML = html;
      })
      .catch(error => console.error('Error fetching timetable:', error));
    }