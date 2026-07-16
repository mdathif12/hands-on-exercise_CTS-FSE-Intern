import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";

import courses from "../data/courses";
import { enroll } from "../redux/enrollmentSlice";

function CourseDetailPage() {
  const { courseId } = useParams();

  const navigate = useNavigate();
  const dispatch = useDispatch();

  const course = courses.find(
    (item) => item.id === Number(courseId)
  );

  if (!course) {
    return <h2>Course Not Found</h2>;
  }

  const handleEnroll = () => {
    dispatch(enroll(course));
    navigate("/profile");
  };

  return (
    <div className="detail-card">
      <h1>{course.title}</h1>

      <p>{course.description}</p>

      <button onClick={handleEnroll}>
        Enroll Now
      </button>
    </div>
  );
}

export default CourseDetailPage;