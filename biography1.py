import streamlit as st

# Set the title of the page
st.title("Liza Reil Agad's Biography Blog :sunflower:")

# Add a profile picture (Ensure to upload the image to GitHub or use a local path)
st.image('images/profile.jpg', caption='This is me!', width=250)  # Update the path if needed

# Introduction Section
st.header("Introduction")
st.write("""
Hi there! I'm **Liza Reil Agad**, a third-year student at Surigao del Norte State University. 
I'm passionate about technology, especially in areas like **data science** and **web development**.
In this blog, I’ll share a bit about my skills, projects, and how you can get in touch with me.
""")

# Skills Section
st.header("Skills")
st.write("""
- **Programming Languages**: Python, JavaScript
- **Data Science**: Pandas, NumPy, Scikit-learn
- **Web Development**: HTML, CSS, Flask
- **Other**: Git, SQL, Docker
""")

# Projects Section
st.header("My Projects")
st.write("""
Here are a few projects I've worked on:
1. **Personal Portfolio Website** - Built using HTML, CSS, and JavaScript.
2. **Data Analysis on COVID-19** - Analyzed COVID-19 trends using Python and Pandas.
3. **Machine Learning for Stock Price Prediction** - Created a model using Scikit-learn to predict stock prices.
""")

# Contact Section
st.header("Contact Me")
st.write("""
Feel free to reach out for any questions, project collaboration, or just to connect!
""")

# Contact Form
with st.form(key='contact_form'):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit_button = st.form_submit_button("Send Message")
    
    if submit_button:
        if not name or not email or not message:
            st.error("Please fill in all fields.")
        else:
            st.success(f"Thank you {name}! Your message has been sent successfully.")
            st.write(f"Subject: General Inquiry")
            st.write(f"Message: {message}")
            st.write(f"We’ll reach out to you at {email}.")

# Optional Footer
st.markdown("---")
st.write("This is a simple biography blog created with Streamlit. All content is for demonstration purposes.")
