async function StoreSemesterCoursesData() {
  try {
    const response = await fetch("http://localhost:3005/InsertSemesterCoursesData", {
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
document.getElementById("StoreSemesterCoursesButton").addEventListener("click", StoreSemesterCoursesData);

// Display courses data
async function ViewSemesterCoursesData() {
    try {
        const Semester = document.getElementById("Semester").value;
        const BranchName = document.getElementById("BranchName").value;
        const CourseCode = document.getElementById("CourseCode").value;
        const response = await fetch("http://localhost:3005/ViewSemesterCoursesData");
        const data = await response.json();

        if (response.ok) {
        console.log("Data received from server successfully.");
        displayDataInTable(data, 'ViewSemesterCoursesTable');
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
document.getElementById("ViewSemesterCoursesButton").addEventListener("click", ViewSemesterCoursesData);
