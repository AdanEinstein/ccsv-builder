from components import *


def select_dataframes():

    if 'xlsx' in st.session_state:
        xlsx: pd.ExcelFile = st.session_state["xlsx"]
        st.divider()
        with st.form("form_sheets"):
            st.markdown(
                body='''
    ##### Planilhas:
    '''
            )
            sheets = st.multiselect(
                label="Planilhas",
                placeholder="Selecione quais planilhas serão mescladas",
                options=xlsx.sheet_names,
                key="sheets"
            )

            submitted_sheets = st.form_submit_button("Confirmar")
            if submitted_sheets:
                if len(sheets) == 0:
                    st.error("Nenhuma planilha foi selecionada")
                    st.stop()
                
                dataframes = [pd.read_excel(xlsx, sheet_name=sheet, dtype=str) for sheet in sheets]

                st.toast(
                    body='Planilhas selecionadas!',
                    icon='✅'
                )
                
                st.session_state["dataframes"] = dataframes
