from sqlalchemy.orm import Session
from models import Challenge, User, Feedback
from schemas import ChallengeCreate, UserCreate, FeedbackCreate

# Serviço para criar um desafio
def create_challenge(db: Session, challenge: ChallengeCreate):
    db_challenge = Challenge(**challenge.dict())
    db.add(db_challenge)
    db.commit()
    db.refresh(db_challenge)
    return db_challenge

# Serviço para obter desafios
def get_challenges(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Challenge).offset(skip).limit(limit).all()

# Serviço para criar um usuário
def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Serviço para obter usuários
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

# Serviço para criar um feedback
def create_feedback(db: Session, feedback: FeedbackCreate):
    db_feedback = Feedback(**feedback.dict())
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

# Serviço para obter feedbacks
def get_feedbacks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Feedback).offset(skip).limit(limit).all()
