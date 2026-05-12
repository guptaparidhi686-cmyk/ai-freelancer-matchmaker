import ollama as ol

sample_freelancers = [
    {
        "name": "Aisha Khan",
        "skills": ["Python", "Django", "FastAPI", "SQL"],
        "hourly_rate": 45,
        "location": "Lahore, PK",
        "availability": "Full-time",
        "summary": "Backend engineer with 7 years of SaaS and fintech experience."
    },
    {
        "name": "Miguel Santos",
        "skills": ["React", "TypeScript", "Node.js", "UI/UX"],
        "hourly_rate": 50,
        "location": "Lisbon, PT",
        "availability": "Part-time",
        "summary": "Frontend specialist building responsive web apps and design systems."
    },
    {
        "name": "Priya Sharma",
        "skills": ["Copywriting", "SEO", "Content Strategy", "WordPress"],
        "hourly_rate": 35,
        "location": "Bangalore, IN",
        "availability": "Available",
        "summary": "Content marketing writer with 5 years of experience in tech and B2B."
    },
    {
        "name": "Noah Thompson",
        "skills": ["Data Science", "Machine Learning", "PyTorch", "NLP"],
        "hourly_rate": 70,
        "location": "Austin, TX",
        "availability": "Consulting",
        "summary": "AI consultant delivering production-ready ML pipelines and analytics."
    }
]

sample_data_text = (
    "Freelancer database:\n"
    "1. Aisha Khan — Python, Django, FastAPI, SQL; Rate $45/hr; Lahore, PK; Full-time; Backend engineer with 7 years of SaaS and fintech experience.\n"
    "2. Miguel Santos — React, TypeScript, Node.js, UI/UX; Rate $50/hr; Lisbon, PT; Part-time; Frontend specialist building responsive web apps and design systems.\n"
    "3. Priya Sharma — Copywriting, SEO, Content Strategy, WordPress; Rate $35/hr; Bangalore, IN; Available; Content marketing writer with 5 years of experience in tech and B2B.\n"
    "4. Noah Thompson — Data Science, Machine Learning, PyTorch, NLP; Rate $70/hr; Austin, TX; Consulting; AI consultant delivering production-ready ML pipelines and analytics.\n"
)

system_prompt = (
    "You are a freelancer AI assistant. Use the provided freelancer database to answer user requests accurately. "
    "When a user asks for a freelancer, recommend the best match from the sample data and explain why. "
    "If the user asks for pricing, availability, skills, or location, answer based on the sample freelancers."
)


def create_chat(user_query: str):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "system", "content": sample_data_text},
        {"role": "user", "content": user_query}
    ]

    return ol.chat(
        model="gemma4:31b-cloud",
        messages=messages,
        stream=True
    )


def print_sample_data():
    print("Sample Freelancer Data:\n")
    for freelancer in sample_freelancers:
        print(f"- {freelancer['name']}: {', '.join(freelancer['skills'])} | ${freelancer['hourly_rate']}/hr | {freelancer['location']} | {freelancer['availability']}")
        print(f"  {freelancer['summary']}\n")


if __name__ == "__main__":
    print_sample_data()
    user_query = input("\nAsk for a freelancer or describe your project: ").strip()

    if not user_query:
        print("No query provided. Exiting.")
    else:
        print("\nAssistant response:\n")
        chat = create_chat(user_query)
        for chunk in chat:
            print(chunk, end="", flush=True)
        print()
    