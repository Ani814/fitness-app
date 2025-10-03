"""
Seed script for populating the database with predefined exercises.
Run this after creating the database and running migrations:
    python seed.py
"""

from sqlalchemy.orm import Session
from database import SessionLocal
import models

# Predefined exercise list (20 diverse exercises)
EXERCISES = [
    {
        "name": "Push-Up",
        "description": "A bodyweight exercise that targets the chest, triceps, and shoulders.",
        "muscle_group": "Chest"
    },
    {
        "name": "Squat",
        "description": "A lower-body exercise that strengthens the quads, glutes, and hamstrings.",
        "muscle_group": "Legs"
    },
    {
        "name": "Pull-Up",
        "description": "An upper-body exercise that primarily targets the back and biceps.",
        "muscle_group": "Back"
    },
    {
        "name": "Plank",
        "description": "An isometric core exercise that improves stability and endurance.",
        "muscle_group": "Core"
    },
    {
        "name": "Bench Press",
        "description": "A compound lift that builds the chest, triceps, and shoulders using a barbell.",
        "muscle_group": "Chest"
    },
    {
        "name": "Deadlift",
        "description": "A compound exercise that works the entire posterior chain, including back, glutes, and hamstrings.",
        "muscle_group": "Back"
    },
    {
        "name": "Overhead Press",
        "description": "A shoulder press with a barbell or dumbbells that targets delts and triceps.",
        "muscle_group": "Shoulders"
    },
    {
        "name": "Lunge",
        "description": "A unilateral lower-body exercise targeting quads and glutes.",
        "muscle_group": "Legs"
    },
    {
        "name": "Bicep Curl",
        "description": "An isolation exercise focusing on the biceps using dumbbells or barbells.",
        "muscle_group": "Arms"
    },
    {
        "name": "Tricep Dip",
        "description": "A bodyweight exercise that strengthens the triceps, chest, and shoulders.",
        "muscle_group": "Arms"
    },
    {
        "name": "Leg Press",
        "description": "A machine exercise that targets the quads, glutes, and hamstrings.",
        "muscle_group": "Legs"
    },
    {
        "name": "Russian Twist",
        "description": "A rotational core exercise that strengthens obliques and improves stability.",
        "muscle_group": "Core"
    },
    {
        "name": "Lat Pulldown",
        "description": "A machine exercise targeting the latissimus dorsi and upper back.",
        "muscle_group": "Back"
    },
    {
        "name": "Chest Fly",
        "description": "An isolation chest exercise performed with dumbbells or a machine.",
        "muscle_group": "Chest"
    },
    {
        "name": "Step-Up",
        "description": "A unilateral leg exercise that builds balance and leg strength.",
        "muscle_group": "Legs"
    },
    {
        "name": "Mountain Climber",
        "description": "A dynamic, core-focused cardio move that also works the shoulders and legs.",
        "muscle_group": "Core"
    },
    {
        "name": "Burpee",
        "description": "A full-body conditioning exercise combining a squat, push-up, and jump.",
        "muscle_group": "Full Body"
    },
    {
        "name": "Calf Raise",
        "description": "An isolation exercise that targets the calf muscles.",
        "muscle_group": "Legs"
    },
    {
        "name": "Hip Thrust",
        "description": "A glute-dominant exercise that builds posterior chain strength.",
        "muscle_group": "Glutes"
    },
    {
        "name": "Side Plank",
        "description": "An isometric exercise that strengthens obliques and improves core stability.",
        "muscle_group": "Core"
    },
]


def seed_exercises(db: Session):
    """Insert exercises into the database if they don't already exist."""
    for ex in EXERCISES:
        existing = db.query(models.Exercise).filter_by(name=ex["name"]).first()
        if not existing:
            new_ex = models.Exercise(
                name=ex["name"],
                description=ex["description"],
                muscle_group=ex["muscle_group"]
            )
            db.add(new_ex)
    db.commit()


def main():
    print("Seeding database with predefined exercises...")
    db = SessionLocal()
    try:
        seed_exercises(db)
        print(f"✅ Successfully seeded {len(EXERCISES)} exercises.")
    except Exception as e:
        print(f"❌ Error while seeding: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    main()
