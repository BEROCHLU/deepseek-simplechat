#!/usr/bin/env python
import os
import sys
from datetime import datetime
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

# 環境変数からAPIキーを取得
API_KEY = os.environ.get("DEEPSEEK_API_KEY")
client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")
console = Console()

# 会話の初期コンテキスト
conversation = [
    {"role": "system", "content": "You are a helpful assistant"},
]

api_params = {
    "model": "deepseek-reasoner",  # deepseek-chat | deepseek-reasoner
    "messages": conversation,
    "temperature": 1.3,
    "max_tokens": 8192,
    # "reasoning_effort": "medium",
}

while True:
    # ユーザーからの入力を取得
    user_input = input("User: ")
    if not user_input:
        sys.exit()

    # ::を質問とファイルパスの区切りとする
    args = user_input.split("::")

    # 最初の引数を質問として扱う
    user_question = args[0].strip()
    file_contents = ""

    # 2つ目の引数があればファイルパスとして処理
    if len(args) >= 2:
        file_path = args[1].strip()
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                file_contents = file.read()
            console.print(f"[bold blue]Completed loading the file: '{file_path}'[/bold blue]")
        except Exception as e:
            console.print(f"[bold red]{e}[/bold red]")
            sys.exit()

    # AIの応答を会話履歴に追加
    if file_contents:
        conversation.append({"role": "user", "content": f"{user_question} :: {file_contents}"})
    else:
        conversation.append({"role": "user", "content": user_question})

    # API 呼び出し（タイムアウトや例外に備えエラーハンドリング）
    try:
        response = client.chat.completions.create(**api_params)
        # API からの応答を取得
        assistant_reply = response.choices[0].message.content

        console.print("[bold green]Assistant:[/bold green]")
        console.print(Markdown(assistant_reply))
        console.print("\n")

        conversation.append({"role": "assistant", "content": assistant_reply})
    except Exception as e:
        console.print(f"[bold red]Error occurred: {e}[/bold red]\n")
        break

# 会話履歴と（オプションで）読み込んだファイルの内容をファイルへ保存
save_dir = "./history"
os.makedirs(save_dir, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
history_file = os.path.join(save_dir, f"{api_params['model']}_{timestamp}.md")

try:
    with open(history_file, "w", encoding="utf-8") as f:
        # 会話履歴の出力
        for msg in conversation:
            f.write(f'{msg["role"].capitalize()}: {msg["content"]}\n\n')
    console.print(f"[bold blue]Conversation history saved to {history_file}[/bold blue]")
except Exception as e:
    console.print(f"[bold red]Failed to save conversation history: {e}[/bold red]")
