# creating a base route
from fastapi import FastAPI

# creating an instance of the main class
app = FastAPI()

# minimal app - et requests
# creating a route decorator
@app.get("/", tags=['ROOT'])

async def root() -> dict:
    return{"ping": "pong"}

# Get --> Read Todo
@app.get("/todo", tags=['todos'])
async def get_to_do() -> dict:
    return {"data": todos}



# Post --> Create Todo
@app.post("/todo", tags=['todos'])
async def add_to_do(todo:dict) -> dict:
    todos.append(todo)
    return {
        "data": "A todo has been added succesfully"
    }


# Put --> Update Todo
@app.put("/todo/{id}", tags=['todos'])
async def update_to_do(id:int, body:dict) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todo['Activity'] = body['Activity']
            return {
                "data": "to do with the id {id} has been updated"
            }
    return {
        "data": f"Todo with id number {id} was not found"
    }


# Delete --> Delete Todo
@app.delete("/todo{id}", tags = ["todos"])
async def delete_to_do(id: int) -> dict:
    for todo in todos:
        if int((todo["id"])) == id:
            todos.remove(todo)
            return {
                "data": "data with id{id} has been deleted successfully"
            }
    return {
        "data": f"this to do with id{id} wasn't found"
    }


todos = [
{
    "id": 1,
    "Activity": "Jogging for 2 hours at 7:00 AM."
    },
{
    "id": 2,
    "Activity": "Writing 3 pages of my new book at 2:00PM."
}
]