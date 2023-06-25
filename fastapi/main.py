### TO START THE SERVER ###
# fastapi uvicorn --port 8000 --reload --reload  OR
# python -m uvicorn main:app --reload OR
# uvicorn main:app --reload
# ###########################

from uuid import UUID

from fastapi import FastAPI, HTTPException
from api.models import User, Role, Gender, Employee
from typing import List

app = FastAPI()
db: List[User] = [
    User(
        id="538b3c05-41b5-4b91-b172-9b1161dfec62",
        first_name="Jane",
        last_name="Doe",
        gender=Gender.FEMALE,
        roles=Role.STUDENT),
    User(
        id="99862670-8484-4e98-ab79-9574e180a1b1",
        first_name="John",
        last_name="Doe",
        gender=Gender.MALE,
        roles=Role.ADMIN)]

db_employees = [Employee] =[
    Employee(
        id="538b3c05-41b5-4b91-b172-9b1161dfec62",
        first_name="Jane",
        last_name="Doe",
        gender=Gender.FEMALE,
        roles=Role.STUDENT)
]

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/api/v1/employees")
def get_employees():
    return db_employees
@app.get("/api/v1/users")
def read_users():
    return db



@app.post("/api/v1/users")
async def post_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"id": user.id}
    raise HTTPException(status_code=404, detail=f"User '{id}' not found")
