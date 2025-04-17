from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
app=FastAPI()

#CORS Settings
orgins=['*'] # allow all orgins (can be modified later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=orgins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#input request model
class QuestionRequest(BaseModel):
    question:str

class AnswerResponse(BaseModel):
    answer:str


# post endpoint
@app.post('/ask',response_model=AnswerResponse)
async def answer_question(request:QuestionRequest):
    question=request.question
    answer="Here is a generic answer";
    return {'answer': answer}
#only run if you run python main.py
if(__name__=='__main__'):
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)


