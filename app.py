from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Autonomous AI Creator")


@app.get("/")
def home():
    return {
        "project": "Autonomous AI Creator",
        "status": "Running"
    }


@app.get("/plan")
def get_plan():
    return {
        "goal": "Learn DSA",
        "tasks": [
            "Study Arrays",
            "Practice Binary Search",
            "Solve 5 Questions"
        ],
        "next_step": "Complete today's tasks"
    }


class Goal(BaseModel):
    goal: str


@app.post("/goal")
def create_goal(data: Goal):
    goal = data.goal.lower()

    if "python" in goal:
        tasks = [
            "Learn Variables",
            "Practice Loops",
            "Solve 5 Problems"
        ]
    elif "dsa" in goal:
        tasks = [
            "Study Arrays",
            "Practice Binary Search",
            "Solve 5 Questions"
        ]
    else:
        tasks = [
            "Break goal into small steps",
            "Study 1 hour",
            "Review progress"
        ]

    return {
        "goal": data.goal,
        "tasks": tasks,
        "status": "Plan Created"
    }