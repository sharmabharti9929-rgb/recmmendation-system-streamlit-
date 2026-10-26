import streamlit as st
import random

st.set_page_config(
    page_title="AI Movie Recommendation",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* ---------------- Main Background ---------------- */

.stApp{
    background: #0F1117;
    color: white;
}

/* ---------------- Sidebar ---------------- */

[data-testid="stSidebar"]{
    background: #161B22;
}

[data-testid="stSidebar"] *{
    color: white;
}

/* ---------------- Padding ---------------- */

.block-container{
    padding-top:2rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* ---------------- Title ---------------- */

.title{
    font-size:48px;
    font-weight:bold;
    text-align:center;
    color:#FF4B4B;
}

.subtitle{
    text-align:center;
    font-size:22px;
    color:#C9D1D9;
    margin-bottom:30px;
}

/* ---------------- Cards ---------------- */

.card{
    background:#1E222D;
    border-radius:15px;
    padding:25px;
    color:white;
    border:1px solid #30363D;
    transition:0.3s;
    box-shadow:0px 5px 15px rgba(0,0,0,.4);
    height:220px;
}

.card:hover{
    transform:translateY(-8px);
    border:1px solid #FF4B4B;
}

/* ---------------- Buttons ---------------- */

.stButton>button{
    background:#E50914;
    color:white;
    border:none;
    border-radius:10px;
    height:48px;
    font-size:16px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#B20710;
    color:white;
}

/* ---------------- Select Box ---------------- */

div[data-baseweb="select"]{
    background:#1E222D;
    color:white;
    border-radius:10px;
}

/* ---------------- Input Box ---------------- */

.stTextInput input{
    background:#1E222D;
    color:white;
    border-radius:10px;
}

/* ---------------- Metric Cards ---------------- */

[data-testid="metric-container"]{
    background:#1E222D;
    border-radius:12px;
    padding:15px;
    border:1px solid #30363D;
}

/* ---------------- Info Box ---------------- */

[data-testid="stAlert"]{
    background:#1E222D;
    color:white;
}

/* ---------------- Footer ---------------- */

.footer{
    text-align:center;
    color:#8B949E;
    margin-top:40px;
    font-size:15px;
}

hr{
    border:1px solid #30363D;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🎬 AI Powered Movie Recommendation System</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Discover your next favorite movie using Machine Learning.</div>", unsafe_allow_html=True)

st.divider()

col1, col2, col3, col4 = st.columns(4)

col1.metric(" Movies", "5000+")
col2.metric(" Genres", "20+")
col3.metric("ML Model", "Cosine Similarity")
col4.metric("Accuracy", "High")

st.write("")

st.subheader("✨ Features")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class='card'>
    <h3>Smart Recommendation</h3>
    <p>Get personalized movie recommendations using Machine Learning.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='card'>
    <h3>Dataset</h3>
    <p>Built using TMDB 5000 Movies Dataset with metadata and genres.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='card'>
    <h3>⚡ Fast Search</h3>
    <p>Instant recommendations powered by cosine similarity.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
quotes = [
    "Movies touch our hearts and awaken our vision.",
    "Cinema is a matter of what's in the frame.",
    "Every great movie starts with a great story.",
    "Life is like a movie. Write your own ending.",
    "Keep calm and watch movies."
]

st.info(random.choice(quotes))

st.write("")

st.subheader("Technologies Used")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.success("Python")
tech2.success("Streamlit")
tech3.success("Pandas")
tech4.success("Scikit-Learn")

st.write("")

st.subheader(" Quick Actions")

b1, b2 = st.columns(2)

with b1:
    if st.button("Start Recommending"):
        st.success("Open the Recommendation page from the sidebar.")

with b2:
    if st.button(" View Dataset"):
        st.info("Open the Dataset page from the sidebar.")

st.divider()

st.markdown("""
<div class='footer'>
Made with using Streamlit <br><br>
<b>Developer:</b> Bharti Sharma
</div>
""", unsafe_allow_html=True)