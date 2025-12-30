import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# 1. ページの設定（タブのタイトルなど）
st.set_page_config(page_title="Gemini Chat App", page_icon="🤖")

# 2. APIキーの読み込み
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 3. タイトルを表示
st.title("🤖 私だけのGeminiチャット")
st.write("何か質問してみてください！")

# 4. 入力フォームを作る
user_input = st.text_input("ここに入力してEnterを押してください", key="input")

# 5. 送信されたらGeminiを呼ぶ
if user_input:
    if not api_key:
        st.error("エラー: APIキーが設定されていません")
    else:
        # クライアントの準備
        client = genai.Client(api_key=api_key)
        
        try:
            # AIに考え中...と表示させる
            with st.spinner("Geminiが考え中..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=user_input
                )
            
            # 結果を表示する
            st.success("回答が来ました！")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")