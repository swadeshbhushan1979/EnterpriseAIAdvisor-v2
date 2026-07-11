import streamlit as st

st.set_page_config(
    page_title="Knowledge Assessment",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Knowledge Assessment")

st.markdown(
"""
Evaluate your organization's AI skills and readiness.
"""
)

st.divider()

# -----------------------------------------
# Organization
# -----------------------------------------

company_data = st.session_state.get("company_data", {})

company = company_data.get("company_profile", {})

st.subheader("Organization")

col1, col2 = st.columns(2)

with col1:
    st.text_input(
        "Company",
        value=company.get("Company",""),
        disabled=True
    )

with col2:
    st.text_input(
        "Industry",
        value=company.get("Industry",""),
        disabled=True
    )

st.divider()

# -----------------------------------------
# Assessment
# -----------------------------------------

st.subheader("Knowledge Assessment")

questions = {

    "Executive AI Awareness":80,

    "AI Strategy":70,

    "Cloud Readiness":75,

    "Data Quality":65,

    "Data Governance":60,

    "AI Skills":55,

    "MLOps Capability":40,

    "Security & Compliance":70,

    "Change Management":65,

    "AI Adoption Culture":60

}

scores = {}

for question, default in questions.items():

    scores[question] = st.slider(

        question,

        0,

        100,

        default

    )

st.divider()

# -----------------------------------------
# Calculate
# -----------------------------------------

if st.button(

    "🎯 Calculate Knowledge Score",

    type="primary",

    use_container_width=True

):

    overall = round(sum(scores.values()) / len(scores),1)

    if overall >= 80:
        maturity = "Advanced"

    elif overall >= 65:
        maturity = "Intermediate"

    elif overall >= 50:
        maturity = "Developing"

    else:
        maturity = "Beginner"

    report = {

        "overall_score":overall,

        "maturity":maturity,

        "scores":scores

    }

    st.session_state["knowledge_assessment"] = report

# -----------------------------------------
# Dashboard
# -----------------------------------------

if "knowledge_assessment" in st.session_state:

    report = st.session_state["knowledge_assessment"]

    st.divider()

    st.header("📊 Assessment Result")

    col1,col2 = st.columns(2)

    with col1:

        st.metric(

            "Overall Score",

            f"{report['overall_score']}%"

        )

    with col2:

        st.metric(

            "AI Maturity",

            report["maturity"]

        )

    st.subheader("Capability Scores")

    chart=[]

    for k,v in report["scores"].items():

        chart.append({

            "Capability":k,

            "Score":v

        })

    st.dataframe(

        chart,

        use_container_width=True

    )

    st.divider()

    st.session_state["knowledge_complete"] = True

    if st.button(

        "➡ Continue to Investment Portfolio",

        type="primary",

        use_container_width=True

    ):

        st.switch_page(

            "pages/6_Investment_Portfolio.py"

        )