from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from fastapi.middleware.cors import CORSMiddleware

from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm

from jose import jwt
from jose import JWTError

from sqlalchemy.orm import Session

from database import Base
from database import engine
from database import SessionLocal

from models import User
from models import Course

from schemas import UserCreate
from schemas import UserResponse
from schemas import CourseCreate
from schemas import CourseResponse

from security import get_password_hash
from security import verify_password

from auth import create_access_token
from auth import SECRET_KEY
from auth import ALGORITHM

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hands On 9 API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login/"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = db.query(User).filter(
        User.email == email
    ).first()

    return user

@app.post(
    "/api/v1/auth/register/",
    response_model=UserResponse
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    new_user = User(
        email=user.email,
        hashed_password=get_password_hash(
            user.password
        )
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.post("/api/v1/auth/login/")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        form_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@app.get(
    "/api/v1/courses/",
    response_model=list[CourseResponse]
)
def get_courses(
    db: Session = Depends(get_db)
):
    return db.query(Course).all()

@app.post(
    "/api/v1/courses/",
    response_model=CourseResponse
)
def create_course(
    course: CourseCreate,
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):
    new_course = Course(**course.dict())

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course

@app.delete(
    "/api/v1/courses/{course_id}"
)
def delete_course(
    course_id: int,
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(get_db)
):
    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    db.delete(course)
    db.commit()

    return {
        "message": "Course deleted"
    }

"""
OAuth2 Authorization Code Flow:

1. User logs in with Google/GitHub.
2. Provider returns authorization code.
3. Backend exchanges code for token.
4. Token is used for API access.

This project uses direct JWT login:
email + password -> JWT token.
"""