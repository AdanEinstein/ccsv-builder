import streamlit as st

st.set_page_config(
    page_title="Sobre",
    page_icon="⚙️",
    layout="wide"
)

with st.container(border=True):
    st.markdown(
        body=f'''
# :violet[Objetivo]
> #### **Transformar qualquer excel num CSV**

'''
    )
    st.page_link(
        page="https://www.linkedin.com/in/adaneinstein", 
        label="Desenvolvido por **:violet[Adan Einstein]**",
        icon="✈️"
    )