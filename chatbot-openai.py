#!/usr/bin/env python

import os
import re
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

API_KEY = os.environ.get("OPENAI_API_KEY")  # 環境変数に設定したAPIキーを取得
MODEL = "o3-mini"  # gpt-4o-mini | o3-mini | gpt-4o-2024-11-20 | chatgpt-4o-latest
TEMPERATURE = 0.75
REASONING_EFFORT = "high"  # low | medium | high

client = OpenAI(api_key=API_KEY)

console = Console()

# 会話の初期コンテキストとして system メッセージを設定
conversation = [
    {"role": "system", "content": "You are a helpful assistant"},
]

api_params = {
    "model": MODEL,
    "messages": conversation,
    "temperature": TEMPERATURE,
    "max_completion_tokens": 16384,  # max_tokens(Deprecated)、出力トークンのみの制限
}

# 推論モデルのみ設定
if re.match(r"^o[1-9]-", MODEL):
    api_params["temperature"] = 1.0
    api_params["reasoning_effort"] = REASONING_EFFORT
    api_params["max_completion_tokens"] = 99999

while True:
    # ユーザーからの入力を取得
    user_input = input("User: ").strip()
    if not user_input:
        break

    # ユーザーのメッセージを会話履歴に追加
    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(**api_params)

    # API より応答を取得
    assistant_reply = response.choices[0].message.content

    # rich を使って Markdown としてterminalに描画
    console.print("[bold green]Assistant:[/bold green]")
    console.print(Markdown(assistant_reply))
    console.print("\n")  # 改行で区切り

    # AI応答を会話履歴に追加
    conversation.append({"role": "assistant", "content": assistant_reply})
