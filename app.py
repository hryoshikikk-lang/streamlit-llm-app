from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# LLMからの回答を取得する関数
def get_llm_response(input_text, expert_type):
    if expert_type == "転職活動についての専門家":
        system_message = "あなたは転職活動についての専門家です。"
    elif expert_type == "副業についての専門家":
        system_message = "あなたは副業についての専門家です。"
    else:
        system_message = ""

    chat = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text)
    ]

    response = chat.invoke(messages)
    return response.content

# Streamlitアプリ
st.title("LLMを活用した専門家アプリ")

st.write(
    "このアプリでは、転職活動や副業についての専門家に質問することができます。\n"
    "質問を入力し、専門家の種類を選択してください。"
)

input_text = st.text_input("質問を入力してください:")
expert_type = st.radio(
    "専門家の種類を選択してください:",
    ("転職活動についての専門家", "副業についての専門家")
)

if st.button("送信"):
    if input_text.strip():
        response = get_llm_response(input_text, expert_type)
        st.subheader("回答")
        st.write(response)
    else:
        st.error("質問を入力してください！")