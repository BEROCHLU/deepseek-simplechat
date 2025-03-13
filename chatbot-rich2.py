#!/usr/bin/env python

import os
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

API_KEY = os.environ.get("OPENAI_API_KEY")  # 環境変数に設定したAPIキーを取得
MODEL = "o3-mini-2025-01-31"  # o3-mini-2025-01-31 | gpt-4o-mini-2024-07-18
TEMPERATURE = 0.7
REASONING_EFFORT = "medium"

client = OpenAI(api_key=API_KEY)

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

    api_params = {
        "model": MODEL,
        "messages": conversation,
        "temperature": TEMPERATURE,
        # max_completion_tokens=6080,  # max_tokensと違い出力トークンのみの制限。8000を超えると重くなる
    }

    # 推論モデルのみ設定
    if MODEL == "o3-mini-2025-01-31":
        api_params["temperature"] = 1.0
        api_params["reasoning_effort"] = REASONING_EFFORT

    response = client.chat.completions.create(**api_params)

    # API より応答を取得
    assistant_reply = response.choices[0].message.content

    # rich を使って Markdown としてterminalに描画
    console.print("[bold green]Assistant:[/bold green]")
    console.print(Markdown(assistant_reply))
    console.print("\n")  # 改行で区切り

    # 会話履歴に追加
    conversation.append({"role": "assistant", "content": assistant_reply})
