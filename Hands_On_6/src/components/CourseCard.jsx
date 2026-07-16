import { Link } from "react-router-dom";

function CourseCard({ course }) {
  return (
    <div className="card">
      <h3>{course.title}</h3>

      <p>{course.description}</p>

      <Link
        className="btn"
        to={`/courses/${course.id}`}
      >
        View Details
      </Link>
    </div>
  );
}

export default CourseCard;