from typing import Callable
from components.select_columns import select_columns
from components.select_dataframes import select_dataframes
from components.uploader import convert_df, uploader
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="XLSX para CSV",
    page_icon="✍️",
    layout='wide'
)


st.markdown(
    body='''
## Conversor **:violet[(XLSX para CSV)]**
'''
)

uploader()
select_dataframes()
select_columns()

has_columns = 'columns' in st.session_state
has_intersection = 'intersection' in st.session_state

if has_columns and has_intersection:
    dataframes: list[pd.DataFrame] = st.session_state.dataframes
    columns: dict[str, list[str]] = st.session_state.columns
    intersection: str = st.session_state.intersection

    df = None
    for dataframe in dataframes:
        if df is None:
            df = dataframe
            continue
        df = pd.merge(df, dataframe, on=intersection)

    cols = [col for cols in columns.values() for col in cols]

    inter_df: pd.DataFrame = df[[intersection, *cols]]

    for col in inter_df.select_dtypes(include=['datetime64[ns]', 'datetime']):
        inter_df[col] = inter_df[col].dt.strftime('%d/%m/%Y')

    search = st.text_input(
        label='',
        placeholder="Pesquise aqui",
    )

    condition: Callable[[pd.Series], pd.Series] = lambda row: row.astype(str).str.contains(search, case=False).any()

    contains_search_string = inter_df.apply(condition, axis=1)

    final_df = inter_df
    if search:
        final_df = inter_df[contains_search_string]

    event = st.dataframe(
        data=final_df,
        hide_index=True,
        use_container_width=True,
        selection_mode='multi-row',
        on_select='rerun',
    )

    if len(event.selection.rows) > 0:
        download_df: pd.DataFrame = final_df.iloc[event.selection.rows]

        csv = convert_df(download_df)
        is_downloaded = st.download_button(
            label="Baixar CSV",
            data=csv,
            file_name="csv-file.csv",
            mime="text/csv",
            use_container_width=True,
        )

        if is_downloaded:
            st.session_state.clear()
            st.rerun()
