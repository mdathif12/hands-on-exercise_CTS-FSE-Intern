from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    status,
    BackgroundTasks
)

from sqlalchemy.orm import Session

import models
import schemas

from database import (
    SessionLocal,
    engine
)

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Course Management API",
    description="CRUD API using FastAPI",
    version="1.0.0",
    contact={
        "name": "Athif",
        "email": "athif@example.com"
    }
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def send_confirmation_email(email):
    print(f"Sending confirmation to {email}")


# ---------------- COURSES ----------------

@app.post(
    "/api/courses/",
    response_model=schemas.CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create Course",
    response_description="Created Course"
)
def create_course(
    course: schemas.CourseCreate,
    db: Session = Depends(get_db)
):
    new_course = models.Course(**course.dict())

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course


@app.get(
    "/api/courses/",
    response_model=list[schemas.CourseResponse],
    tags=["Courses"]
)
def get_courses(
    db: Session = Depends(get_db)
):
    return db.query(models.Course).all()


@app.get(
    "/api/courses/{course_id}",
    response_model=schemas.CourseResponse,
    tags=["Courses"]
)
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    course = db.query(models.Course).filter(
        models.Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


@app.put(
    "/api/courses/{course_id}",
    response_model=schemas.CourseResponse,
    tags=["Courses"]
)
def update_course(
    course_id: int,
    course: schemas.CourseCreate,
    db: Session = Depends(get_db)
):
    db_course = db.query(models.Course).filter(
        models.Course.id == course_id
    ).first()

    if not db_course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    db_course.name = course.name
    db_course.code = course.code
    db_course.credits = course.credits

    db.commit()
    db.refresh(db_course)

    return db_course


@app.delete(
    "/api/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Courses"]
)
def delete_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    course = db.query(models.Course).filter(
        models.Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    db.delete(course)
    db.commit()

    return


# -------- COURSE STUDENTS JOIN --------

@app.get(
    "/api/courses/{course_id}/students/",
    tags=["Courses"]
)
def get_course_students(
    course_id: int,
    db: Session = Depends(get_db)
):
    students = (
        db.query(models.Student)
        .join(models.Enrollment)
        .filter(
            models.Enrollment.course_id == course_id
        )
        .all()
    )

    return students


# ---------------- STUDENTS ----------------

@app.post(
    "/api/students/",
    response_model=schemas.StudentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Students"]
)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    new_student = models.Student(**student.dict())

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


@app.get(
    "/api/students/",
    response_model=list[schemas.StudentResponse],
    tags=["Students"]
)
def get_students(
    db: Session = Depends(get_db)
):
    return db.query(models.Student).all()


@app.put(
    "/api/students/{student_id}",
    response_model=schemas.StudentResponse,
    tags=["Students"]
)
def update_student(
    student_id: int,
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    db_student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if not db_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db_student.name = student.name
    db_student.email = student.email

    db.commit()
    db.refresh(db_student)

    return db_student


@app.delete(
    "/api/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Students"]
)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return


# ---------------- ENROLLMENTS ----------------

@app.post(
    "/api/enrollments/",
    response_model=schemas.EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Enrollments"]
)
def create_enrollment(
    enrollment: schemas.EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    new_enrollment = models.Enrollment(
        **enrollment.dict()
    )

    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)

    student = db.query(models.Student).filter(
        models.Student.id == enrollment.student_id
    ).first()

    if student:
        background_tasks.add_task(
            send_confirmation_email,
            student.email
        )

    return new_enrollment


@app.get(
    "/api/enrollments/",
    response_model=list[schemas.EnrollmentResponse],
    tags=["Enrollments"]
)
def get_enrollments(
    db: Session = Depends(get_db)
):
    return db.query(models.Enrollment).all()


@app.delete(
    "/api/enrollments/{enrollment_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Enrollments"]
)
def delete_enrollment(
    enrollment_id: int,
    db: Session = Depends(get_db)
):
    enrollment = db.query(
        models.Enrollment
    ).filter(
        models.Enrollment.id == enrollment_id
    ).first()

    if not enrollment:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    db.delete(enrollment)
    db.commit()

    return