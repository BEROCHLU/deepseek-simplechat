#!/usr/bin/env python

import os
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

API_KEY = os.environ.get("DEEPSEEK_API_KEY")  # 環境変数に設定したAPIキーを取得

client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")

console = Console()

# 会話の初期コンテキストとして system メッセージを設定
conversation = [
    {"role": "system", "content": "You are a helpful assistant"},
]

while True:
    # ユーザーからの入力を取得
    user_input = input("User: ").strip()
    if not user_input:
        break

    # ユーザーのメッセージを会話履歴に追加
    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="deepseek-chat",  # deepseek-chat | deepseek-reasoner
        messages=conversation,
        stream=False,
        temperature=1.3,  # o3, o1と違いreasonerであっても1.0で固定する必要がない
        # max_completion_tokens=6080,  # max_tokensと違い出力トークンのみの制限。8000を超えると重くなる
    )

    # API より応答を取得
    assistant_reply = response.choices[0].message.content

    # rich を使って Markdown としてterminalに描画
    console.print("[bold green]Assistant:[/bold green]")
    console.print(Markdown(assistant_reply))
    console.print("\n")  # 改行で区切り

    # 会話履歴に追加
    conversation.append({"role": "assistant", "content": assistant_reply})
