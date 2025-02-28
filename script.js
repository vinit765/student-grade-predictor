function predictScore() {
    let data = {
        "Attendance (%)": document.getElementById("attendance").value,
        "Midterm_Score": document.getElementById("midterm").value,
        "Final_Score": document.getElementById("final").value,
        "Assignments_Avg": document.getElementById("assignments").value,
        "Study_Hours_per_Week": document.getElementById("study_hours").value,
        "Stress_Level (1-10)": document.getElementById("stress").value,
        "Sleep_Hours_per_Night": document.getElementById("sleep").value
    };

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = `🎯 Predicted Grade: ${data.predicted_grade}`;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
