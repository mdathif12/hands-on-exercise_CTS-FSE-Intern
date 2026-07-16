import { useState, useEffect } from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";
import "./App.css";

function App() {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [searchTerm, setSearchTerm] = useState("");
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await fetch(
          "https://jsonplaceholder.typicode.com/posts"
        );

        if (!response.ok) {
          throw new Error("Failed to fetch courses");
        }

        const data = await response.json();

        const courseNames = [
  "Web Development",
  "Database Management Systems",
  "Computer Networks",
  "Operating Systems",
  "Cyber Security"
];

const mappedCourses = data.slice(0, 5).map((post, index) => ({
  id: post.id,
  name: courseNames[index],
  code: `CSE${101 + index}`,
  credits: 3 + (index % 2),
  grade: ["A", "A+", "B+", "A", "O"][index]
}));

        setCourses(mappedCourses);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchCourses();
  }, []);

  // Dependency array ensures this runs only when courses change
  useEffect(() => {
    console.log("Courses updated");
  }, [courses]);

  const handleEnroll = (course) => {
    const alreadyEnrolled = enrolledCourses.find(
      (item) => item.id === course.id
    );

    if (!alreadyEnrolled) {
      setEnrolledCourses([...enrolledCourses, course]);
    }
  };

  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div>
      <Header
        siteName="Student Portal"
        enrolledCount={enrolledCourses.length}
      />

      <main className="container">
        <h2>Available Courses</h2>

        <input
          type="text"
          placeholder="Search courses..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="search-box"
        />

        {loading && <p>Loading...</p>}

        {error && <p className="error">{error}</p>}

        <div className="course-grid">
          {!loading &&
            filteredCourses.map((course) => (
              <CourseCard
                key={course.id}
                {...course}
                onEnroll={handleEnroll}
              />
            ))}
        </div>

        <StudentProfile />
      </main>

      <Footer />
    </div>
  );
}

export default App;