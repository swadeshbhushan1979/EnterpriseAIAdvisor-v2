from services.assumption_review_service import review_assumptions
from services.roi_ai_services import generate_business_case
from calculators.roi_engine import calculate_roi
import streamlit as st

st.set_page_config(
    page_title="Enterprise AI ROI Builder",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Enterprise AI ROI Builder")

st.markdown("""
Estimate the business value of Enterprise AI initiatives.

Complete this assessment to generate:

- ROI %
- Annual Savings
- Payback Period
- Executive Business Case
""")

st.divider()

# -----------------------------
# Company Information
# -----------------------------

st.header("Organization Information")

company_info = st.session_state.get(
    "company_info",
    {}
)

company_name = st.text_input(
    "Company Name",
    value=company_info.get("company", "")
)

country = st.text_input(
    "Country",
    value=company_info.get("country", "")
)

industry = st.selectbox(
    "Industry",
    [
        "Manufacturing",
        "Healthcare",
        "Retail",
        "Banking",
        "Insurance",
        "Technology",
        "Telecom",
        "Government",
        "Other"
    ]
)



# country = st.text_input(
#     "Country",
#     value=company_info.get("country", "")
# )

employees = st.number_input(
    "Total Employees",
    min_value=1,
    value=1000
)

annual_revenue = st.number_input(
    "Annual Revenue ($)",
    min_value=0,
    value=10000000
)

st.divider()

st.header("Select AI Use Case")

use_case_list = [
    "IT Service Desk Copilot",
    "HR AI Assistant",
    "Finance Invoice Automation",
    "Customer Support AI Agent",
    "Procurement Assistant",
    "Sales Copilot",
    "Knowledge Management Assistant",
    "Software Development Copilot",
    "Legal Document Assistant",
    "Executive AI Assistant"
]

default_use_case = st.session_state.get(
    "selected_use_case",
    use_case_list[0]
)

if default_use_case not in use_case_list:
    default_use_case = use_case_list[0]

use_case = st.selectbox(
    "AI Use Case",
    use_case_list,
    index=use_case_list.index(default_use_case)
)

st.success(f"Selected Use Case : {use_case}")

st.divider()

# ==========================================
# Dynamic Question Engine
# ==========================================

USE_CASES = {

    "IT Service Desk Copilot": [

        ("Number of Service Desk Agents", 20),
        ("Tickets per Month", 10000),
        ("Average Resolution Time (Minutes)", 25),
        ("Average Annual Salary per Agent ($)", 50000),
        ("% Tickets AI Can Resolve", 40)

    ],

    "HR AI Assistant": [

        ("Number of HR Employees", 25),
        ("Employee Queries per Month", 4000),
        ("Average Query Handling Time (Minutes)", 12),
        ("Average Annual Salary ($)", 60000),
        ("% Queries AI Can Resolve", 50)

    ],

    "Finance Invoice Automation": [

        ("Finance Employees", 15),
        ("Invoices per Month", 12000),
        ("Average Invoice Processing Time (Minutes)", 8),
        ("Average Annual Salary ($)", 70000),
        ("% Invoice Automation", 70)

    ],

    "Customer Support AI Agent": [

        ("Support Agents", 60),
        ("Support Tickets per Month", 18000),
        ("Average Handle Time (Minutes)", 10),
        ("Average Annual Salary ($)", 45000),
        ("% AI Resolution", 45)

    ],

    "Procurement Assistant": [

        ("Procurement Employees", 20),
        ("Purchase Orders per Month", 5000),
        ("Average Review Time (Minutes)", 20),
        ("Average Annual Salary ($)", 65000),
        ("% Automation", 35)

    ],

    "Sales Copilot": [

        ("Sales Representatives", 100),
        ("Average Annual Revenue per Rep ($)", 1000000),
        ("Hours Spent on Administration Per Day", 2),
        ("Average Annual Salary ($)", 85000),
        ("% Productivity Improvement", 30)

    ],

    "Knowledge Management Assistant": [

        ("Knowledge Workers", 500),
        ("Average Search Time Per Day (Minutes)", 45),
        ("Working Days Per Year", 220),
        ("Average Annual Salary ($)", 90000),
        ("% Search Time Reduction", 60)

    ],

    "Software Development Copilot": [

        ("Developers", 150),
        ("Coding Hours Per Day", 5),
        ("Average Annual Salary ($)", 120000),
        ("% Productivity Improvement", 30),
        ("% Bug Reduction", 20)

    ],

    "Legal Document Assistant": [

        ("Legal Professionals", 15),
        ("Contracts Per Month", 800),
        ("Average Review Time (Minutes)", 60),
        ("Average Annual Salary ($)", 150000),
        ("% Review Automation", 40)

    ],

    "Executive AI Assistant": [

        ("Executives", 30),
        ("Meetings Per Week", 18),
        ("Hours on Email Per Day", 2),
        ("Hours on Reporting Per Week", 8),
        ("% Productivity Improvement", 25)

    ]

}

st.header("Business Inputs")

answers = {}

for question, default in USE_CASES[use_case]:

    answers[question] = st.number_input(

        question,

        value=float(default)

    )

st.success("Business inputs captured successfully.")

st.divider()

# ==========================================
# AI Investment
# ==========================================

st.header("AI Investment")

solution_type = st.selectbox(

    "Solution Type",

    [
        "SaaS Solution",
        "Internal Development",
        "Implementation Partner"
    ]
)

software_cost = st.number_input(

    "Annual Software / Subscription Cost ($)",

    min_value=0.0,

    value=50000.0,

    step=1000.0

)

implementation_cost = st.number_input(

    "Implementation Cost ($)",

    min_value=0.0,

    value=100000.0,

    step=5000.0

)

training_cost = st.number_input(

    "Training Cost ($)",

    min_value=0.0,

    value=20000.0,

    step=1000.0

)

infrastructure_cost = st.number_input(

    "Infrastructure Cost ($)",

    min_value=0.0,

    value=30000.0,

    step=1000.0

)

annual_support = st.number_input(

    "Annual Support & Maintenance ($)",

    min_value=0.0,

    value=25000.0,

    step=1000.0

)

st.success("Investment information captured successfully.")

st.divider()

st.header("ROI Calculation")


calculate = st.button(
    "Calculate ROI",
    type="primary",
    use_container_width=True
)

if calculate or "selected_use_case" in st.session_state:

    # ---------------------------------------
    # Total Investment
    # ---------------------------------------

    total_investment = (

        software_cost

        + implementation_cost

        + training_cost

        + infrastructure_cost

        + annual_support

    )

    # ---------------------------------------
    # Estimate Hours Saved
    # ---------------------------------------

    # annual_salary = 50000

    # for key in answers.keys():

    #     if "Salary" in key:

    #         annual_salary = answers[key]

    # hourly_cost = annual_salary / 220 / 8

    # hours_saved = 0


    # # if use_case == "IT Service Desk Copilot":

    # #     tickets = answers["Tickets per Month"]

    # #     resolution = answers["Average Resolution Time (Minutes)"]

    # #     automation = answers["% Tickets AI Can Resolve"]

    # #     hours_saved = (

    # #         tickets

    # #         * 12

    # #         * (resolution / 60)

    # #         * (automation / 100)

    # #     )

    # # elif use_case == "HR AI Assistant":

    # #     queries = answers["Employee Queries per Month"]

    # #     handling = answers["Average Query Handling Time (Minutes)"]

    # #     automation = answers["% Queries AI Can Resolve"]

    # #     hours_saved = (

    # #         queries

    # #         * 12

    # #         * (handling / 60)

    # #         * (automation / 100)

    # #     )

    # # elif use_case == "Finance Invoice Automation":

    # #     invoices = answers["Invoices per Month"]

    # #     processing = answers["Average Invoice Processing Time (Minutes)"]

    # #     automation = answers["% Invoice Automation"]

    # #     hours_saved = (

    # #         invoices

    # #         * 12

    # #         * (processing / 60)

    # #         * (automation / 100)

    # #     )

    # # else:

    # #     hours_saved = 5000

    # # productivity_savings = hours_saved * hourly_cost

    # # revenue_gain = annual_revenue * 0.01


    roi_result = calculate_roi(
    use_case,
    answers
    )


    # st.write("ROI Result Type:", type(roi_result))
    # st.write("ROI Result:", roi_result)


    hours_saved = roi_result["hours_saved"]
    productivity_savings = roi_result["salary_savings"]
    revenue_gain = roi_result["revenue_gain"]
    operational_savings = productivity_savings * 0.20
    
    annual_benefit = (

        productivity_savings

        + revenue_gain

        + operational_savings

        )



    roi = (

        (

            annual_benefit

            - total_investment

        )

        / total_investment

        ) * 100

    payback = total_investment / annual_benefit

    st.session_state["roi_results"] = {

        "investment": total_investment,

        "benefit": annual_benefit,

        "roi": roi,

        "payback": payback,

        "hours_saved": hours_saved,

        "salary_savings": productivity_savings

        }
    st.session_state["selected_use_case"] = use_case

    company_data = {

    "company_profile": {
        "Company": company_name,
        "Industry": industry,
        "Country": country,
        "Employees": employees,
        "Annual Revenue": annual_revenue
    },

    # run_calculation = (
    #     "selected_use_case" in st.session_state
    #     )

    "selected_use_case": use_case,

    "business_inputs": answers,

    "investment": {
        "Software": software_cost,
        "Implementation": implementation_cost,
        "Training": training_cost,
        "Infrastructure": infrastructure_cost,
        "Support": annual_support,
        "Total Investment": total_investment
    },

    "calculated_results": {

        "Hours Saved": hours_saved,

        "Salary Savings": productivity_savings,

        "Revenue Gain": revenue_gain,

        "Annual Benefit": annual_benefit,

        "ROI": roi,

        "Payback": payback

    }

    }

    st.session_state["company_data"] = company_data

    #added assumption review step
    try:
        with st.spinner("🧐 Reviewing business assumptions..."):
            assumption_review = review_assumptions(company_data)
            st.session_state["assumption_review"] = assumption_review
    except Exception as e:
        st.warning(f"Assumption Review skipped: {e}")
    #calling OpenAI or LLM
    try:
        with st.spinner("🤖 Generating Executive Business Case..."):
            business_case = generate_business_case(company_data)
            st.session_state["business_case"] = business_case
    except Exception as e:
        st.warning(f"Business Case generation skipped: {e}")

    st.success("ROI calculation completed successfully.")

# ==========================================
# Executive ROI Dashboard
# ==========================================

if "roi_results" in st.session_state:

    results = st.session_state["roi_results"]
    

    st.divider()

    st.header("📊 Executive ROI Dashboard")

#     tab1, tab2, tab3, tab4 = st.tabs([
#     "📊 Financial Summary",
#     "🤖 AI Business Case",
#     "⚠ Risks & Assumptions",
#     "🗺 90-Day Roadmap"
# ]   )

    investment = results["investment"]
    benefit = results["benefit"]
    roi = results["roi"]
    payback = results["payback"]
    hours_saved = results["hours_saved"]
    salary_savings = results["salary_savings"]

    # with tab1:
    # ---------------------------------
    # KPI Cards
    # ---------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "💰 Total Investment",
            f"${investment:,.0f}"
        )

    with col2:
        st.metric(
            "📈 Annual Benefit",
            f"${benefit:,.0f}"
        )

    with col3:
        st.metric(
            "📊 ROI",
            f"{roi:.1f}%"
        )

    with col4:
        st.metric(
            "⏳ Payback",
            f"{payback:.2f} Years"
        )

    st.divider()

    # ---------------------------------
    # Additional KPIs
    # ---------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Business Impact")

        st.metric(
            "Annual Hours Saved",
            f"{hours_saved:,.0f}"
        )

        st.metric(
            "Salary Savings",
            f"${salary_savings:,.0f}"
        )

    with col2:

        st.subheader("Investment Summary")

        st.metric(
            "Annual Revenue",
            f"${annual_revenue:,.0f}"
        )

        st.metric(
            "Employees",
            f"{employees:,}"
        )

    st.divider()

    # ---------------------------------
    # Executive Summary
    # ---------------------------------

    st.subheader("Executive Summary")

    st.info(
        f"""
The proposed **{use_case}** initiative for **{company_name}**
is expected to generate an estimated **ROI of {roi:.1f}%**.

The estimated annual business benefit is
**${benefit:,.0f}** against a total investment of
**${investment:,.0f}**.

The investment is expected to recover within
approximately **{payback:.2f} years**.

The initiative is estimated to save
**{hours_saved:,.0f} hours** annually,
resulting in productivity savings of
**${salary_savings:,.0f}**.
"""
    )

    st.divider()

    # ---------------------------------
    # Recommendation
    # ---------------------------------

    st.subheader("Recommendation")

    if roi >= 150:

        st.success("""
### ✅ Highly Recommended

This initiative demonstrates an excellent financial return.

Recommended for immediate implementation.
""")

    elif roi >= 75:

        st.success("""
### ✅ Recommended

The initiative shows a positive business case.

Proceed after validating assumptions.
""")

    elif roi >= 0:

        st.warning("""
### ⚠ Requires Further Analysis

The initiative appears viable but assumptions
should be reviewed before investment.
""")

    else:

        st.error("""
### ❌ Not Financially Justified

Current assumptions do not support the investment.

Reassess costs or expected benefits.
""")

    st.divider()

    # ---------------------------------
    # Financial Breakdown
    # ---------------------------------

    st.subheader("Financial Breakdown")

    financial_data = {
        "Metric": [
            "Total Investment",
            "Annual Benefit",
            "Salary Savings",
            "Annual Hours Saved",
            "Payback (Years)",
            "ROI (%)"
        ],
        "Value": [
            f"${investment:,.0f}",
            f"${benefit:,.0f}",
            f"${salary_savings:,.0f}",
            f"{hours_saved:,.0f}",
            f"{payback:.2f}",
            f"{roi:.1f}%"
        ]
    }

    st.table(financial_data)

    st.divider()

    # ---------------------------------
    # Next Steps
    # ---------------------------------
    
    st.header("🤖 AI Executive Business Case")

    if "business_case" in st.session_state:

        report = st.session_state["business_case"]

        st.subheader("Executive Summary")
        st.write(report["executive_summary"])

        st.subheader("Strategic Alignment")
        st.write(report["strategic_alignment"])

        st.subheader("Business Value")
        st.write(report["business_value"])

        st.subheader("Top Benefits")
        for benefit in report["top_benefits"]:
            st.success(benefit)

        st.subheader("Top Risks")
        for risk in report["top_risks"]:
            st.warning(risk)

        st.subheader("Critical Assumptions")
        for item in report["critical_assumptions"]:
            st.info(item)

        st.subheader("Recommended KPIs")
        for item in report["recommended_kpis"]:
            st.write("•", item)

        st.subheader("90-Day Roadmap")

        st.success("Month 1")
        st.write(report["roadmap"]["month1"])

        st.success("Month 2")
        st.write(report["roadmap"]["month2"])

        st.success("Month 3")
        st.write(report["roadmap"]["month3"])

        st.subheader("Executive Recommendation")
        st.write(report["executive_recommendation"])

    #Assumption Review Section
    st.divider()
    st.subheader(" 🤖 AI Assumption Review")

    review = st.session_state.get("assumption_review")

    if review:

        st.metric("Confidence", review["confidence"])

        st.write("### Unrealistic Assumptions")

        for item in review["unrealistic_assumptions"]:
            st.warning(item)

        st.write("### Missing Assumptions")

        for item in review["missing_assumptions"]:
            st.info(item)

        st.write("### Recommendations")

        for item in review["recommendations"]:
            st.success(item)

    else:
        st.info("Assumption Review is not available.")
    
    st.divider()

    # ---------------------------------
    # Reset
    # ---------------------------------

    if st.button("🔄 Calculate Another ROI"):

        st.session_state.pop("roi_results")

        st.rerun()

    st.session_state["roi_complete"] = True

st.divider()

if st.button(
    "➡ Continue to AI Roadmap",
    type="primary",
    use_container_width=True
):
    st.switch_page("pages/4_AI_Roadmap.py")

#-------------------------------------

# import streamlit as st

# st.title("💰 AI ROI Calculator")

# fte = st.number_input("Current FTEs", 1)

# salary = st.number_input("Average Annual Salary")

# automation = st.slider(
#     "Expected Automation %",
#     0,
#     100,
#     30
# )

# st.button("Calculate ROI")