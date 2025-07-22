import streamlit as st
import google.generativeai as genai

# Gemini APIキーの設定
api_key = st.secrets["GEMINI_API_KEY"]

# Gemini APIの設定
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash-lite')

# Streamlit UI
st.title("レシピ提案アプリ 🍳")

ingredients = st.text_input("使う食材を入力してください（例：卵、トマト、チーズ）")
servings = st.number_input("何人分のレシピが必要ですか？", min_value=1, max_value=10, value=2)
cuisine_type = st.selectbox("レシピの種類を選んでください", ["指定なし", "和食", "洋食", "中華", "イタリアン", "韓国料理"])

if st.button("レシピを提案してもらう"):
    if ingredients:
        cuisine_text = f"{cuisine_type}の" if cuisine_type != "指定なし" else ""
        prompt = f"""
        以下の食材を使って、日本語で{cuisine_text}家庭的なレシピを1つ提案してください。
        食材: {ingredients}
        {servings}人分の分量でお願いします。

        レシピには以下を含めてください：
        - 料理名
        - 材料一覧（{servings}人分）
        - 調理手順
        - 所要時間
        - 難易度
        """
        response = model.generate_content(prompt)
        st.markdown("### 📝 提案されたレシピ")
        st.write(response.text)
    else:
        st.warning("食材を入力してください。")

