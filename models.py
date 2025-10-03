from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Float, Table
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

# Association table for WorkoutPlan <-> Exercises
workout_exercise_association = Table(
    'workout_exercise',
    Base.metadata,
    Column('workout_plan_id', Integer, ForeignKey('workout_plans.id')),
    Column('exercise_id', Integer, ForeignKey('exercises.id'))
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    weights = relationship("WeightRecord", back_populates="user")
    fitness_goals = relationship("FitnessGoal", back_populates="user")
    workout_plans = relationship("WorkoutPlan", back_populates="user")


class Exercise(Base):
    __tablename__ = "exercises"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    muscle_group = Column(String)
    workouts = relationship("WorkoutPlan", secondary=workout_exercise_association, back_populates="exercises")


class WorkoutPlan(Base):
    __tablename__ = "workout_plans"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    user = relationship("User", back_populates="workout_plans")
    exercises = relationship("Exercise", secondary=workout_exercise_association, back_populates="workouts")


class WeightRecord(Base):
    __tablename__ = "weight_records"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    weight = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="weights")


class FitnessGoal(Base):
    __tablename__ = "fitness_goals"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    goal_type = Column(String)
    goal_value = Column(Float)
    achieved = Column(Boolean, default=False)
    date_set = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="fitness_goals")
