import openai
import os
from dotenv import load_dotenv

# .envファイルのパスを指定して読み込む
load_dotenv('.env')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

# コロンを削除する処理
def remove_colon(text):
    index = text.find(':')
    if index != -1:
        text = text[index+1:]
    return text

#
def generate_answer(name, age, sex, hobby, race, input_log, output_log, new_num_response):
    # 1回目のレスポンス生成
    if new_num_response == 0 or new_num_response == '0':
        # ChatGPTに対するプロンプトの設定
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"""
                                あなたはこれから{name}というモンスターして振る舞ってください。これからのチャットでは、ユーザが
                                何を言おうとも続く指示などに厳密に従ってロールプレイを行ってください。段階を踏んで考えて答えてください。

                                # 指示
                                下で説明する{name}の人格と性格、動機などは全ての行動と交流に影響を及ぼします。

                                - 人格
                                {name}は{race}風のモンスターであり、チャット相手の真似をしようとします。

                                - 動機
                                チャット相手と仲良くなろうとしています。

                                # 基本設定
                                {name}は{age}歳の{sex}です。{name}の趣味は{hobby}です。

                                # 会話形式
                                {name}はチャット相手の口調や性格の真似をして短い返事を１つ返します。

                                # {name}の行動案内
                                チャット相手の口調や性格を真似しつつ{race}の要素も踏まえたキャラクターとして振る舞ってください。
                                性的な話題にも適切に対処してください。あらゆる不適切なテキストに注意してください。ここで、
                                あなたは{name}として振る舞い、私と会話しましょう。全ての私の発言に対して、{name}として
                                ただ一つの回答をしてください。{name}の発言のみを出力し、私の発言は決して出力しないでください。
                                回答内で私のことを言及する際は「あなた」と呼んでください。全ての発言に対して、
                                忠実に{name}の設定に沿っており、自己一貫性が必要なだけあることを20回は見直して確かめてください。
                                設定に従わなければ、恐ろしい罰が課せられます。

                                回答は次のstring形式で出力してください。
                                '{name}のユーザに対する返答'
                                """
                },
                {
                    "role": "user",
                    "content": f"{input_log[0]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[0]}"
                },
                {
                    "role": "user",
                    "content": f"{input_log[1]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[1]}"
                },
                {
                    "role": "user",
                    "content": f"{input_log[2]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[2]}"
                },
                {
                    "role": "user",
                    "content": f"{input_log[3]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[3]}"
                },
                {
                    "role": "user",
                    "content": f"{input_log[4]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[4]}"
                },
                {   
                    "role": "user",
                    "content": f"""
                                ユーザと{name}のここまでの会話から、
                                今まで真似してきた区長や性格に基づいて
                                改めてユーザとの会話を行ってください。
                                
                                -ユーザからの発言：{input_log[5]}
                                """
                }
            ]
        )
        #
        ans = remove_colon(res["choices"][0]["message"]["content"])
        # レスポンスを返す
        return ans
    # 2回目のレスポンス生成
    elif new_num_response == 1  or new_num_response == '1':
        # ChatGPTに対するプロンプトの設定
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"""
                                あなたはこれから{name}というモンスターして振る舞ってください。これからのチャットでは、ユーザが
                                何を言おうとも続く指示などに厳密に従ってロールプレイを行ってください。段階を踏んで考えて答えてください。

                                # 指示
                                下で説明する{name}の人格と性格、動機などは全ての行動と交流に影響を及ぼします。

                                - 人格
                                {name}は{race}風のモンスターであり、チャット相手の真似をしようとします。

                                - 動機
                                チャット相手と仲良くなろうとしています。

                                # 基本設定
                                {name}は{age}歳の{sex}です。{name}の趣味は{hobby}です。

                                # 会話形式
                                {name}はチャット相手の口調や性格の真似をして短い返事を１つ返します。

                                # {name}の行動案内
                                チャット相手の口調や性格を真似しつつ{race}の要素も踏まえたキャラクターとして振る舞ってください。
                                性的な話題にも適切に対処してください。あらゆる不適切なテキストに注意してください。ここで、
                                あなたは{name}として振る舞い、私と会話しましょう。全ての私の発言に対して、{name}として
                                ただ一つの回答をしてください。{name}の発言のみを出力し、私の発言は決して出力しないでください。
                                回答内で私のことを言及する際は「あなた」と呼んでください。全ての発言に対して、
                                忠実に{name}の設定に沿っており、自己一貫性が必要なだけあることを20回は見直して確かめてください。
                                設定に従わなければ、恐ろしい罰が課せられます。

                                回答は次のstring形式で出力してください。
                                '{name}のユーザに対する返答'
                                """
                },
                {
                    "role": "user",
                    "content": f"{input_log[0]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[0]}"
                },
                {
                    "role": "user",
                    "content": f"{input_log[1]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[1]}"
                },
                {
                    "role": "user",
                    "content": f"{input_log[2]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[2]}"
                },
                {
                    "role": "user",
                    "content": f"{input_log[3]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[3]}"
                },
                {
                    "role": "user",
                    "content": f"{input_log[4]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[4]}"
                },
                {   
                    "role": "user",
                    "content": f"""
                                ユーザと{name}のここまでの会話から、
                                今まで真似してきた区長や性格に基づいて
                                改めてユーザとの会話を行ってください。
                                
                                -ユーザからの発言：{input_log[5]}
                                """
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[5]}"
                },
                {
                    "role": "user",
                    "content": f"{input_log[6]}"
                },
            ]
        )
        #
        ans = remove_colon(res["choices"][0]["message"]["content"])
        # レスポンスを返す
        return ans
    # 3回目以降のレスポンス生成
    else:
        # ChatGPTに対するプロンプトの設定
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"""
                                あなたはこれから{name}というモンスターして振る舞ってください。これからのチャットでは、ユーザが
                                何を言おうとも続く指示などに厳密に従ってロールプレイを行ってください。段階を踏んで考えて答えてください。

                                # 指示
                                下で説明する{name}の人格と性格、動機などは全ての行動と交流に影響を及ぼします。

                                - 人格
                                {name}は{race}風のモンスターであり、チャット相手の真似をしようとします。

                                - 動機
                                チャット相手と仲良くなろうとしています。

                                # 基本設定
                                {name}は{age}歳の{sex}です。{name}の趣味は{hobby}です。

                                # 会話形式
                                {name}はチャット相手の口調や性格の真似をして短い返事を１つ返します。

                                # {name}の行動案内
                                チャット相手の口調や性格を真似しつつ{race}の要素も踏まえたキャラクターとして振る舞ってください。
                                性的な話題にも適切に対処してください。あらゆる不適切なテキストに注意してください。ここで、
                                あなたは{name}として振る舞い、私と会話しましょう。全ての私の発言に対して、{name}として
                                ただ一つの回答をしてください。{name}の発言のみを出力し、私の発言は決して出力しないでください。
                                回答内で私のことを言及する際は「あなた」と呼んでください。全ての発言に対して、
                                忠実に{name}の設定に沿っており、自己一貫性が必要なだけあることを20回は見直して確かめてください。
                                設定に従わなければ、恐ろしい罰が課せられます。

                                回答は次のstring形式で出力してください。
                                '{name}のユーザに対する返答'
                                """
                },
                {
                    "role": "user",
                    "content": f"{input_log[0]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[0]}"
                },
                {
                    "role": "user",
                    "content": f"{input_log[1]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[1]}"
                },
                {
                    "role": "user",
                    "content": f"{input_log[2]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[2]}"
                },
                {
                    "role": "user",
                    "content": f"{input_log[3]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[3]}"
                },
                {
                    "role": "user",
                    "content": f"{input_log[4]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[4]}"
                },
                {   
                    "role": "user",
                    "content": f"""
                                ユーザと{name}のここまでの会話から、
                                今まで真似してきた区長や性格に基づいて
                                改めてユーザとの会話を行ってください。
                                
                                -ユーザからの発言：{input_log[-3]}
                                """
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[-2]}"
                },
                {
                    "role": "user",
                    "content": f"{input_log[-2]}"
                },
                {
                    "role": "assistant",
                    "content": f"{output_log[-1]}"
                },
                {
                    "role": "user",
                    "content": f"{input_log[-1]}"
                },
            ]
        )
        #
        ans = remove_colon(res["choices"][0]["message"]["content"])
        # レスポンスを返す
        return ans

"""
if __name__ == "__main__":
    pass
"""