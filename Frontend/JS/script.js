// JavaScript to handle file input and display CSV content

let jsonArray = [];

function convertCSVtoJSON(inputId, tableId, storeButtonIds) {
  const fileInput = document.getElementById(inputId);
  const tableResult = document.getElementById(tableId);

  const file = fileInput.files[0];
  if (!file) {
    alert("Please select a CSV file.");
    return;
  }

  const reader = new FileReader();
  reader.onload = function (event) {
    const csvData = event.target.result;
    const lines = csvData.split("\n");
    const headers = lines[0].split(",");
    jsonArray = [];

    for (let i = 1; i < lines.length; i++) {
      const currentLine = lines[i].split(",");
      if (currentLine.length !== headers.length) {
        alert("CSV file is not properly formatted.");
        return;
      }

      const jsonObject = {};
      for (let j = 0; j < headers.length; j++) {
        jsonObject[headers[j]] = currentLine[j];
      }
      jsonArray.push(jsonObject);
    }

    const jsonString = JSON.stringify(jsonArray, null, 2);

    // Display JSON data as a table
    const table = document.createElement("table");
    const headerRow = table.insertRow(0);

    for (const header of headers) {
      const cell = headerRow.insertCell(-1);
      cell.textContent = header;
    }

    for (let i = 0; i < jsonArray.length; i++) {
      const row = table.insertRow(-1);
      for (const header of headers) {
        const cell = row.insertCell(-1);
        cell.textContent = jsonArray[i][header];
      }
    }

    tableResult.innerHTML = "";
    tableResult.appendChild(table);
    storeButtonIds.forEach(buttonId => {
      const storeButton = document.getElementById(buttonId);
      if (storeButton) {
        storeButton.style.display = "block";
      } else {
        console.error("Button with ID '" + buttonId + "' not found.");
      }
    });
  };

  reader.readAsText(file);
}


function displayDataInTable(data, tableId) {
  const tableDiv = document.getElementById(tableId);
  let table = '<table>';
  data.forEach((row) => {
    table += `<tr>${Object.values(row).map((value) => `<td>${value}</td>`).join('')}</tr>`;
  });
  table += '</table>';
  tableDiv.innerHTML = table;
}
