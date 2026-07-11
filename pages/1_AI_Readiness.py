
import streamlit as st
from services.readiness_ai_service import generate_assessment
import json

st.set_page_config(page_title="AI Readiness Assessment", page_icon="📊", layout="wide")

if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "report" not in st.session_state:
    st.session_state.report = None

SECTIONS = [
{"title":"Organization Profile","fields":[("Company Name","text"),("Industry",["Manufacturing","Healthcare","Retail","Banking","Insurance","Technology"]),("Country",["India","USA","UK","Germany","Japan","Other"]),("Employees",["1-100","101-500","501-5000","5001-20000","20000+"]),("Annual Revenue",["< $10M","$10M-$100M","$100M-$1B",">$1B"]),("Primary Cloud Platform",["AWS","Azure","Google Cloud","Oracle Cloud","Hybrid","On-Prem"])]},
{"title":"Business Strategy","fields":[("AI Strategy",["None","Planning","Approved","Executing"]),("Executive Sponsorship",["None","CIO","Executive Committee","CEO"]),("AI Budget",["None","Pilot","Department","Enterprise"])]},
{"title":"Data Readiness","fields":[("Data Quality",["Poor","Average","Good","Excellent"]),("Data Governance",["None","Basic","Defined","Mature"]),("Analytics Maturity",["Excel","BI","Advanced Analytics","AI Driven"])]},
{"title":"Technology Readiness","fields":[("Cloud Maturity",["Legacy","Hybrid","Modern Cloud","AI Ready"]),("API Integration",["Poor","Average","Good","Excellent"]),("ERP Modernization",["Legacy","Partially Modern","Modern"])]},
{"title":"People & Change","fields":[("AI Skills",["None","Beginner","Intermediate","Advanced"]),("Change Readiness",["Low","Medium","High"])]},
{"title":"Governance & Risk","fields":[("Responsible AI",["None","Planning","Defined","Mature"]),("AI Risk Management",["None","Basic","Mature"])]},
{"title":"AI Vision","fields":[("Primary AI Objective",["Cost Reduction","Productivity","Customer Experience","Revenue Growth","Innovation"]),("Biggest Challenge",["Skills","Budget","Technology","Data","Governance","Executive Buy-in"])]}
]

total_steps=len(SECTIONS)+2
st.title("📊 Enterprise AI Readiness Assessment")
progress = min(st.session_state.step / (total_steps - 1), 1.0)
st.progress(progress)
st.caption(f"Step {st.session_state.step+1} of {total_steps}")

if st.session_state.step==0:
    st.markdown("### Welcome\nComplete this assessment to receive an executive AI readiness report.")
    if st.button("🚀 Start Assessment"):
        st.session_state.step=1
        st.rerun()
elif 1<=st.session_state.step<=len(SECTIONS):
    sec=SECTIONS[st.session_state.step-1]
    st.subheader(sec["title"])
    for label,control in sec["fields"]:
        if control=="text":
            st.session_state.answers[label]=st.text_input(label,value=st.session_state.answers.get(label,""))
        else:
            opts=control
            cur=st.session_state.answers.get(label,opts[0])
            if cur not in opts: cur=opts[0]
            st.session_state.answers[label]=st.selectbox(label,opts,index=opts.index(cur))
    c1,c2=st.columns(2)
    with c1:
        if st.session_state.step>1 and st.button("⬅ Previous"):
            st.session_state.step-=1
            st.rerun()
    with c2:
        if st.button("Next ➜"):
            st.session_state.step+=1
            st.rerun()
elif st.session_state.step==len(SECTIONS)+1:
    st.subheader("Review Assessment")
    for k,v in st.session_state.answers.items():
        st.write(f"**{k}:** {v}")
    c1,c2=st.columns(2)
    with c1:
        if st.button("⬅ Previous"):
            st.session_state.step-=1
            st.rerun()
    with c2:
        
        api_key = st.text_input(
            "OpenAI API Key",
            type="password"
        )
        if api_key:
            st.session_state["OPENAI_API_KEY"] = api_key

        if st.button("🚀 Generate Executive Report"):
            with st.spinner("Generating report..."):
                st.session_state.report=generate_assessment(st.session_state.answers)
                st.write(type(st.session_state.report))
                st.write(st.session_state.report)
                st.session_state.step+=1
                st.rerun()
else:
    #st.success("Executive Report")
    #st.markdown(st.session_state.report)
    if st.button("🔄 Start New Assessment"):
        st.session_state.step=0
        st.session_state.answers={}
        st.session_state.report=""
        st.rerun()
    
# ============================================================
# Display AI Readiness Assessment Report
# ============================================================


report = st.session_state.report

if report is not None and isinstance(report, dict):

    st.success("## 🎯 Enterprise AI Readiness Assessment")

    score = report["overall_score"]

    # -----------------------------
    # Executive Status
    # -----------------------------

    if score >= 80:

        st.success("🟢 AI Ready Organization")

    elif score >= 60:

        st.warning("🟡 AI Developing Organization")

    elif score >= 40:

        st.warning("🟠 AI Emerging Organization")

    else:

        st.error("🔴 AI Transformation Required")

    # -----------------------------
    # Progress Bar
    # -----------------------------

    st.progress(score / 100)

    st.write(f"### Overall Readiness Score: **{score}%**")

    # -----------------------------
    # Executive Metrics
    # -----------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.metric(

            "AI Readiness Score",

            f"{score}%"

        )

    with col2:

        st.metric(

            "AI Maturity",

            report["overall_level"]

        )

    st.divider()

    # -----------------------------
    # Strengths
    # -----------------------------

    st.subheader("✅ Organizational Strengths")

    for item in report["strengths"]:

        st.success(item)

    st.divider()

    # -----------------------------
    # Gaps
    # -----------------------------

    st.subheader("⚠️ Improvement Areas")

    for item in report["gaps"]:

        st.warning(item)

    st.divider()

    # -----------------------------
    # Recommendations
    # -----------------------------

    st.subheader("🚀 Executive Recommendations")

    for item in report["recommendations"]:

        st.info(item)

    report = st.session_state.report

    markdown = f"""
    # Enterprise AI Readiness Report

    ## Overall Score

    {report['overall_score']}

    ## Maturity

    {report['overall_level']}

    ## Strengths

    """

    for s in report["strengths"]:
        markdown += f"- {s}\n"

    markdown += "\n## Gaps\n"

    for g in report["gaps"]:
        markdown += f"- {g}\n"

    markdown += "\n## Recommendations\n"

    for r in report["recommendations"]:
        markdown += f"- {r}\n"

    st.download_button(
        "📥 Download Report",
        data=markdown,
        file_name="Enterprise_AI_Readiness_Report.md",
        mime="text/markdown"
    )