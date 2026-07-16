import { Link } from "react-router-dom";
import { useSelector } from "react-redux";

function Header() {
  const enrolledCount = useSelector(
    (state) => state.enrollment.enrolledCourses.length
  );

  return (
    <header className="header">
      <div className="logo">
        Student Portal
      </div>

      <nav>
        <Link to="/">Home</Link>
        <Link to="/courses">Courses</Link>
        <Link to="/profile">Profile</Link>
      </nav>

      <div className="count">
        Enrolled: {enrolledCount}
      </div>
    </header>
  );
}

export default Header;