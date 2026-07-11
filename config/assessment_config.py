ASSESSMENT = [

    {
        "section": "Organization",
        "title": "Organization Profile",

        "questions": [

            {
                "id": "company",
                "label": "Company Name",
                "type": "text"
            },

            {
                "id": "industry",
                "label": "Industry",
                "type": "select",

                "options": [
                    "Manufacturing",
                    "Healthcare",
                    "Retail",
                    "Banking",
                    "Insurance",
                    "Technology"
                ]
            },

            {
                "id": "employees",
                "label": "Employees",
                "type": "select",

                "options": [
                    "1-100",
                    "100-500",
                    "500-1000",
                    "1000-5000",
                    "5000+"
                ]
            },

            {
                "id": "country",
                "label": "Country",
                "type": "text"
            }

        ]
    },

    {
        "section": "Business Strategy",
        "title": "Business Strategy",

        "questions": [

            {
                "id": "ai_strategy",

                "label": "AI Strategy",

                "type": "radio",

                "options": [
                    "No Strategy",
                    "Planning",
                    "Approved",
                    "Executing"
                ]
            },

            {
                "id": "executive_sponsorship",

                "label": "Executive Sponsorship",

                "type": "radio",

                "options": [
                    "None",
                    "CIO",
                    "Multiple Leaders",
                    "CEO Driven"
                ]
            },

            {
                "id": "budget",

                "label": "AI Budget",

                "type": "radio",

                "options": [
                    "None",
                    "Pilot",
                    "Department",
                    "Enterprise"
                ]
            }

        ]
    }

]
