from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from response import generate_response
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# フロントエンドから与えられる入力
class Info(BaseModel):
    name: str
    age: int
    sex: str
    hobby: str
    race: str
    input_log: list
    output_log: list
    num_response: int

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
