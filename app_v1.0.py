import streamlit as st
from services.llm_service import ask_ai

st.set_page_config(
    page_title="Enterprise AI Advisor",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Enterprise AI Advisor")

st.subheader("Helping CIOs Build AI Strategy")

st.write("Welcome Swadesh!")

st.markdown("---")

st.markdown("### Choose a module")

col1, col2 = st.columns(2)

with col1:
    st.button("📊 AI Readiness Assessment")
    st.button("💰 ROI Calculator")
    st.button("🤖 IT Support Agent")

with col2:
    st.button("📚 Knowledge Assistant")
    st.button("🗺 AI Roadmap")
    st.button("💡 AI Use Cases")

st.header("Ask Enterprise AI Advisor")

question = st.text_input("Ask any AI or IT Strategy question")

if st.button("Ask AI"):

    st.write("✅ Ask AI button clicked")

    if question:

        st.write("✅ Calling ask_ai()...")

        answer = ask_ai(question)

        st.write("✅ Response received")

        st.markdown("### Enterprise AI Advisor")

        st.write(answer)
