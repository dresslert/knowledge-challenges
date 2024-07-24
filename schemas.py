from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ChallengeBase(BaseModel):
    title: str
    description: Optional[str] = None
    category: str

class ChallengeCreate(ChallengeBase):
    pass

class Challenge(ChallengeBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class FeedbackBase(BaseModel):
    content: str
    type: str

class FeedbackCreate(FeedbackBase):
    user_id: int
    challenge_id: int

class Feedback(FeedbackBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
