from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash

# --- User ---
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# --- Workout Plan ---
def create_workout_plan(db: Session, workout: schemas.WorkoutPlanCreate, user_id: int):
    exercises = db.query(models.Exercise).filter(models.Exercise.id.in_(workout.exercises)).all()
    db_plan = models.WorkoutPlan(name=workout.name, user_id=user_id, exercises=exercises)
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan

def get_workout_plan(db: Session, workout_id: int, user_id: int):
    return db.query(models.WorkoutPlan).filter_by(id=workout_id, user_id=user_id).first()

# --- Weight Record ---
def add_weight_record(db: Session, weight_record: schemas.WeightRecordCreate, user_id: int):
    db_record = models.WeightRecord(weight=weight_record.weight, user_id=user_id)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

# --- Fitness Goal ---
def set_fitness_goal(db: Session, goal: schemas.FitnessGoalCreate, user_id: int):
    db_goal = models.FitnessGoal(goal_type=goal.goal_type, goal_value=goal.goal_value, user_id=user_id)
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal

# --- Exercises ---
def get_all_exercises(db: Session):
    return db.query(models.Exercise).all()
