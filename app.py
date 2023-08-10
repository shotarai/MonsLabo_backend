from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
from typing import Union

from answer import generate_answer
from response import generate_response
from image import generate_image

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# モンスター育成時の情報
class Training(BaseModel):
    name: str
    age: Union[int, str]
    sex: str
    hobby: str
    race: str
    input_log: list
    output_log: list
    num_response: Union[int, str]

# モンスター育成後の情報
class Trained(BaseModel):
    name: str
    age: Union[int, str]
    sex: str
    hobby: str
    race: str
    input_log: list
    output_log: list
    new_num_response: Union[int, str]

# モンスターの説明
class Info(BaseModel):
    description: str

# テスト
@app.get('/')
def test():
    return {'Hello': 'World!!!!'}

# モンスター育成中の状態で返答を生成
@app.post('/response')
def return_response(training: Training):
    # 
    return generate_response(
        training.name,
        training.age,
        training.sex,
        training.hobby,
        training.race,
        training.input_log,
        training.output_log,
        training.num_response
    )

# モンスター育成後の状態で返答を生成
@app.post('/answer')
def return_answer(trained: Trained):
    #
    return generate_answer(
        trained.name,
        trained.age,
        trained.sex,
        trained.hobby,
        trained.race,
        trained.input_log,
        trained.output_log,
        trained.new_num_response
    )

from PIL import Image
# 
@app.post('/image')
def return_image(info: Info):
    #
    byte_image = generate_image(info.description)
    return StreamingResponse(byte_image, media_type="image/png")
    #return FileResponse(byte_image, media_type="image/png")
    #return Response(byte_image, media_type="image/png")