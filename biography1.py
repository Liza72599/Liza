import streamlit as st

st.title("My Biography :sunflower:")

st.image('pic.jpg', caption='About Myself!', width=200)

st.subheader("Introduction")

# Add content for the introduction section
st.write("""
Hello! My name is Liza Reil Agad, and I am a third year irregular student of Surigao del Norte State University. Taking the course of Bachelor of Science in Computer Engineering. 
In this blog, I will share a little bit about my journey, educational attainments, and hobbies. I hope you enjoy reading my journey!
""")
st.subheader("About Me")
st.write("""
- **Name:** Liza Reil Agad 
- **Gender:** Female
- **Age:** 25 years old
- **Permanent Address:** Prk. Sunflower, Gamut, Tago, Surigao del Sur
- **Current Address:** P-24, Sitio Looc, Brgy. Luna. Surigao City
- **Birthday:** July 25, 1999
- **Place of Birth:** Gamut, Tago, Surigao del Sur
""")
st.subheader("Educational Attainments")
st.write("""
- **Elementary:** Gamut Elementary School
- **High School:** Gamut National High School
- **Senior High School:** Gamut National High School
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
