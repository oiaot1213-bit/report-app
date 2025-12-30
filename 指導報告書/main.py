import os
from dotenv import load_dotenv
from google import genai  # 新しいライブラリ

# 1. 環境変数を読み込む
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 2. クライアントを作成（ここが新しくなりました）
client = genai.Client(api_key=api_key)

print("Geminiに質問中...")

try:
    # 3. コンテンツを生成する（書き方が少しシンプルになりました）
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Pythonを学ぶ初心者に、励ましの言葉を1文でください。"
    )

    # 結果を表示
    print("--- Geminiからの回答 ---")
    print(response.text)
    
except Exception as e:
    print(f"エラーが発生しました: {e}")