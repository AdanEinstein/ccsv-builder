import streamlit as st

st.set_page_config(
    page_title="Manual",
    page_icon="📰",
    layout='wide'
)

st.title('Manual de uso:')

st.divider()

with open('assets/1.mp4', 'rb') as video:
    st.markdown(
        '''
        #### 1. Carregue o arquivo Excel:
        Selecione o arquivo Excel que deseja converter.
        ''')
    st.video(video.read(), format='video/mp4')

st.divider()

with open('assets/2.mp4', 'rb') as video:
    st.markdown(
        '''
        #### 2. Selecionar as abas:
        Selecione as abas que deseja converter.
        ''')
    st.video(video.read(), format='video/mp4')
    
st.divider()

with open('assets/3.mp4', 'rb') as video:
    st.markdown(
        '''
        #### 3. Selecionar as colunas:
        Selecione as colunas que deseja converter.
        ''')
    st.markdown(
        '''
        #### 4. Selecionar a coluna de interseção:
        Selecione a coluna que possui valores comuns entre as abas.
        ''')
    st.video(video.read(), format='video/mp4')

st.divider()

with open('assets/4.mp4', 'rb') as video:
    st.markdown(
        '''
        #### 5. Filtrar por palavra:
        Pesquise por palavras específicas no conteúdo das colunas.
        ''')
    st.markdown(
        '''
        #### 6. Substituir valores:
        Preencha os campos "Substituir" e "Para" para substituir valores específicos.
        ''')
    st.video(video.read(), format='video/mp4')

st.divider()

with open('assets/5.mp4', 'rb') as video:
    st.markdown(
        '''
        ##### 7. Download do CSV:
        Clique no botão "Baixar CSV" para baixar o
        CSV resultante com os dados filtrados e substituídos.
        ''')
    st.video(video.read(), format='video/mp4')

