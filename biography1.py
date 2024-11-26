import streamlit as st

# Set the title of the page
st.title("My Biography Blog :sunflower:")

st.image('pic.jpg', caption='This is me!', width=200)

# Add a subtitle for the introduction section
st.subheader("Introduction")

# Add content for the introduction section
st.write("""
Welcome to my biography blog! My name is Liza Reil Agad, and I am a third year irregular student of Surigao del Norte State University. 
In this blog, I will share a little bit about my life, achievements, and future aspirations. I hope you enjoy reading my journey!
""")

# Add a subtitle for the achievements section
st.subheader("Achievements")

# Add content for the achievements section
st.write("""
- I graduated with a degree in [Your Degree].
- I have worked with [Company/Organization] as a [Position].
- I published my first book/article on [Topic].
- I have been recognized for my contributions in [Industry/Field].
- I have a passion for [Hobby/Interest].
""")

# Add a subtitle for the future aspirations section
st.subheader("Future Aspirations")

# Add content for future aspirations
st.write("""
In the coming years, I aim to:
- Expand my knowledge in [Field/Subject].
- Collaborate with professionals in [Industry].
- Write more about my experiences and lessons learned.
- Continue to inspire others through my work.
""")

# Add a subtitle for the contact section
st.subheader("Contact Me")

# Add a contact form using Streamlit's forms feature
with st.form(key='contact_form'):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    
    submit_button = st.form_submit_button("Send Message")
    
    if submit_button:
        st.write(f"Thank you {name} for reaching out! I'll get back to you soon.")
        st.write(f"Message: {message}")
        st.write(f"We'll contact you at {email}.")

# Optional: Add a small footer or additional section
st.markdown("---")
st.write("This is a simple biography blog built using Streamlit. All content is fictional and for demonstration purposes.")
