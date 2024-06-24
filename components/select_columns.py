from components import *


def select_columns():
    has_dataframes = 'dataframes' in st.session_state
    has_sheets = 'sheets' in st.session_state
    if has_dataframes and has_sheets:
        dataframes: list[pd.DataFrame] = st.session_state['dataframes']
        sheets: list[int | str] = st.session_state['sheets']
        st.divider()
        with st.form("settings_columns"):
            st.markdown(
                body='''
                    ##### Colunas:
                    '''
            )

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
                st.multiselect(
                    label=f"Colunas da planilha ({sheets[i]})",
                    placeholder="Selecione quais colunas serão adicionadas no CSV final",
                    options=[
                        col for col in dataframe.columns if col != intersection],
                    key=f'columns_{sheets[i]}'
                )

            submitted_columns = st.form_submit_button("Confirmar")

            if submitted_columns:
                has_columns = all([bool(len(v)) for k, v in st.session_state.items() if 'columns_' in k])
                if not has_columns:
                    st.error(
                        f"Não foi possível selecionar as colunas, Tente novamente")
                    st.stop()

                st.toast(
                    body='Colunas selecionadas!',
                    icon='✅'
                )