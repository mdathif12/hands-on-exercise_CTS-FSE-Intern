from pydantic import BaseModel, EmailStr


class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int


class CourseResponse(CourseCreate):
    id: int

    class Config:
        from_attributes = True


class StudentCreate(BaseModel):
    name: str
    email: EmailStr


class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int


class EnrollmentResponse(EnrollmentCreate):
    id: int

    class Config:
        from_attributes = True