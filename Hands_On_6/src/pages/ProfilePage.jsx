import { useSelector, useDispatch } from "react-redux";
import { unenroll } from "../redux/enrollmentSlice";

function ProfilePage() {
  const dispatch = useDispatch();

  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );

  return (
    <div className="profile-container">
      <h1>My Enrolled Courses</h1>

      {enrolledCourses.length === 0 ? (
        <div className="empty">
          <h3>No Courses Enrolled Yet</h3>
        </div>
      ) : (
        enrolledCourses.map((course) => (
          <div
            className="profile-card"
            key={course.id}
          >
            <h3>{course.title}</h3>

            <button
              className="remove-btn"
              onClick={() =>
                dispatch(unenroll(course.id))
              }
            >
              Remove
            </button>
          </div>
        ))
      )}
    </div>
  );
}

export default ProfilePage;