async function StoreCourseTeacherData() {
  try {
    const response = await fetch("http://localhost:3005/InsertCourseTeacherData", {
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
document.getElementById("StoreCourseTeacherButton").addEventListener("click", StoreCourseTeacherData);

// Display courses data
async function ViewCourseTeacherData() {
    try {
        const response = await fetch("http://localhost:3005/ViewCourseTeacherData");
        const data = await response.json();

        if (response.ok) {
        console.log("Data received from server successfully.");
        displayDataInTable(data, 'ViewCourseTeacherTable');
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
document.getElementById("ViewCourseTeacherButton").addEventListener("click", ViewCourseTeacherData);

// Add  courses data
async function addCourseTeacher() {
    try {
        const CourseCode = document.getElementById("CourseCode").value;
        const TeacherID = document.getElementById("TeacherID").value;

        const response = await fetch("http://localhost:3005/addCourseTeacher", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                CourseCode,
                TeacherID
            }),
        });

        if (response.ok) {
            console.log("Data added to server successfully.");
        } else {
            console.error(
                "Error adding data to server:",
                response.status,
                response.statusText
            );
        }
    } catch (error) {
        console.error("Error adding data to server:", error);
    }
}


async function deleteCourseTeacher() {
    try {
        const CourseCode = document.getElementById("CourseCode").value;
        const TeacherID = document.getElementById("TeacherID").value;

        const response = await fetch("http://localhost:3005/deleteCourseTeacher", {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                CourseCode,
                TeacherID
            }),
        });

        if (response.ok) {
            console.log("Data deleted from server successfully.");
        } else {
            console.error(
                "Error deleting data from server:",
                response.status,
                response.statusText
            );
        }
    } catch (error) {
        console.error("Error deleting data from server:", error);
    }
}