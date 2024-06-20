from typing import Callable
from components.select_columns import select_columns
from components.select_dataframes import select_dataframes
from components.uploader import convert_df, uploader
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="XLSX para CSV",
    page_icon="✍️",
    layout='wide',
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

    for col in df.columns:
        if col.endswith('_x') or col.endswith('_y'):
            base_col = col[:-2]  # Remove o sufixo '_x' ou '_y'
            if base_col in df.columns:
                df[base_col] = df[base_col].combine_first(df[col])
                df.drop(columns=[col], inplace=True)
            else:
                df.rename(columns={col: base_col}, inplace=True)

    cols = set(col for cols in columns.values() for col in cols)

    inter_df: pd.DataFrame = df[[intersection, *cols]].copy()

    for col in inter_df.select_dtypes(include=['datetime64[ns]', 'datetime']):
        inter_df[col] = inter_df[col].dt.strftime('%d/%m/%Y')

    search = st.text_input(
        label='Pesquise aqui',
        placeholder="Separe com espaços caso queria mais deu uma busca!",
    )

    inter_df = inter_df.dropna(subset=[intersection])
    inter_df = inter_df[inter_df[intersection].astype(str).str.strip() != '']

    final_df = inter_df.copy()
    if search:
        splitted_search = search.split(" ")

        def condition(word):
            return inter_df.apply(lambda row: row.astype(str).str.contains(word, case=False).any(), axis=1)

        conditions = [condition(word) for word in splitted_search]

        combined_condition = conditions[0]
        for cond in conditions[1:]:
            combined_condition &= cond

        final_df = inter_df[combined_condition]

    

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
            # st.balloons()
            st.session_state.clear()
            st.rerun()
