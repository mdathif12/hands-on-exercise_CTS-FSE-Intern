export default function CourseCard({
  course,
}) {
  return (
    <div className="card">
      <h2>{course.title}</h2>

      <p>
        {course.description}
      </p>

      <button>
        Enroll Now
      </button>
    </div>
  );
}