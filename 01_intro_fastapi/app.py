from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# 1. starlette
# 2. unicorn ASGI server
# 3. API method GET, POST, PUT, DELETE

class Messageinput(BaseModel):
    role: str
    content: str

class Chatinput(BaseModel):
    message: list[Messageinput]

@app.get("/")
def hello():
    """ 
    A simple hello world endpoint.
    """
    return {"message": "Hello World how're you"}

# @app.get("/about")
# def about():
#     return {"message": "This is a simple FastAPI application."}

# @app.post("/chat/start") 
# def start_chat(message:str):
#     print(message)
#     return message


def test_hello_message():
    assert hello() == {"message": "Hello World how're you"}

@app.post("/chat/")
def chat(input: Chatinput):
    """
    A simple chat endpoint.
    """
    print("[+] Chat input", type(input.model_dump()))
    print("[+] Chat input", input.model_dump())
    print("[+] Chat input Type", type(input))
    print("[+] Chat input Type", input.message)
    print("[+] Chat input Type", type(input.message))
    return {"message": input.message}


if __name__ == "__main__":
    test_hello_message()