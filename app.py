
import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit Page Settings
st.set_page_config(
    page_title="Shaina's AI Learning Buddy",
    page_icon="🎓"
)

st.markdown("""
<style>

/* Background */
.main {
    background: linear-gradient(135deg, #0f172a, #111827);
}

/* Hero Section */
.hero{
    text-align:center;
    padding:40px 20px 50px 20px;
}

/* Main Heading */
.hero h1{
    font-size:78px;
    font-weight:800;
    margin-bottom:10px;
    background: linear-gradient(90deg,#4F8BF9,#7C3AED,#00E5FF);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    text-shadow:0px 0px 30px rgba(79,139,249,0.35);
    letter-spacing:-2px;
}

/* Subtitle */
.hero p{
    font-size:24px;
    color:#d1d5db;
    margin-bottom:12px;
}

/* Small Description */
.hero span{
    font-size:17px;
    color:#9ca3af;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">

<h1 style="font-size:90px; font-weight:900;">🧠 AI Learning Buddy</h1>

<p>Your Personal AI Tutor</p>

<span>
Learn • Practice • Quiz • Interview Prep • Summarize
</span>

</div>
""", unsafe_allow_html=True)

st.title("🎓 Shaina's AI Learning Buddy")

st.write("Your Personal AI Tutor for Learning Anything!")

# User Input
topic = st.text_input("Enter a Topic")

# Activity Selection
option = st.selectbox(
    "Choose Activity",
    [
        "📖 Explain Concept",
        "💡 Real-Life Example",
        "📝 Generate Quiz",
        "⚖ Advantages & Disadvantages",
        "🎤 Interview Questions",
        "📄 Summary",
        "🤖 Ask Anything"
    ]
)

# Generate Button
if st.button("🚀 Generate AI Response", use_container_width=True):

    if topic == "":
        st.warning("Please enter a topic.")

    else:

        if option == "📖 Explain Concept":
            prompt = f"""
            Explain {topic} in simple language.
            Use headings and bullet points.
            """

        elif option == "💡 Real-Life Example":
            prompt = f"""
            Give 3 simple real-life examples of {topic}.
            """

        elif option == "📝 Generate Quiz":
            prompt = f"""
            Create 5 MCQs on {topic}.
            Give answers at the end.
            """

        elif option == "⚖ Advantages & Disadvantages":
            prompt = f"""
            List advantages and disadvantages of {topic}.
            """

        elif option == "🎤 Interview Questions":
            prompt = f"""
            Generate 10 interview questions on {topic} with answers.
            """

        elif option == "📄 Summary":
            prompt = f"""
            Summarize {topic} in less than 200 words.
            """

        else:
            prompt = topic

        with st.spinner("🤖 Gemini is thinking..."):
          response = model.generate_content(prompt)

        with st.container(border=True):
          st.subheader("📚 AI Response")
          st.write(response.text)
