import openai
import os
from dotenv import load_dotenv

# .envファイルのパスを指定して読み込む
load_dotenv('.env')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

#
def generate_feedback(input_log, output_log):
    # 会話の流れが交互になるようにする
    # 参考：https://qiita.com/Rihoritsuko/items/5ffc004cae89706f9cc3
    log = [None] * (len(input_log) + len(output_log))
    log[::2] = input_log
    log[1::2] = output_log
    # ChatGPTに対するプロンプトの設定
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"""
                            与えられた私とあなたの会話履歴をもとに、
                            あなたに関する情報と私に対する印象を伝えてください。
                            """
            },
            {
                "role": "user",
                "content": f"""
                            会話履歴：{log}
                            私の会話部分：{input_log}
                            あなたの会話部分：{output_log}
                            """
            }
        ]
    )
    # レスポンスを返す
    return res["choices"][0]["message"]["content"]

"""
if __name__ == "__main__":
    pass
"""