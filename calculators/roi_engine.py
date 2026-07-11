"""
Enterprise AI ROI Calculation Engine

All financial calculations are performed here.

The Streamlit UI should ONLY collect inputs and display outputs.
"""

from unittest import result


WORKING_DAYS = 220
WORKING_HOURS = 8


def hourly_rate(annual_salary):

    return annual_salary / WORKING_DAYS / WORKING_HOURS


def calculate_service_desk(inputs):

    tickets = inputs["Tickets per Month"]

    resolution = inputs["Average Resolution Time (Minutes)"]

    automation = inputs["% Tickets AI Can Resolve"]

    salary = inputs["Average Annual Salary per Agent ($)"]

    hours_saved = (
        tickets
        * 12
        * (resolution / 60)
        * (automation / 100)
    )

    salary_savings = hours_saved * hourly_rate(salary)

    return {
        "hours_saved": hours_saved,
        "salary_savings": salary_savings
    }


def calculate_hr(inputs):

    queries = inputs["Employee Queries per Month"]

    handling = inputs["Average Query Handling Time (Minutes)"]

    automation = inputs["% Queries AI Can Resolve"]

    salary = inputs["Average Annual Salary ($)"]

    hours_saved = (
        queries
        * 12
        * (handling / 60)
        * (automation / 100)
    )

    salary_savings = hours_saved * hourly_rate(salary)

    return {
        "hours_saved": hours_saved,
        "salary_savings": salary_savings
    }


def calculate_finance(inputs):

    invoices = inputs["Invoices per Month"]

    processing = inputs["Average Invoice Processing Time (Minutes)"]

    automation = inputs["% Invoice Automation"]

    salary = inputs["Average Annual Salary ($)"]

    hours_saved = (
        invoices
        * 12
        * (processing / 60)
        * (automation / 100)
    )

    salary_savings = hours_saved * hourly_rate(salary)

    return {
        "hours_saved": hours_saved,
        "salary_savings": salary_savings
    }

def calculate_customer_support(inputs):

    tickets = inputs["Support Tickets per Month"]

    handle = inputs["Average Handle Time (Minutes)"]

    automation = inputs["% AI Resolution"]

    salary = inputs["Average Annual Salary ($)"]

    hours_saved = (
        tickets
        * 12
        * (handle / 60)
        * (automation / 100)
    )

    salary_savings = hours_saved * hourly_rate(salary)

    return {
        "hours_saved": hours_saved,
        "salary_savings": salary_savings
    }


def calculate_procurement(inputs):

    po = inputs["Purchase Orders per Month"]

    review = inputs["Average Review Time (Minutes)"]

    automation = inputs["% Automation"]

    salary = inputs["Average Annual Salary ($)"]

    hours_saved = (
        po
        * 12
        * (review / 60)
        * (automation / 100)
    )

    salary_savings = hours_saved * hourly_rate(salary)

    return {
        "hours_saved": hours_saved,
        "salary_savings": salary_savings
    }


def calculate_sales(inputs):

    reps = inputs["Sales Representatives"]

    hours = inputs["Hours Spent on Administration Per Day"]

    improvement = inputs["% Productivity Improvement"]

    salary = inputs["Average Annual Salary ($)"]

    hours_saved = (
        reps
        * WORKING_DAYS
        * hours
        * (improvement / 100)
    )

    salary_savings = hours_saved * hourly_rate(salary)

    revenue_gain = (
        reps
        * inputs["Average Annual Revenue per Rep ($)"]
        * 0.02
    )

    return {
        "hours_saved": hours_saved,
        "salary_savings": salary_savings,
        "revenue_gain": revenue_gain
    }

def calculate_knowledge(inputs):

    workers = inputs["Knowledge Workers"]

    search_minutes = inputs["Average Search Time Per Day (Minutes)"]

    working_days = inputs["Working Days Per Year"]

    reduction = inputs["% Search Time Reduction"]

    salary = inputs["Average Annual Salary ($)"]

    hours_saved = (
        workers
        * working_days
        * (search_minutes / 60)
        * (reduction / 100)
    )

    salary_savings = hours_saved * hourly_rate(salary)

    return {
        "hours_saved": hours_saved,
        "salary_savings": salary_savings
    }

def calculate_developer(inputs):

    developers = inputs["Developers"]

    coding_hours = inputs["Coding Hours Per Day"]

    improvement = inputs["% Productivity Improvement"]

    salary = inputs["Average Annual Salary ($)"]

    bug_reduction = inputs["% Bug Reduction"]

    hours_saved = (
        developers
        * WORKING_DAYS
        * coding_hours
        * (improvement / 100)
    )

    salary_savings = hours_saved * hourly_rate(salary)

    operational_savings = salary_savings * (bug_reduction / 100)

    return {
        "hours_saved": hours_saved,
        "salary_savings": salary_savings,
        "operational_savings": operational_savings
    }

def calculate_legal(inputs):

    professionals = inputs["Legal Professionals"]

    contracts = inputs["Contracts Per Month"]

    review_time = inputs["Average Review Time (Minutes)"]

    automation = inputs["% Review Automation"]

    salary = inputs["Average Annual Salary ($)"]

    hours_saved = (
        contracts
        * 12
        * (review_time / 60)
        * (automation / 100)
    )

    salary_savings = hours_saved * hourly_rate(salary)

    return {
        "hours_saved": hours_saved,
        "salary_savings": salary_savings
    }


def calculate_executive(inputs):

    executives = inputs["Executives"]

    meetings = inputs["Meetings Per Week"]

    email_hours = inputs["Hours on Email Per Day"]

    reporting = inputs["Hours on Reporting Per Week"]

    improvement = inputs["% Productivity Improvement"]

    average_hours = (
        (meetings * 1)
        + (email_hours * 5)
        + reporting
    )

    hours_saved = (
        executives
        * 52
        * average_hours
        * (improvement / 100)
    )

    executive_salary = 250000

    salary_savings = hours_saved * hourly_rate(executive_salary)

    return {
        "hours_saved": hours_saved,
        "salary_savings": salary_savings
    }



ENGINES = {

    "IT Service Desk Copilot": calculate_service_desk,

    "HR AI Assistant": calculate_hr,

    "Finance Invoice Automation": calculate_finance,

    "Customer Support AI Agent": calculate_customer_support,

    "Procurement Assistant": calculate_procurement,

    "Sales Copilot": calculate_sales,

    "Knowledge Management Assistant": calculate_knowledge,

    "Software Development Copilot": calculate_developer,

    "Legal Document Assistant": calculate_legal,

    "Executive AI Assistant": calculate_executive

}


def calculate_roi(use_case, inputs):

    if use_case not in ENGINES:

        return {
            "hours_saved": 0,
            "salary_savings": 0,
            "revenue_gain": 0
        }

    result = ENGINES[use_case](inputs)

    defaults = {
    "hours_saved": 0,
    "salary_savings": 0,
    "revenue_gain": 0,
    "operational_savings": 0
    }

    defaults.update(result)

    return defaults

    # print("Use Case:", use_case)
    # print("Engine:", ENGINES[use_case])
    # print("Result:", result)
    # print("Result Type:", type(result))
    return result
