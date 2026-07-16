from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from fastapi import Request

from sqlalchemy.orm import Session

from database import SessionLocal
from models import Course

from schemas import (
    CourseCreate,
    CourseUpdate,
    CoursePatch
)

router = APIRouter(
    prefix="/api/v1/courses",
    tags=["Courses"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def error_response(code, message, field=None):
    return {
        "error": {
            "code": code,
            "message": message,
            "field": field
        }
    }

@router.get("/")
def get_courses(
    request: Request,
    page: int = 1,
    page_size: int = 2,
    search: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(Course)

    if search:
        query = query.filter(
            (Course.name.ilike(f"%{search}%")) |
            (Course.code.ilike(f"%{search}%"))
        )

    total = query.count()

    courses = query.offset(
        (page - 1) * page_size
    ).limit(page_size).all()

    next_url = None
    previous_url = None

    if page * page_size < total:
        next_url = f"?page={page+1}&page_size={page_size}"

    if page > 1:
        previous_url = f"?page={page-1}&page_size={page_size}"

    return {
        "count": total,
        "next": next_url,
        "previous": previous_url,
        "results": courses
    }

@router.get("/{course_id}")
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail=error_response(
                "NOT_FOUND",
                f"Course with id {course_id} does not exist"
            )
        )

    return course

@router.post("/", status_code=201)
def create_course(
    course: CourseCreate,
    response: Response,
    db: Session = Depends(get_db)
):
    new_course = Course(**course.dict())

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    response.headers[
        "Location"
    ] = f"/api/v1/courses/{new_course.id}"

    return new_course

@router.put("/{course_id}")
def update_course(
    course_id: int,
    course_data: CourseUpdate,
    db: Session = Depends(get_db)
):
    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail=error_response(
                "NOT_FOUND",
                f"Course with id {course_id} does not exist"
            )
        )

    for key, value in course_data.dict().items():
        setattr(course, key, value)

    db.commit()
    db.refresh(course)

    return course

@router.patch("/{course_id}")
def patch_course(
    course_id: int,
    patch_data: CoursePatch,
    db: Session = Depends(get_db)
):
    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail=error_response(
                "NOT_FOUND",
                f"Course with id {course_id} does not exist"
            )
        )

    updates = patch_data.dict(
        exclude_unset=True
    )

    for key, value in updates.items():
        setattr(course, key, value)

    db.commit()
    db.refresh(course)

    return course

@router.delete("/{course_id}",
               status_code=204)
def delete_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail=error_response(
                "NOT_FOUND",
                f"Course with id {course_id} does not exist"
            )
        )

    db.delete(course)
    db.commit()

    return Response(status_code=204)