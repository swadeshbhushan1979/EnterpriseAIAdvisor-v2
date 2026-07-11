import streamlit as st
import os

st.set_page_config(
    page_title="Enterprise AI Advisor",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Enterprise AI Advisor")

st.subheader("Enterprise AI Transformation Workflow")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.success("①\n\nAI Opportunity")

with col2:
    st.info("②\n\nROI Business Case")

with col3:
    st.warning("③\n\nAI Roadmap")

with col4:
    st.info("④\n\nKnowledge")

with col5:
    st.success("⑤\n\nExecutive Dashboard")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:

    st.metric("Modules", "5")

with col2:

    st.metric("AI Powered", "100%")

with col3:

    st.metric("Workflow", "Guided")

st.divider()

api_key = st.text_input(
    "OpenAI API Key",
    type="password"
)

if api_key:
    #os.environ["OPENAI_API_KEY"] = api_key
    st.session_state["OPENAI_API_KEY"] = api_key

if st.button(
    "🚀 Start AI Transformation Assessment",
    use_container_width=True,
    type="primary"
):
    st.switch_page("pages/2_AI_Opportunity.py")



# import streamlit as st

# st.set_page_config(
#     page_title="Enterprise AI Advisor",
#     page_icon="🤖",
#     layout="wide"
# )

# st.title("🤖 Enterprise AI Advisor")

# st.subheader("Helping CIOs Build AI Strategy")

# st.markdown("---")

# st.markdown("""
# ## Welcome

# Enterprise AI Advisor helps CIOs and IT Leaders:

# - Assess AI Readiness
# - Identify AI Opportunities
# - Calculate ROI
# - Build AI Roadmaps
# - Access Enterprise Knowledge
# - Resolve IT Support Issues

# 👈 Select a module from the sidebar to begin.
# """)