from components import *


def select_columns():
    has_dataframes = 'dataframes' in st.session_state
    has_sheets = 'sheets' in st.session_state
    if has_dataframes and has_sheets:
        dataframes: list[pd.DataFrame] = st.session_state['dataframes']
        sheets: list[int | str] = st.session_state['sheets']
        st.divider()
        with st.form("columns_settings"):
            st.markdown(
                body='''
                    ##### Colunas:
                    '''
            )

            columns: dict[str, list[str]] = {}
            intersection_columns = set()
            for dataframe in dataframes:
                if len(intersection_columns) == 0:
                    intersection_columns = set(dataframe.columns)
                intersection_columns = intersection_columns & set(
                    dataframe.columns)

            intersection = st.selectbox(
                label="Intersecção",
                placeholder="Selecione as colunas de intersecções entre as planilhas",
                options=intersection_columns,
                key='intersection'
            )

            for i, dataframe in enumerate(dataframes):
                columns[sheets[i]] = st.multiselect(
                    label=f"Colunas da planilha ({sheets[i]})",
                    placeholder="Selecione quais colunas serão adicionadas no CSV final",
                    options=[
                        col for col in dataframe.columns if col != intersection],
                )

            submitted_columns = st.form_submit_button("Confirmar")

            if submitted_columns:
                for sheet, cols in columns.items():
                    if len(cols) == 0:
                        st.error(
                            f"Nenhuma coluna da planilha ({sheet}) foi selecionada")
                        st.stop()

                st.toast(
                    body='Colunas selecionadas!',
                    icon='✅'
                )

                st.session_state['columns'] = columns
