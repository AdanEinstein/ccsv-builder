from components import *

def uploader():
    with st.form("uploader"):
        uploaded_file = st.file_uploader(
            label="Selecione a planilha com os dados",
            accept_multiple_files=False,
            type=['xlsx']
        )

        submitted_file = st.form_submit_button("Confirmar")

        if submitted_file:
            if uploaded_file is None:
                st.error(f"Nenhum arquivo foi selecionado")
                st.stop()

            with st.spinner("Lendo o arquivo..."):
                xlsx = pd.ExcelFile(uploaded_file)
                st.session_state["xlsx"] = xlsx
            
            st.toast(
                body='Arquivo selecionado!',
                icon='✅'
            )

@st.cache_data
def convert_df(df: pd.DataFrame):
    return df.to_csv(index=False).encode("utf-8")