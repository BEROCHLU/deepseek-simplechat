#!/usr/bin/env python

import os
from datetime import datetime
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
    "temperature": 1.3,  # Not supported by deepseek-reasoner; probably fixed to 1.0.
    "max_tokens": 8192,  # openAIのmax_completion_tokensに近いのか？
    # "reasoning_effort": "medium",  # The parameter for deepseek-reasoner will be available soon. low | medium | high
}

while True:
    # ユーザーからの入力を取得
    user_input = input("User: ").strip()
    if not user_input:
        break

    # ユーザーのメッセージを会話履歴に追加
    conversation.append({"role": "user", "content": user_input})

    # 時々、タイムアウトが起きるのでエラーハンドリングを追加
    try:
        response = client.chat.completions.create(**api_params)

        # API より応答を取得
        assistant_reply = response.choices[0].message.content

        # rich を使って Markdown としてterminalに描画
        console.print("[bold green]Assistant:[/bold green]")
        console.print(Markdown(assistant_reply))
        console.print("\n")  # 改行で区切り

        # AI応答を会話履歴に追加
        conversation.append({"role": "assistant", "content": assistant_reply})

    except Exception as e:
        console.print(f"[bold red]Error occurred: {e}[/bold red]\n")
        break

# ここで会話履歴をテキストファイルに保存
save_dir = "./history"  # 保存先ディレクトリを指定し、存在しない場合は作成
os.makedirs(save_dir, exist_ok=True)

# タイムスタンプ取得（例: 20231020_153045）
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
history_file = os.path.join(save_dir, f"{api_params['model']}_{timestamp}.md")

try:
    with open(history_file, "w", encoding="utf-8") as f:
        for msg in conversation:
            # role と content を分かりやすい形式で保存
            f.write(f'{msg["role"].capitalize()}: {msg["content"]}\n\n')
    console.print(f"[bold blue]Conversation history saved to {history_file}[/bold blue]")
except Exception as e:
    console.print(f"[bold red]Failed to save conversation history: {e}[/bold red]")
