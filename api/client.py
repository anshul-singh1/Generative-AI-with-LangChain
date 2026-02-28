import requests
import streamlit as st

st.set_page_config(page_title="Luxury AI Poet", page_icon="🖋️", layout="centered")

# Dark Luxury CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #000000, #1c1c1c);
    color: #f5f5f5;
    font-family: 'Georgia', serif;
}

# .lux-card {
#     background: rgba(255, 215, 0, 0.05);
#     padding: 50px;
#     border-radius: 25px;
#     backdrop-filter: blur(20px);
#     border: 1px solid rgba(255, 215, 0, 0.3);
#     box-shadow: 0 0 40px rgba(255, 215, 0, 0.15);
# }

h1 {
    text-align: center;
    color: gold;
    letter-spacing: 2px;
}

.stTextInput>div>div>input {
    background-color: rgba(255,255,255,0.08);
    color: gold;
    border: 1px solid rgba(255,215,0,0.4);
    border-radius: 12px;
}

.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #b8860b, #ffd700);
    color: black;
    font-weight: bold;
    border-radius: 12px;
    border: none;
    padding: 10px;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #ffd700, #b8860b);
}
</style>
""", unsafe_allow_html=True)

def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={'input': {'topic': input_text}}
    )
    return response.json()['output']

# UI
st.markdown("<div class='lux-card'>", unsafe_allow_html=True)

st.markdown("""
<h1 style="
    background: rgba(255, 215, 0, 0.05);
    padding: 50px;
    border-radius: 25px;
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 215, 0, 0.3);
    box-shadow: 0 0 40px rgba(255, 215, 0, 0.15);
    text-align: center;
    color: white;
    margin-bottom: 20px;
">
    🖋️ The Midnight Poem
</h1>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; opacity:0.8;'>Where words meet elegance.</p>", unsafe_allow_html=True)

topic = st.text_input("Whisper your theme...")

if st.button("Craft Masterpiece"):
    if topic:
        with st.spinner("Composing elegance..."):
            poem = get_ollama_response(topic)
        st.markdown("### ✨ Your Poem")
        st.write(poem)

st.markdown("</div>", unsafe_allow_html=True)



