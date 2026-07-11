import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# import pandas as pd

from services.opportunity_ai_service import generate_opportunities

st.set_page_config(
    page_title="AI Opportunity Finder",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Enterprise AI Opportunity Finder")

# st.write(
#     "Identify and prioritize the best AI opportunities for your organization."
# )

st.divider()

st.header("Organization")

company = st.text_input("Company Name")

country = st.text_input(
    "Country",
    value="India"
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

st.header("Business Challenges")

challenges = st.multiselect(

    "Select the current business challenges",

    [

        "High Operational Cost",

        "Manual Processes",

        "Slow Customer Response",

        "Employee Productivity",

        "Knowledge Management",

        "Legacy Applications",

        "Data Quality Issues",

        "Compliance",

        "Cybersecurity",

        "Supply Chain Visibility",

        "Forecasting Accuracy",

        "Decision Making",

        "IT Support Backlog",

        "HR Service Delays",

        "Finance Processing Delays"

    ]

)

st.divider()

st.header("Strategic Objectives")

objectives = st.multiselect(

    "Select strategic objectives",

    [

        "Reduce Cost",

        "Increase Revenue",

        "Improve Customer Experience",

        "Improve Employee Experience",

        "Digital Transformation",

        "Business Growth",

        "Operational Excellence",

        "Innovation",

        "Risk Reduction",

        "Compliance"

    ]

)

st.divider()

st.header("Current Technology")

erp = st.selectbox(

    "ERP Platform",

    [

        "SAP",

        "Oracle",

        "Microsoft Dynamics",

        "Workday",

        "Salesforce",

        "Custom",

        "None"

    ]

)

cloud = st.selectbox(

    "Cloud Platform",

    [

        "AWS",

        "Azure",

        "Google Cloud",

        "Hybrid",

        "On-Premise"

    ]

)



employees = st.number_input(
    "Employees",
    min_value=1,
    value=1000
)

st.divider()

if st.button(
    "🎯 Discover AI Opportunities",
    use_container_width=True
):

    opportunity_data = {

        "company": company,

        "industry": industry,

        "employees": employees,

        "business_challenges": challenges,

        "strategic_objectives": objectives,

        "erp": erp,

        "cloud": cloud

    }

    with st.spinner("🤖 Identifying AI opportunities..."):

        opportunities = generate_opportunities(opportunity_data)

    st.session_state["opportunities"] = opportunities

    st.success("AI opportunities identified successfully.")

if "opportunities" in st.session_state:

    report = st.session_state["opportunities"]

    st.divider()

    st.header("🎯 AI Opportunity Dashboard")

    st.metric(
        "Overall AI Potential",
        report["overall_ai_potential"]
    )

    st.divider()

    st.subheader("Top AI Opportunities")

    for item in report["top_opportunities"]:

        with st.container(border=True):

            st.subheader(item["use_case"])

            # st.write(f"**Department:** {item['department']}")

            # st.write(f"**Business Value:** {item['business_value']}")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Priority", item["priority"])

            with col2:
                st.metric("Priority Score", f"{item['priority_score']}/100")

            with col3:
                st.metric("Impact", f"{item['business_impact']}/100")

            with col4:
                st.metric("Effort", f"{item['implementation_effort']}/100")

            # st.write(
            #     f"**Estimated ROI:** {item['estimated_roi']}"
            # )

            # st.write(
            #     f"**Suggested Phase:** {item['implementation_phase']}"
            # )

            # if st.button(
            #     f"💰 Calculate ROI - {item['use_case']}",
            #     key=item["use_case"]
            # ):

            #     st.session_state["selected_use_case"] = item["use_case"]
            #     st.switch_page("pages/2_ROI_Calculator.py")

    st.divider()
    st.subheader("⚡ Quick Wins")
    for item in report["quick_wins"]:
        st.success(item)
    
    st.divider()
    st.subheader("🚀 Strategic Initiatives")
    for item in report["strategic_initiatives"]:
        st.info(item)

    st.divider()

    st.subheader("📈 Impact vs Effort Matrix")

    matrix = pd.DataFrame(

        [

            {

                "Use Case": item["use_case"],

                "Impact": item["business_impact"],

                "Effort": item["implementation_effort"]

            }

            for item in report["top_opportunities"]

        ]

    )

    st.subheader("📋 Opportunity Prioritization")

    priority_data = []

    for item in report["top_opportunities"]:

        impact = item["business_impact"]
        effort = item["implementation_effort"]

        if impact >= 70 and effort <= 40:
            quadrant = "⭐⭐⭐ Quick Win"

        elif impact >= 70:
            quadrant = "🚀 Strategic Bet"

        elif effort <= 40:
            quadrant = "⚡ Fill-in"

        else:
            quadrant = "📅 Major Program"

        priority_data.append({

            "Use Case": item["use_case"],

            "Department": item["department"],

            "Impact": impact,

            "Effort": effort,

            "Priority": item["priority"],
            "Estimated ROI": item["estimated_roi"],
            "Quadrant": quadrant

        })

    st.dataframe(
        priority_data,
        use_container_width=True
    )

    st.divider()
    st.subheader("📈 Executive AI Opportunity Matrix")
    matrix = pd.DataFrame(priority_data)

    fig = go.Figure()

    # Quick Wins
    fig.add_shape(
        type="rect",
        x0=0,
        x1=50,
        y0=50,
        y1=100,
        fillcolor="lightgreen",
        opacity=0.20,
        line_width=0,
    )

    # Strategic Bets
    fig.add_shape(
        type="rect",
        x0=50,
        x1=100,
        y0=50,
        y1=100,
        fillcolor="lightblue",
        opacity=0.20,
        line_width=0,
    )

    # Fill-ins
    fig.add_shape(
        type="rect",
        x0=0,
        x1=50,
        y0=0,
        y1=50,
        fillcolor="khaki",
        opacity=0.20,
        line_width=0,
    )

    # Major Programs
    fig.add_shape(
        type="rect",
        x0=50,
        x1=100,
        y0=0,
        y1=50,
        fillcolor="lightcoral",
        opacity=0.20,
        line_width=0,
    )

    fig.add_vline(
        x=50,
        line_width=3,
        line_dash="dash",
    )

    fig.add_hline(
        y=50,
        line_width=3,
        line_dash="dash",
    )

    matrix["Short Name"] = matrix["Use Case"].apply(
        lambda x: "<br>".join(x.split()[:2]) if len(x) > 18 else x
    )

    fig.add_trace(

        go.Scatter(

            x=matrix["Effort"],

            y=matrix["Impact"],

            mode="markers+text",

            text=matrix["Short Name"],

            textposition="middle right",

            textfont=dict(
            color="black",
            size=11,
            family="Arial"
            ),

            marker=dict(
                size=18,
                color="#0B5ED7",
                line=dict(
                    color="white",
                    width=2
                )
            ),

            hovertemplate=
            "<b>%{customdata[0]}</b><br>"
            "Department: %{customdata[1]}<br>"
            "Priority: %{customdata[2]}<br>"
            "Impact: %{y}/100<br>"
            "Effort: %{x}/100<br>"
            "ROI: %{customdata[3]}<extra></extra>",
            customdata=matrix[
                [
                    "Use Case",
                    "Department",
                    "Priority",
                    "Estimated ROI"
                ]
            ],
            
        )   
    )
    fig.add_annotation(
        x=25,
        y=75,
        text="<b>⭐ Quick Wins</b>",
        showarrow=False,
        font=dict(
            size=16,
            color="black",
            family="Arial Black"
        )
    )

    fig.add_annotation(
        x=75,
        y=75,
        text="<b>🚀 Strategic Bets</b>",
        showarrow=False,
        font=dict(
            size=16,
            color="black",
            family="Arial Black"
        )
    )

    fig.add_annotation(
        x=25,
        y=25,
        text="<b>⚡ Fill-ins</b>",
        showarrow=False,
        font=dict(
            size=16,
            color="black",
            family="Arial Black"
        )
    )

    fig.add_annotation(
        x=75,
        y=25,
        text="<b>📅 Major Programs</b>",
        showarrow=False,
        font=dict(
            size=16,
            color="black",
            family="Arial Black"
        )
    )

    fig.update_layout(

        title=dict(
            text="Enterprise AI Opportunity Prioritization",
            font=dict(size=22, color="black")
        ),

        xaxis=dict(
            range=[0,100],
            title=dict(
                text="Implementation Effort",
                font=dict(size=16, color="black")
            ),
            tickfont=dict(size=12, color="black"),
            showgrid=False
        ),

        yaxis=dict(
            range=[0,100],
            title=dict(
                text="Business Impact",
                font=dict(size=16, color="black")
            ),
            tickfont=dict(size=12, color="black"),
            showgrid=False
        ),

        paper_bgcolor="white",

        plot_bgcolor="white",

        font=dict(
            color="black",
            size=13
        ),

        height=750,

        showlegend=False

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # st.write(priority_data)

    st.divider()
    st.subheader("📋 Recommended AI Initiatives")

    for item in report["top_opportunities"]:

        with st.container(border=True):

            col1, col2 = st.columns([4, 1])

            with col1:

                st.markdown(f"### {item['use_case']}")
                st.write(f"**Department:** {item['department']}")
                st.write(f"**Priority:** {item['priority']}")
                st.write(f"**Estimated ROI:** {item['estimated_roi']}")

            with col2:

                USE_CASE_MAPPING = {
                    "IT": "IT Service Desk Copilot",
                    "HR": "HR AI Assistant",
                    "Finance": "Finance Invoice Automation",
                    "Customer Service": "Customer Support AI Agent",
                    "Procurement": "Procurement Assistant",
                    "Sales": "Sales Copilot",
                    "Knowledge Management": "Knowledge Management Assistant",
                    "Software Engineering": "Software Development Copilot",
                    "Legal": "Legal Document Assistant",
                    "Executive": "Executive AI Assistant",
                    "Supply Chain": "Procurement Assistant"
                }
                # st.write(item)
                if st.button(
                    "💰 Calculate ROI",
                    key=f"roi_{item['use_case']}"
                ):

                    # Save selected use case
                    st.session_state["selected_use_case"] = item["roi_model"]

                    st.session_state["company_info"] = {

                        "company": company,

                        "industry": industry,

                        "country": country,

                        "employees": employees

                    }
                    # Go to ROI Calculator
                    st.switch_page("pages/3_ROI_Calculator.py")

st.divider()

# if "opportunities" in st.session_state:

#     if st.button(
#         "➡ Continue to ROI Business Case",
#         use_container_width=True,
#         type="primary"
#     ):
#         st.switch_page("pages/3_ROI_Calculator.py")

