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

api_params = {
    "model": "deepseek-reasoner",  # deepseek-chat | deepseek-reasoner
    "messages": conversation,
    "temperature": 0.7,  # openAIの推論モデルと違い、deepseek-reasonerは1.0にする必要がない
    "reasoning_effort": "low",  # low, medium, high, for reasoner parameter
    "max_completion_tokens": 99999,  # max_tokens(Deprecated)、出力トークンのみの制限
}

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
