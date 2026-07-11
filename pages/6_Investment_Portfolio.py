import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Investment Portfolio",
    page_icon="💼",
    layout="wide"
)

st.title("💼 AI Investment Portfolio")

# -----------------------------
# Validate Session
# -----------------------------

required = [
    "opportunities",
    "roi_results",
    "roadmap"
]

for item in required:
    if item not in st.session_state:
        st.error(f"{item} not available.")
        st.stop()

report = st.session_state["opportunities"]
roi = st.session_state["roi_results"]
roadmap = st.session_state["roadmap"]

opportunities = report["top_opportunities"]

# -----------------------------
# KPIs
# -----------------------------

st.subheader("Portfolio Summary")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "Investment",
    f"${roi['investment']:,.0f}"
)

c2.metric(
    "Benefit",
    f"${roi['benefit']:,.0f}"
)

c3.metric(
    "ROI",
    f"{roi['roi']:.1f}%"
)

c4.metric(
    "Payback",
    f"{roi['payback']:.2f} yrs"
)

c5.metric(
    "Initiatives",
    len(opportunities)
)

st.divider()

# -----------------------------
# Portfolio
# -----------------------------

rows = []

investment_per_project = roi["investment"] / len(opportunities)
benefit_per_project = roi["benefit"] / len(opportunities)

for item in opportunities:

    rows.append({

        "Initiative": item["use_case"],

        "Department": item["department"],

        "Priority": item["priority"],

        "ROI": item["estimated_roi"],

        "Phase": item["implementation_phase"],

        "Investment ($)": round(investment_per_project),

        "Benefit ($)": round(benefit_per_project)

    })

portfolio = pd.DataFrame(rows)

st.subheader("Investment Portfolio")

st.dataframe(
    portfolio,
    use_container_width=True,
    hide_index=True
)

st.divider()

# -----------------------------
# Investment by Department
# -----------------------------

dept = (
    portfolio
    .groupby("Department")["Investment ($)"]
    .sum()
)

st.subheader("Investment by Department")

st.bar_chart(dept)

st.divider()

# -----------------------------
# Phase Distribution
# -----------------------------

phase = (
    portfolio["Phase"]
    .value_counts()
)

st.subheader("Implementation Phases")

st.bar_chart(phase)

st.divider()

# -----------------------------
# Executive Recommendation
# -----------------------------

st.subheader("Executive Recommendation")

high = portfolio[
    portfolio["Priority"] == "High"
]

medium = portfolio[
    portfolio["Priority"] == "Medium"
]

low = portfolio[
    portfolio["Priority"] == "Low"
]

st.success("Invest Immediately")

for x in high["Initiative"]:
    st.write("•", x)

if len(medium):

    st.warning("Phase 2")

    for x in medium["Initiative"]:
        st.write("•", x)

if len(low):

    st.info("Later")

    for x in low["Initiative"]:
        st.write("•", x)

st.divider()

if st.button(
    "➡ Executive Report",
    type="primary",
    use_container_width=True
):
    st.switch_page(
        "pages/7_Executive_Dashboard.py"
    )