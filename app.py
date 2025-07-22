# app.py
import streamlit as st
import google.generativeai as genai

# Gemini APIキーの設定
genai.configure(GEMINI_API_KYE="AIzaSyDrVm4jKIc806ElZepC5gPCzEMIUKaOMtk")

# モデルの準備
model = genai.GenerativeModel("gemini-pro")

# Streamlit UI
st.title("冷蔵庫の中身でレシピ提案アプリ 🍳")

ingredients = st.text_input("冷蔵庫にある食材を入力してください（例：卵、トマト、チーズ）")

if st.button("レシピを提案してもらう"):
    if ingredients:
        prompt = f"""
        以下の食材を使って、日本語で家庭的なレシピを1つ提案してください。
        食材: {ingredients}
        レシピには以下を含めてください：
        - 料理名
        - 材料一覧
        - 調理手順
        - 所要時間
        - 難易度
        """
        response = model.generate_content(prompt)
        st.markdown("### 📝 提案されたレシピ")
        st.write(response.text)
    else:
        st.warning("食材を入力してください。")

