import { Link } from "react-router-dom";

function HomePage() {
  return (
    <div className="hero">
      <h1>Welcome to Student Learning Portal</h1>

      <p>
        Discover courses, enroll instantly and
        track your learning journey.
      </p>

      <Link className="hero-btn" to="/courses">
        Explore Courses
      </Link>
    </div>
  );
}

export default HomePage;