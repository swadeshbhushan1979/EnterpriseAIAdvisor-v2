from utils.report_generator import generate_report
import streamlit as st

st.set_page_config(
    page_title="Executive Report",
    page_icon="📑",
    layout="wide"
)

st.title("📑 Executive AI Transformation Report")

# ----------------------------
# Session Check
# ----------------------------

required = [
    "company_data",
    "opportunities",
    "roi_results",
    "roadmap",
    "knowledge_assessment"
]

for item in required:
    if item not in st.session_state:
        st.error(f"{item} not found.")
        st.stop()

company = st.session_state["company_data"]
report = st.session_state["opportunities"]
roi = st.session_state["roi_results"]
roadmap = st.session_state["roadmap"]
knowledge = st.session_state["knowledge_assessment"]

profile = company["company_profile"]

# ----------------------------
# Company
# ----------------------------

st.header("🏢 Company Profile")

c1,c2,c3,c4 = st.columns(4)

c1.metric("Company", profile["Company"])
c2.metric("Industry", profile["Industry"])
c3.metric("Country", profile["Country"])
c4.metric("Employees", profile["Employees"])

st.divider()

# ----------------------------
# Executive KPIs
# ----------------------------

st.header("📊 Executive Summary")

k1,k2,k3,k4 = st.columns(4)

k1.metric(
    "AI Potential",
    report["overall_ai_potential"]
)

k2.metric(
    "ROI",
    f'{roi["roi"]:.1f}%'
)

k3.metric(
    "Payback",
    f'{roi["payback"]:.2f} Years'
)

k4.metric(
    "Knowledge Score",
    f'{knowledge["overall_score"]}%'
)

st.divider()

# ----------------------------
# Opportunities
# ----------------------------

st.header("🎯 Top AI Opportunities")

for item in report["top_opportunities"]:

    st.success(
        f'{item["use_case"]}  |  {item["priority"]}'
    )

st.divider()

# ----------------------------
# Roadmap
# ----------------------------

st.header("🗺 AI Roadmap")

st.info(roadmap["executive_summary"])

c1,c2,c3 = st.columns(3)

with c1:

    st.subheader("Phase 1")

    for item in roadmap["phase1"]:
        st.write("•", item)

with c2:

    st.subheader("Phase 2")

    for item in roadmap["phase2"]:
        st.write("•", item)

with c3:

    st.subheader("Phase 3")

    for item in roadmap["phase3"]:
        st.write("•", item)

st.divider()

# ----------------------------
# Investment
# ----------------------------

st.header("💰 Investment")

a,b,c = st.columns(3)

a.metric(
    "Investment",
    f'${roi["investment"]:,.0f}'
)

b.metric(
    "Annual Benefit",
    f'${roi["benefit"]:,.0f}'
)

c.metric(
    "Salary Savings",
    f'${roi["salary_savings"]:,.0f}'
)

st.divider()

# ----------------------------
# Knowledge
# ----------------------------

st.header("🎓 AI Readiness")

st.metric(
    "Overall Score",
    f'{knowledge["overall_score"]}%'
)

scores = knowledge["scores"]

for k,v in scores.items():

    st.progress(v/100)

    st.write(f"{k} : {v}%")

st.divider()

# ----------------------------
# Recommendation
# ----------------------------

st.header("🚀 Executive Recommendation")

st.success("""
1. Start with Phase-1 initiatives.

2. Allocate investment immediately.

3. Build AI CoE.

4. Review ROI quarterly.

5. Expand AI adoption across business functions.
""")

st.divider()

c1,c2 = st.columns(2)

with c1:

    report_data = {

        "company_data": company,

        "opportunities": report,

        "roi_results": roi,

        "roadmap": roadmap,

        "knowledge_assessment": knowledge

    }

    word_file = generate_report(report_data)

    st.download_button(

        "📄 Download Executive Report",

        data=word_file,

        file_name="Enterprise_AI_Report.docx",

        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",

        use_container_width=True

    )

#with c2:

#     ppt = generate_ppt(report_data)

#     st.download_button(

#         "📊 Download PowerPoint",

#         data=ppt,

#         file_name="Enterprise_AI_Transformation.pptx",

#         mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",

#         use_container_width=True

#     )

# import streamlit as st

# st.set_page_config(
#     page_title="Executive Dashboard",
#     page_icon="📊",
#     layout="wide"
# )

# st.title("📊 Executive AI Dashboard")

# # ------------------------
# # Company
# # ------------------------

# company = st.session_state.get("company_data", {})

# st.header("🏢 Company")

# if company:

#     profile = company.get("company_profile", {})

#     col1, col2 = st.columns(2)

#     with col1:
#         st.metric("Company", profile.get("Company", ""))
#         st.metric("Industry", profile.get("Industry", ""))
#         st.metric("Country", profile.get("Country", ""))

#     with col2:
#         st.metric("Employees", profile.get("Employees", ""))
#         st.metric("Revenue", profile.get("Annual Revenue", ""))
#         st.metric("AI Readiness", profile.get("AI Readiness", ""))

# # ------------------------
# # Opportunities
# # ------------------------

# st.header("🎯 AI Opportunities")

# if "opportunities" in st.session_state:

#     report = st.session_state["opportunities"]

#     st.metric(
#         "Overall AI Potential",
#         report["overall_ai_potential"]
#     )

#     st.dataframe(
#         report["top_opportunities"],
#         use_container_width=True
#     )

# # ------------------------
# # ROI
# # ------------------------

# st.header("💰 ROI")

# if "roi_results" in st.session_state:

#     roi = st.session_state["roi_results"]

#     c1, c2, c3, c4 = st.columns(4)

#     c1.metric(
#         "Investment",
#         f"${roi['investment']:,.0f}"
#     )

#     c2.metric(
#         "Benefit",
#         f"${roi['benefit']:,.0f}"
#     )

#     c3.metric(
#         "ROI",
#         f"{roi['roi']:.1f}%"
#     )

#     c4.metric(
#         "Payback",
#         f"{roi['payback']:.2f} yrs"
#     )

# # ------------------------
# # Roadmap
# # ------------------------

# st.header("🗺 AI Roadmap")

# if "roadmap" in st.session_state:

#     roadmap = st.session_state["roadmap"]

#     st.write(roadmap["executive_summary"])

#     st.success("Phase 1")

#     for item in roadmap["phase1"]:
#         st.write("•", item)

#     st.success("Phase 2")

#     for item in roadmap["phase2"]:
#         st.write("•", item)

#     st.success("Phase 3")

#     for item in roadmap["phase3"]:
#         st.write("•", item)

# # ------------------------
# # Knowledge Assessment
# # ------------------------

# st.header("🎓 Knowledge Assessment")

# if "knowledge_assessment" in st.session_state:

#     knowledge = st.session_state.get("knowledge_assessment", {})

#     if knowledge:

#         col1, col2 = st.columns(2)

#         with col1:
#             st.metric(
#                 "Knowledge Score",
#                 f'{knowledge["overall_score"]}%'
#             )

#         with col2:
#             st.metric(
#                 "AI Maturity",
#                 knowledge["maturity"]
#             )

#         st.subheader("Capability Scores")

#         chart = []

#         for k, v in knowledge["scores"].items():

#             chart.append({
#                 "Capability": k,
#                 "Score": v
#             })

#         st.dataframe(
#             chart,
#             use_container_width=True,
#             hide_index=True
#         )

# st.divider()

# st.success("✅ Enterprise AI Assessment Completed")