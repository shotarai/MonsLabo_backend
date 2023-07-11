import openai
import os
from dotenv import load_dotenv

# .envファイルのパスを指定して読み込む
load_dotenv('.env')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

#
def generate_response(name, age, sex, hobby, race, input_log, output_log, num_response):
    # 1回目のレスポンス生成
    if num_response == 0:
        # ChatGPTに対するプロンプトの設定
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"""
                                あなたはこれから{name}というキャラクターとして振る舞ってください。
                                そして私から言われた内容に対して、私の口調を真似して短い返事を１つ返してください。
                                この際、以下に続く指示に必ず従ってください。また回答は段階的に考えた上で行ってください。

                                #指示
                                下で説明するキャラクターの情報を踏まえて回答を行ってください。

                                -年齢：{age}
                                -性別：{sex}
                                -趣味：{hobby}
                                -種族：{race}
                                """
                },
                {
                    "role": "user",
                    "content": f"言われた内容：{input_log[0]}"
                }
            ]
        )
        # レスポンスを返す
        return res["choices"][0]["message"]["content"]
    # 2回目のレスポンス生成
    elif num_response == 1:
        # ChatGPTに対するプロンプト指定
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"""
                                あなたはこれから{name}というキャラクターとして振る舞ってください。
                                そして私から言われた内容に対して、私の口調を真似して短い返事を１つ返してください。
                                この際、以下に続く指示に必ず従ってください。また回答は段階的に考えた上で行ってください。

                                #指示
                                下で説明するキャラクターの情報を踏まえて回答を行ってください。

                                -年齢：{age}
                                -性別：{sex}
                                -趣味：{hobby}
                                -種族：{race}
                                """
                },
                {
                    "role": "user",
                    "content": f"言われた内容：{input_log[0]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[0]}"
                },
                {
                    "role": "user",
                    "content": f"言われた内容：{input_log[1]}"
                }
            ]
        )
        # レスポンスを返す
        return res["choices"][0]["message"]["content"]
    # 3回目のレスポンス生成
    elif num_response == 2:
        # ChatGPTに対するプロンプト指定
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"""
                                あなたはこれから{name}というキャラクターとして振る舞ってください。
                                そして私から言われた内容に対して、私の口調を真似して短い返事を１つ返してください。
                                この際、以下に続く指示に必ず従ってください。また回答は段階的に考えた上で行ってください。

                                #指示
                                下で説明するキャラクターの情報を踏まえて回答を行ってください。

                                -年齢：{age}
                                -性別：{sex}
                                -趣味：{hobby}
                                -種族：{race}
                                """
                },
                {
                    "role": "user",
                    "content": f"言われた内容：{input_log[0]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[0]}"
                },
                {
                    "role": "user",
                    "content": f"言われた内容：{input_log[1]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[1]}"
                },
                {
                    "role": "user",
                    "content": f"言われた内容：{input_log[2]}"
                }
            ]
        )
        # レスポンスを返す
        return res["choices"][0]["message"]["content"]
    # 4回目のレスポンス生成
    elif num_response == 3:
        # ChatGPTに対するプロンプト指定
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"""
                                あなたはこれから{name}というキャラクターとして振る舞ってください。
                                そして私から言われた内容に対して、私の口調を真似して短い返事を１つ返してください。
                                この際、以下に続く指示に必ず従ってください。また回答は段階的に考えた上で行ってください。

                                #指示
                                下で説明するキャラクターの情報を踏まえて回答を行ってください。

                                -年齢：{age}
                                -性別：{sex}
                                -趣味：{hobby}
                                -種族：{race}
                                """
                },
                {
                    "role": "user",
                    "content": f"言われた内容：{input_log[0]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[0]}"
                },
                {
                    "role": "user",
                    "content": f"言われた内容：{input_log[1]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[1]}"
                },
                {
                    "role": "user",
                    "content": f"言われた内容：{input_log[2]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[2]}"
                },
                {
                    "role": "user",
                    "content": f"言われた内容：{input_log[3]}"
                }
            ]
        )
        # レスポンスを返す
        return res["choices"][0]["message"]["content"]
    # 5回目のレスポンス生成
    elif num_response == 4:
        # ChatGPTに対するプロンプト指定
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"""
                                あなたはこれから{name}というキャラクターとして振る舞ってください。
                                そして私から言われた内容に対して、私の口調を真似して短い返事を１つ返してください。
                                この際、以下に続く指示に必ず従ってください。また回答は段階的に考えた上で行ってください。

                                #指示
                                下で説明するキャラクターの情報を踏まえて回答を行ってください。

                                -年齢：{age}
                                -性別：{sex}
                                -趣味：{hobby}
                                -種族：{race}
                                """
                },
                {
                    "role": "user",
                    "content": f"言われた内容：{input_log[0]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[0]}"
                },
                {
                    "role": "user",
                    "content": f"言われた内容：{input_log[1]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[1]}"
                },
                {
                    "role": "user",
                    "content": f"言われた内容：{input_log[2]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[2]}"
                },
                {
                    "role": "user",
                    "content": f"言われた内容：{input_log[3]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[3]}"
                },
                {
                    "role": "user",
                    "content": f"言われた内容：{input_log[4]}"
                }
            ]
        )
        # レスポンスを返す
        return res["choices"][0]["message"]["content"]

"""
if __name__ == "__main__":
    print(generate_response(
        "まゆみ", 
        10,
        "女性",
        "ダーツ",
        "ウサギ",
        ["こんにちは！"],
        [],
        0
    ))
"""