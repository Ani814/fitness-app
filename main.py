from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from . import models, schemas, crud, auth
from .database import SessionLocal, engine

# --- Create tables ---
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# --- Dependency ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Auth routes ---
@app.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db, user)

# --- Workout Plans ---
@app.post("/workout_plans/", response_model=schemas.WorkoutPlan)
def create_workout_plan(workout: schemas.WorkoutPlanCreate, db: Session = Depends(get_db),
                        current_user: models.User = Depends(auth.get_current_user)):
    return crud.create_workout_plan(db, workout, current_user.id)

@app.get("/workout_plans/{workout_id}", response_model=schemas.WorkoutPlan)
def get_workout_plan(workout_id: int, db: Session = Depends(get_db),
                     current_user: models.User = Depends(auth.get_current_user)):
    plan = crud.get_workout_plan(db, workout_id, current_user.id)
    if not plan:
        raise HTTPException(status_code=404, detail="Workout plan not found")
    return plan

# --- Weight ---
@app.post("/weight", response_model=schemas.WeightRecord)
def add_weight(weight_record: schemas.WeightRecordCreate, db: Session = Depends(get_db),
               current_user: models.User = Depends(auth.get_current_user)):
    return crud.add_weight_record(db, weight_record, current_user.id)

# --- Fitness Goals ---
@app.post("/fitness_goals", response_model=schemas.FitnessGoal)
def set_goal(goal: schemas.FitnessGoalCreate, db: Session = Depends(get_db),
             current_user: models.User = Depends(auth.get_current_user)):
    return crud.set_fitness_goal(db, goal, current_user.id)

# --- Exercises ---
@app.get("/exercises", response_model=list[schemas.Exercise])
def get_exercises(db: Session = Depends(get_db)):
    return crud.get_all_exercises(db)
