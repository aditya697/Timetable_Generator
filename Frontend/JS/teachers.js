// JavaScript to handle file input and display CSV content

async function StoreTeachersData() {
  try {
    const response = await fetch("http://localhost:3005/InsertTeachersData", {
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
document.getElementById("StoreTeachersButton").addEventListener("click", StoreTeachersData);

async function ViewTeachersData() {
    try {
        const response = await fetch("http://localhost:3005/ViewTeachersData");
        const data = await response.json();

        if (response.ok) {
        console.log("Data received from server successfully.");
        displayDataInTable(data, 'ViewTeachersTable');
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
document.getElementById("ViewTeachersButton").addEventListener("click", ViewTeachersData);

async function addTeacher() {
    try {
        const teacherId = document.getElementById("teacherId").value;
        const teacherName = document.getElementById("teacherName").value;

        const response = await fetch("http://localhost:3005/addTeacher", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                teacherId,
                teacherName
            }),
        });

        if (response.ok) {
            console.log("Teacher added successfully.");
            clearInputFields();
        } else {
            console.error("Error adding teacher:", response.status, response.statusText);
        }
    } catch (error) {
        console.error("Error adding teacher:", error);
    }
}

async function updateTeacher() {
    try {
        const teacherId = document.getElementById("teacherId").value;
        const teacherName = document.getElementById("teacherName").value;

        const response = await fetch("http://localhost:3005/updateTeacher", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                teacherId,
                teacherName
            }),
        });

        if (response.ok) {
            console.log("Teacher updated successfully.");
            clearInputFields();
        } else {
            console.error("Error updating teacher:", response.status, response.statusText);
        }
    } catch (error) {
        console.error("Error updating teacher:", error);
    }
}

async function deleteTeacher() {
    try {
        const teacherId = document.getElementById("teacherId").value;

        const response = await fetch("http://localhost:3005/deleteTeacher", {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                teacherId
            }),
        });

        if (response.ok) {
            console.log("Teacher deleted successfully.");
            clearInputFields();
        } else {
            console.error("Error deleting teacher:", response.status, response.statusText);
        }
    } catch (error) {
        console.error("Error deleting teacher:", error);
    }
}
