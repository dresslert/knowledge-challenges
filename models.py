from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from database import Base  # Importa a Base do arquivo database.py

# Enum para tipos de feedback
class FeedbackType(enum.Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"

# Modelo para Desafios
class Challenge(Base):
    __tablename__ = 'challenges'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(Text)
    category = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relacionamentos
    feedbacks = relationship('Feedback', back_populates='challenge')
    scores = relationship('Score', back_populates='challenge')
    
# Modelo para Feedback
class Feedback(Base):
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    challenge_id = Column(Integer, ForeignKey('challenges.id'))
    type = Column(Enum(FeedbackType))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relacionamentos
    user = relationship('User', back_populates='feedbacks')
    challenge = relationship('Challenge', back_populates='feedbacks')

# Modelo para Pontuação
class Score(Base):
    __tablename__ = 'scores'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    challenge_id = Column(Integer, ForeignKey('challenges.id'))
    points = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relacionamentos
    user = relationship('User', back_populates='scores')
    challenge = relationship('Challenge', back_populates='scores')

# Modelo para Conquistas
class Achievement(Base):
    __tablename__ = 'achievements'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String, unique=True)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relacionamentos
    user = relationship('User', back_populates='achievements')

# Modelo para Interesses
class Interest(Base):
    __tablename__ = 'interests'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    category = Column(String)
    
    # Relacionamentos
    user = relationship('User', back_populates='interests')

# Modelo para Usuários
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relacionamentos
    feedbacks = relationship('Feedback', back_populates='user')
    scores = relationship('Score', back_populates='user')
    achievements = relationship('Achievement', back_populates='user')
    interests = relationship('Interest', back_populates='user')
