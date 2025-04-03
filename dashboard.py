import pandas as pd           #  manipulacao de dados 
import streamlit as st        #  criar dashboard 
import plotly.express as px    #  construir graficos


#=============================== 
# configuracao da pagina
st.set_page_config(page_title="AIDS no Maranhão ", layout="wide")
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #004080;  
    }
    [data-testid="stSidebar"] * {
        color: white !important;   
    }
    </style>
""", unsafe_allow_html=True)

#===============================
# SIDEBAR - painel lateral
with st.sidebar:
    st.image("logo_datasus.png", width=250)   # logo datasus
    st.header("UF: Maranhão")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/45/Bandeira_do_Maranh%C3%A3o.svg",
             width=200)
    st.markdown("---")

    st.markdown("""
    <div style='font-size:18px;'>
        <b>Disciplina:</b> Lógica e Matemática Discreta<br>  
        <br><b>Docente:</b> Leonardo Henrique Silva Lago
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div style='font-size:18px;'>
        <b>Discentes:</b><br>
        • Livius Penha<br>
        • Roberth Furtado<br>
        • Gabriel<br>
        • Eliseu
    </div>
    """, unsafe_allow_html=True)

#===============================
# leitura e tratamento dos dados
df = pd.read_csv("dados.csv", sep=",")
df = df[df["Ano Notificação"] != "TOTAL"] # removendo linha total
df["Ano Notificação"] = df["Ano Notificação"].astype(int)
# lista de faixas etarias
faixas = ['< 1 ano', '1-4', '5-9', '10-14', '15-19', '20-29', '30-39',
          '50-59', '60-69', '70-79', '80 e mais']

#===============================
# titulo do dashboard
st.markdown("<h1 style='text-align: center; color: #004080;' >Casos de AIDS: De 2018 a 2023</h1>", unsafe_allow_html=True)

# texto 1
st.markdown("<h2 style='text-align: left; color: #004080;' >1. Introdução</h2>", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 20px;'>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A AIDS (Síndrome da Imunodeficiência Adquirida) continua sendo um dos maiores desafios de saúde pública no Brasil. 
Embora haja avanços significativos na prevenção e no tratamento, a incidência da doença ainda exige atenção constante dos gestores públicos e da sociedade.
Este relatório tem como foco os casos notificados de AIDS no estado do Maranhão, entre os anos de 2018 e 2023, com o objetivo de analisar padrões de ocorrência por ano e faixa etária. 
A escolha do Maranhão justifica-se por sua importância estratégica na Região Nordeste, além de ser um estado com desafios históricos em relação à cobertura de saúde e vigilância epidemiológica.
</p>""", unsafe_allow_html=True)

# texto 2
st.markdown("<h2 style='text-align: left; color: #004080;' >2. Metodologia</h2>", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 20px;'>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Os dados utilizados neste dashboard foram coletados na plataforma DATASUS, por meio do sistema TABNET/SINAN, que disponibiliza informações públicas sobre doenças e agravos de notificação em todo o território brasileiro.
Foi realizado um recorte específico para o estado do Maranhão, abrangendo o período de 2018 a 2023. Esses dados foram exportados em formato .csv e processados com a linguagem Python, utilizando as bibliotecas:
    <ul style='font-size: 20px; margin-left: 40px;'>
        <li>Pandas para manipulação dos dados;</li>
        <li>Plotly.express para construção dos gráficos interativos;</li>
        <li>Streamlit para desenvolvimento do dashboard apresentado;</li>
    </ul>
</p>""", unsafe_allow_html=True)

# texto 3
st.markdown("<h2 style='text-align: left; color: #004080;' >3. Dashboards apresentados</h2>", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 20px;'>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Com base nos dados tratados, foram gerados quatro graficos, que compoem os dashboards abaixo:
</p>
<p style='font-size: 20px;'>
1. Grafico de pizza que mostra a distribuicao por ano.<br>
2. Grafico de barras com os grupos etarios mais afetados.<br> 
3. Grafico de barras empilhadas que mostra como a incidencia varia ao longo do tempo.<br>
4. Grafico de linha que permite observar tendencias por grupo etario.<br>
</p>""", unsafe_allow_html=True)

#===============================
# colunas de grafico 1 e 2
col1, col2 = st.columns(2)
# grafico 1  >>  Evolucao total de casos por ano
with col1:
    fig1 = px.pie(df, names='Ano Notificação', values='Total', title="1.Total de Casos por Ano")
    st.plotly_chart(fig1, use_container_width=True)
# grafico 2  >>  Distribuicao por faixa etaria total (18-23)
with col2:
    df_total = pd.read_csv("dados.csv")
    casos_por_faixa = df_total[df_total["Ano Notificação"] == "TOTAL"][faixas].T.reset_index()
    casos_por_faixa.columns = ["Faixa Etaria", "Casos"]

    fig2 = px.bar(casos_por_faixa, x="Casos", y="Faixa Etaria", orientation='h',
                title="2.Distribuicao total por faixa etaria (2018-2023)")
    st.plotly_chart(fig2, use_container_width=True)

#===============================
# colunas de grafico 3 e 4
col3, col4 = st.columns(2)
# grafico 3  >>  Comparacao faixa etaria x ano
with col3:
    df_long = pd.melt(df, id_vars=["Ano Notificação"], value_vars=faixas,
                      var_name="Faixa Etaria", value_name="Casos")
    fig3 = px.bar(df_long, x="Ano Notificação", y="Casos", color="Faixa Etaria",
                  title="3.Casos por faixa etaria ao longo dos anos", barmode="stack")
    st.plotly_chart(fig3, use_container_width=True)
# grafico 4  >>  faixa etaria predominante por ano
with col4:
    df_linhas = df[["Ano Notificação"] + faixas]
    df_long_line = pd.melt(df_linhas, id_vars="Ano Notificação", value_vars=faixas,
                           var_name="Faixa etaria", value_name="Casos")

    df_long_line["Ano Notificação"] = df_long_line["Ano Notificação"].astype(int)

    fig4 = px.line(df_long_line, x="Ano Notificação", y="Casos", color="Faixa etaria",
                   title="4.Evolucao por faixa etaria", markers=True)
    st.plotly_chart(fig4, use_container_width=True)

#================================
# texto de conclusao

st.markdown("<h2 style='text-align: left; color: #004080;' >4. Conclusão</h2>", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 20px;'>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A análise dos dados de AIDS no Maranhão entre 2018 e 2023 revelou que os casos concentram-se principalmente nas faixas etárias entre 20 e 39 anos. Além disso, observou-se uma redução no número total
de casos nos últimos anos, embora ainda existam variações significativas por grupo etário, o que reforça a importância de campanhas direcionadas ao público jovem e adulto referente à conscientização e políticas públicas.
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Este dashboard pode ser facilmente adaptado para análises de outros estados ou doenças notificáveis, promovendo a democratização dos dados e a ampliação do conhecimento baseado em evidências.<br>
</p>""", unsafe_allow_html=True)



#===============================
# rodape
st.markdown("---")
st.caption("Fonte: DATASUS/TabNet • Desenvolvido por Livius, Roberth, Elisei, Gabriel ©")
