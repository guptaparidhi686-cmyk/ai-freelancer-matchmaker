import streamlit as st
import ollama

# -------------------------------
# Config
# -------------------------------
MODEL = "gemma4:31b-cloud"

st.set_page_config(page_title="AI Freelancer Matchmaker", page_icon="🤖")

st.title("🤖 AI Client–Freelancer Matchmaker")
st.write("Find the best freelancer using AI 🚀")

# -------------------------------
# Sample Freelancer Data
# -------------------------------
freelancers = [
    {
        "name": "Rahul",
        "skills": ["python", "machine learning", "nlp"],
        "experience": 3,
        "rate": 20
    },
    {
        "name": "Ananya",
        "skills": ["web development", "react", "node"],
        "experience": 2,
        "rate": 15
    },
    {
        "name": "Arjun",
        "skills": ["data science", "python", "deep learning"],
        "experience": 4,
        "rate": 25
    }
]

# -------------------------------
# User Input
# -------------------------------
client_req = st.text_area(
    "📝 Enter Client Requirement",
    placeholder="Example: I need a Python ML developer under $30/hr"
)

# -------------------------------
# AI Matching Function
# -------------------------------
def match_freelancer(client_requirement):
    prompt = f"""
You are an intelligent AI freelancer matchmaker.

Client Requirement:
{client_requirement}

Freelancers:
{freelancers}

Task:
1. Analyze client needs
2. Compare all freelancers
3. Select BEST match

Return format:
Name:
Reason:
"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']


# -------------------------------
# Button Action
# -------------------------------
if st.button("🔍 Find Best Freelancer"):
    if client_req.strip() == "":
        st.warning("Please enter a requirement!")
    else:
        with st.spinner("🤖 AI is analyzing..."):
            result = match_freelancer(client_req)

        st.success("✅ Best Match Found!")
        st.markdown(result)

# -------------------------------
# Show Freelancers
# -------------------------------
st.subheader("👨‍💻 Available Freelancers")

for f in freelancers:
    st.write(f"**Name:** {f['name']}")
    st.write(f"Skills: {', '.join(f['skills'])}")
    st.write(f"Experience: {f['experience']} years")
    st.write(f"Rate: ${f['rate']}/hr")
    st.write("---")