export const getAllCourses = async () => {
  return [
    {
      id: 1,
      title: "React Fundamentals",
      description:
        "Learn components, JSX, props and state."
    },
    {
      id: 2,
      title: "Advanced JavaScript",
      description:
        "Master ES6+, promises and async/await."
    },
    {
      id: 3,
      title: "Redux Toolkit",
      description:
        "Manage application state efficiently."
    },
    {
      id: 4,
      title: "REST API Integration",
      description:
        "Consume APIs using Axios and Fetch."
    },
    {
      id: 5,
      title: "Responsive Web Design",
      description:
        "Build mobile-friendly applications."
    },
    {
      id: 6,
      title: "Frontend Architecture",
      description:
        "Organize scalable frontend projects."
    }
  ];
};

export const getCourseById = async (id) => {
  const courses = await getAllCourses();
  return courses.find(
    (course) => course.id === Number(id)
  );
};

export const enrollStudent = async (
  studentId,
  courseId
) => {
  return {
    success: true,
    studentId,
    courseId,
    message: "Enrollment Successful"
  };
};