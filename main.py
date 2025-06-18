import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Emil Aghjayev")
    content = """
    Emil Aghjayev is an experienced Product Manager with over 8 years in digital product development across banking, insurance, government, and iGaming sectors. Currently serving as a Product Owner at Kapital Bank, Emil leads the development of innovative lending products, including BNPL and Credit Lines, as part of the bank’s Ecosystem Products squad. He previously played a key role in transforming lottery and instant win games at Azerlotereya and has held impactful positions at Pasha Insurance, ABB Bank, and the Innovation and Digital Development Agency. Emil holds multiple certifications including PSPO III, PSM III, PAL, and PMI-ACP, and is passionate about mentoring aspiring product managers and driving digital innovation through customer-centric design and data-driven decision-making.
    """
    st.info(content)