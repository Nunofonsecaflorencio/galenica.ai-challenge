import streamlit as st


from llm import Recommender

ai = Recommender()
 
st.title("Discover Your Next Favorite Show or Movie!")
st.text("Get personalized recommendations based on your tastes. Discover movies and TV shows you'll love, effortlessly.")
st.write("")

with st.form("my_form", border=False):
    
    user_input = st.text_input("Enter a title, actor, genre, or plot keywords...", placeholder="eg. Movies and shows with Christopher Nolan style")
    submit = st.form_submit_button("Find Recommendations", type='primary')
    st.write("")
    
    if submit:
        if not user_input.strip():
            st.error("Type some something.")
        else:
            
            with st.spinner('Wait for it...'):
                movies, tv_shows = ai.recommend(user_input.strip())
            
            # Display Movies in a Table
            st.subheader("Movies")
            st.table(movies)

            # Display TV Shows in a Table
            st.subheader("TV Shows")
            st.table(tv_shows)
            

