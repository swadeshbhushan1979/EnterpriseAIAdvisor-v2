import streamlit as st

from services.roadmap_ai_service import generate_roadmap
#from jira_mcp.client import create_task_sync

st.set_page_config(
    page_title="AI Roadmap",
    layout="wide"
)

st.title("🗺 Enterprise AI Transformation Roadmap")

if "company_data" not in st.session_state:

    st.error("Please complete ROI Business Case first.")

    st.stop()

company_data = st.session_state["company_data"]

roi_results = st.session_state.get("roi_results", {})

report = st.session_state["opportunities"]
opportunities = report["top_opportunities"]

selected_use_case = st.session_state.get(
    "selected_use_case",
    "Not Selected"
)

# -----------------------------------
# Assign Phases
# -----------------------------------

phase1 = []
phase2 = []
phase3 = []

for item in opportunities:

    score = item["priority_score"]

    if score >= 85:

        phase1.append(item)

    elif score >= 60:

        phase2.append(item)

    else:

        phase3.append(item)

roadmap_input = {

    "phase1":[x["use_case"] for x in phase1],

    "phase2":[x["use_case"] for x in phase2],

    "phase3":[x["use_case"] for x in phase3]

}

if "roadmap" not in st.session_state:

    with st.spinner("Generating roadmap..."):

        st.session_state["roadmap"] = generate_roadmap(
            roadmap_input
        )

roadmap = st.session_state["roadmap"]

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Selected Initiative",
        selected_use_case
    )

with col2:
    st.metric(
        "ROI",
        f'{roi_results["roi"]:.1f}%'
    )

with col3:
    st.metric(
        "Investment",
        f'${roi_results["investment"]:,.0f}'
    )

with col4:
    st.metric(
        "Payback",
        f'{roi_results["payback"]:.2f} Years'
    )

st.divider()

st.success(roadmap["executive_summary"])

st.divider()

col1,col2,col3 = st.columns(3)

with col1:

    st.subheader("🚀 Phase 1")
    st.caption("0-90 Days")

    st.info(roadmap["phase1_objective"])

    for item in phase1:

        st.success(item["use_case"])

with col2:

    st.subheader("⚙ Phase 2")
    st.caption("3-6 Months")

    st.info(roadmap["phase2_objective"])

    for item in phase2:

        st.info(item["use_case"])

with col3:

    st.subheader("🏆 Phase 3")
    st.caption("6-12 Months")

    st.info(roadmap["phase3_objective"])

    for item in phase3:

        st.warning(item["use_case"])

st.divider()

left,right = st.columns(2)

with left:

    st.subheader("⚠ Key Risks")

    for risk in roadmap["risks"]:

        st.write("•",risk)

with right:

    st.subheader("✅ Success Factors")

    for item in roadmap["success_factors"]:

        st.write("•",item)

st.divider()

if "roadmap" in st.session_state:

    if st.button(
        "➡ Continue to Knowledge Assessment",
        type="primary",
        use_container_width=True
    ):

        st.switch_page("pages/5_Knowledge_Assessment.py")

st.divider()
if st.button(
    "🚀 Create Jira Stories",
    use_container_width=True
):
    from jira_mcp.client import create_story_sync
    roadmap = st.session_state["roadmap"]

    created = []

    for phase in [

        "phase1",

        "phase2",

        "phase3"

    ]:

        for item in roadmap.get(phase, []):

            result = create_task_sync(

                item,

                "Generated automatically by Enterprise AI Advisor"

            )

            created.append(result)

    st.success("Stories created successfully.")

    st.write(created)        