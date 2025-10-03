from pydantic import BaseModel
from typing import List, Optional

# --- User ---
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# --- Token ---
class Token(BaseModel):
    access_token: str
    token_type: str

# --- Exercise ---
class ExerciseBase(BaseModel):
    name: str
    description: Optional[str] = None
    muscle_group: Optional[str] = None

class Exercise(ExerciseBase):
    id: int

    class Config:
        orm_mode = True

# --- Workout Plan ---
class WorkoutPlanBase(BaseModel):
    name: str
    exercises: List[int]  # IDs of exercises

class WorkoutPlanCreate(WorkoutPlanBase):
    pass

class WorkoutPlan(WorkoutPlanBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

# --- Weight Record ---
class WeightRecordBase(BaseModel):
    weight: float

class WeightRecordCreate(WeightRecordBase):
    pass

class WeightRecord(WeightRecordBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

# --- Fitness Goal ---
class FitnessGoalBase(BaseModel):
    goal_type: str
    goal_value: float

class FitnessGoalCreate(FitnessGoalBase):
    pass

class FitnessGoal(FitnessGoalBase):
    id: int
    user_id: int
    achieved: bool

    class Config:
        orm_mode = True
