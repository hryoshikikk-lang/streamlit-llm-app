import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

def get_llm_response(input_text, expert_type):
    if expert_type == "転職活動についての専門家":
        system_message = "あなたは転職活動についての専門家です。"
    else:
        system_message = "あなたは副業についての専門家です。"

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

st.title("LLMを活用した専門家アプリ")

input_text = st.text_input("質問を入力してください")
expert_type = st.radio(
    "専門家を選択",
    ("転職活動についての専門家", "副業についての専門家")
)

if st.button("送信"):
    st.write(get_llm_response(input_text, expert_type))
