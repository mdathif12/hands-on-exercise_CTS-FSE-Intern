import { useEffect }
from "react";

import {
  useDispatch,
  useSelector,
} from "react-redux";

import {
  fetchAllCourses,
  selectCourses,
  selectLoading,
  selectError,
} from "../redux/courseSlice";

import CourseCard
from "../components/CourseCard";

import LoadingSpinner
from "../components/LoadingSpinner";

export default function CoursesPage() {

  const dispatch =
    useDispatch();

  const courses =
    useSelector(selectCourses);

  const loading =
    useSelector(selectLoading);

  const error =
    useSelector(selectError);

  useEffect(() => {
    dispatch(
      fetchAllCourses()
    );
  }, [dispatch]);

  if (loading) {
    return (
      <LoadingSpinner />
    );
  }

  if (error) {
    return (
      <h2 className="error">
        {error}
      </h2>
    );
  }

  return (
    <div className="container">

      <header>
        <h1>
          Course Enrollment
          Management Portal
        </h1>

        <p>
          Digital Nurture 5.0
          Frontend Development
        </p>
      </header>

      <div className="grid">
        {courses.map(
          (course) => (
            <CourseCard
              key={course.id}
              course={course}
            />
          )
        )}
      </div>

    </div>
  );
}