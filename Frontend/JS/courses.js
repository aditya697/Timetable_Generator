// JavaScript to handle file input and display CSV content

async function StoreCoursesData() {
  try {
    const response = await fetch("http://localhost:3005/InsertCoursesData", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(jsonArray),
    });

    if (response.ok) {
      console.log("Data sent to server successfully.");
    } else {
      console.error(
        "Error sending data to server:",
        response.status,
        response.statusText
      );
    }
  } catch (error) {
    console.error("Error sending data to server:", error);
  }
}
document.getElementById("StoreCoursesButton").addEventListener("click", StoreCoursesData);

// Display courses data
async function ViewCoursesData() {
    try {
        const response = await fetch("http://localhost:3005/ViewCoursesData");
        const data = await response.json();

        if (response.ok) {
        console.log("Data received from server successfully.");
        displayDataInTable(data, 'ViewCoursesTable');
        } else {
        console.error(
            "Error receiving data from server:",
            response.status,
            response.statusText
        );
        }
    } catch (error) {
        console.error("Error receiving data from server:", error);
    }
}
document.getElementById("ViewCoursesButton").addEventListener("click", ViewCoursesData);

function clearInputFields() {
    document.getElementById("category").value = "";
    document.getElementById("code").value = "";
    document.getElementById("name").value = "";
    document.getElementById("electiveName").value = "";
    document.getElementById("lectureHours").value = "";
    document.getElementById("tutorialHours").value = "";
    document.getElementById("practicalHours").value = "";
}

async function addCourse() {
    try {
        const category = document.getElementById("category").value;
        const code = document.getElementById("code").value;
        const name = document.getElementById("name").value;
        const electiveName = document.getElementById("electiveName").value;
        const lectureHours = parseInt(document.getElementById("lectureHours").value);
        const tutorialHours = parseInt(document.getElementById("tutorialHours").value);
        const practicalHours = parseInt(document.getElementById("practicalHours").value);

        const response = await fetch("http://localhost:3005/addCourse", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                category,
                code,
                name,
                electiveName,
                lectureHours,
                tutorialHours,
                practicalHours
            }),
        });

        if (response.ok) {
            console.log("Course added successfully.");
            clearInputFields();
        } else {
            console.error("Error adding course:", response.status, response.statusText);
        }
    } catch (error) {
        console.error("Error adding course:", error);
    }
}

// Function to update an existing course
async function updateCourse() {
    try {
        const category = document.getElementById("category").value;
        const code = document.getElementById("code").value;
        const name = document.getElementById("name").value;
        const electiveName = document.getElementById("electiveName").value;
        const lectureHours = parseInt(document.getElementById("lectureHours").value);
        const tutorialHours = parseInt(document.getElementById("tutorialHours").value);
        const practicalHours = parseInt(document.getElementById("practicalHours").value);

        const response = await fetch("http://localhost:3005/updateCourse", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                category,
                code,
                name,
                electiveName,
                lectureHours,
                tutorialHours,
                practicalHours
            }),
        });

        if (response.ok) {
            console.log("Course updated successfully.");
            clearInputFields();
        } else {
            console.error("Error updating course:", response.status, response.statusText);
        }
    } catch (error) {
        console.error("Error updating course:", error);
    }
}

async function deleteCourse() {
    const code = document.getElementById("code").value;
    try {
        const response = await fetch('http://localhost:3005/deleteCourse', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                code
            }),
        });
        if (response.ok) {
            console.log("Course deleted successfully.");
            clearInputFields();
        } else {
            console.error("Error deleting course:", response.status, response.statusText);
        }
    } catch (error) {
        console.error("Error deleting course:", error);
    }
}