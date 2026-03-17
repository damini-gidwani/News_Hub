import streamlit as st
import requests

# 🔹 API Key
api = "506769e3bb7646f18ede5b2459a5d36a"

st.markdown("""
    <h1 style='text-align: center; color: #FF4B4B;'>NewsHub</h1>
    <p style='text-align: center; color: gray; font-size: 18px;'>
    Stay updated with the latest headlines from around the world </p>
    """, unsafe_allow_html=True)

# Step 1: Category selection
category = st.radio(
    "Select a news category:",
    ["General", "Sports", "Technology", "Entertainment", "Health", "Science"]
)

# Initialize session state variables
if "articles" not in st.session_state:
    st.session_state.articles = []
if "count" not in st.session_state:
    st.session_state.count = 5
if "current_category" not in st.session_state:
    st.session_state.current_category = ""

# Step 2: Fetch button
if st.button("Get News"):
    st.session_state.count = 5  # reset count every time we fetch new category
    st.session_state.current_category = category

    st.write(f"Fetching latest **{category}** news...")

    c = category.lower()
    url = f"https://newsapi.org/v2/top-headlines?category={c}&language=en&apiKey={api}"

    response = requests.get(url)
    if response.status_code != 200:
        st.error("❌ Unable to fetch news. Please check your internet or try again later.")
    else:
        data = response.json()
        st.session_state.articles = data.get('articles', [])

# Step 3: Display news (if already fetched)
if st.session_state.articles:
    articles = st.session_state.articles
    count = st.session_state.count

    st.success(f"Showing top {min(count, len(articles))} {category} headlines:")

    for article in articles[:count]:
        st.subheader(article.get('title') or "No title")
        st.write(article.get('description') or "No description available")
        st.markdown(f"[Read more]({article.get('url')})")
        st.divider()

    # Show more button
    if count < len(articles):
        if st.button("Show More"):
            st.session_state.count += 5
            st.rerun()
    else:
        st.info("You've reached the end of the list!")
else:
    st.info(" Select a category and click *Get News* to start!")
