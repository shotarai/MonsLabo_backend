from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from response import generate_response
from feedback import generate_feedback

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# モンスターに関する情報など
class Info(BaseModel):
    name: str
    age: int
    sex: str
    hobby: str
    race: str
    input_log: list
    output_log: list
    num_response: int

# モンスターとの会話ログ
class Log(BaseModel):
    input_log: list
    output_log: list

# テスト
@app.get('/')
def test():
    return {'Hello': 'World!!!!'}

# 与えられた情報からレスポンスを生成
@app.post('/response')
def return_response(info: Info):
    # 
    return generate_response(
        info.name,
        info.age,
        info.sex,
        info.hobby,
        info.race,
        info.input_log,
        info.output_log,
        info.num_response
    )

# 会話のログからフィードバックを生成
@app.post('/feedback')
def return_feedback(log: Log):
    # 
    return generate_feedback(
        log.input_log,
        log.output_log
    )