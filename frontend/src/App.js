import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

const ExamPaperGenerator = () => {
  const [examType, setExamType] = useState("");
  const [topics, setTopics] = useState([]);
  const [difficulty, setDifficulty] = useState("");
  const [totalMarks, setTotalMarks] = useState("");
  const [papers, setPapers] = useState([]);
  const [loading, setLoading] = useState(false);

  const allTopics = [
    "Dynamic Programming", "Graphs", "Trees", "Arrays", "Linked Lists",
    "Stacks", "Queues", "Heaps", "Sorting", "Searching",
    "Recursion", "Bit Manipulation", "Greedy Algorithms", "Backtracking", "Divide & Conquer"
  ];

  const handleTopicChange = (event) => {
    const { value, checked } = event.target;
    setTopics((prev) =>
      checked ? [...prev, value] : prev.filter((topic) => topic !== value)
    );
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);

    const requestData = {
      exam_type: examType,
      total_marks: parseInt(totalMarks),
      topics: topics,
      num_papers: 3, // Default to 3 papers
    };

    try {
      const response = await fetch("http://127.0.0.1:5000/generate_paper", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(requestData),
      });

      // const response = await fetch("http://127.0.0.1:5000/question-list", {
      //   method: "GET",
      // });


      const data = await response.json();
      //console.log("API Response:", data);
      setPapers(data.papers || []);

      // useEffect(() => {
      //   console.log("Updated Papers Data:", papers);
      // }, [papers]);

    } catch (error) {
      console.error("Error fetching data:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mt-5 p-4 bg-light rounded shadow">
      <h2 className="text-center mb-4 text-primary fw-bold">Exam Paper Generator</h2>
      <form onSubmit={handleSubmit}>

        {/* Exam Type */}
        <div className="card p-3 mb-3 shadow-sm">
          <label className="form-label fw-bold">Exam Type:</label>
          {["Theory", "Practical", "Technical Round"].map((type) => (
            <div key={type} className="form-check">
              <input
                type="radio"
                name="examType"
                value={type}
                className="form-check-input"
                onChange={(e) => setExamType(e.target.value)}
              />
              <label className="form-check-label ms-2">{type}</label>
            </div>
          ))}
        </div>

        {/* Topics */}
        <div className="card p-3 mb-3 shadow-sm">
          <label className="form-label fw-bold">Topics:</label>
          <div className="row">
            {allTopics.map((topic) => (
              <div key={topic} className="col-md-2 col-6 form-check">
                <input
                  type="checkbox"
                  value={topic}
                  className="form-check-input"
                  onChange={handleTopicChange}
                />
                <label className="form-check-label ms-2">{topic}</label>
              </div>
            ))}
          </div>
        </div>

        {/* Difficulty */}
        <div className="card p-3 mb-3 shadow-sm">
          <label className="form-label fw-bold">Difficulty:</label>
          {["Easy", "Medium", "Hard"].map((level) => (
            <div key={level} className="form-check">
              <input
                type="radio"
                name="difficulty"
                value={level}
                className="form-check-input"
                onChange={(e) => setDifficulty(e.target.value)}
              />
              <label className="form-check-label ms-2">{level}</label>
            </div>
          ))}
        </div>

        {/* Total Marks */}
        <div className="card p-3 mb-3 shadow-sm">
          <label className="form-label fw-bold">Total Marks:</label>
          {["50", "70", "100"].map((marks) => (
            <div key={marks} className="form-check">
              <input
                type="radio"
                name="totalMarks"
                value={marks}
                className="form-check-input"
                onChange={(e) => setTotalMarks(e.target.value)}
              />
              <label className="form-check-label ms-2">{marks}</label>
            </div>
          ))}
        </div>

        <button type="submit" className="btn btn-primary w-100" disabled={loading}>
          {loading ? "Generating..." : "Generate Paper"}
        </button>
      </form>

      {/* Display Generated Papers */}
      {papers.length > 0 && (
        <div className="mt-4">
          <h3 className="text-success">Generated Exam Papers</h3>
          {papers.map((paper, index) => (
            <div key={index} className="card p-3 mb-3 shadow-sm">
              <h5 className="fw-bold">Paper {index + 1}</h5>
              <ul>
                {paper.map((question, qIndex) => (
                  <li key={qIndex}>
                    {question?.Question} ({question?.Marks} Marks)
                  </li>
                ))}
              </ul>

              {/* ✅ Single "Download PDF" Button */}
              <button
                className="btn btn-primary mt-2"
                onClick={async () => {
                  try {
                    // ✅ Ensure correct object structure before sending
                    const requestBody = {
                      exam_type: paper[0]?.["Exam Type"] || "N/A",
                      total_marks: paper.reduce((acc, q) => acc + q.Marks, 0),
                      questions: paper.map(q => ({ text: q.Question }))
                    };

                    // console.log(requestBody)  

                    // console.log("Sending request with data:", requestBody);

                    const response = await fetch("http://localhost:5000/generate_pdf", {
                      method: "POST",
                      headers: { "Content-Type": "application/json" },
                      body: JSON.stringify(requestBody)
                    });

                    if (!response.ok) throw new Error("Failed to generate PDF");

                    const data = await response.json();
                    //console.log("Response received:", data);

                    // ✅ Automatically trigger download
                    const downloadUrl = `http://localhost:5000${data.download_url}`;
                    const link = document.createElement("a");
                    link.href = downloadUrl;
                    link.download = "Generated_Exam_Paper.pdf";
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);

                  } catch (error) {
                    console.error("Error generating PDF:", error);
                    alert("Failed to generate PDF. Please try again.");
                  }
                }}
              >
                Download PDF
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default ExamPaperGenerator;
