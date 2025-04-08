import pandas as pd           #  manipulacao de dados 
import streamlit as st        #  criar dashboard 
import plotly.express as px    #  construir graficos



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

df = pd.read_csv("dados.csv", sep=",")
df = df[df["Ano Notificação"] != "TOTAL"] # removendo linha total
df["Ano Notificação"] = df["Ano Notificação"].astype(int)

# lista de faixas etarias
faixas = ['< 1 ano', '1-4', '5-9', '10-14', '15-19', '20-29', '30-39',
          '50-59', '60-69', '70-79', '80 e mais']

df_sx = pd.read_csv("dados_sx.csv")
df_sx = df_sx[df_sx["Sexo"] != "TOTAL"]

df_sx_long = pd.melt(df_sx, id_vars=["Sexo"], value_vars=["2018", "2019", "2020", "2021", "2022", "2023"],
                     var_name="Ano", value_name="Casos")
df_sx_long["Ano"] = df_sx_long["Ano"].astype(int)            

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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Com base nos dados tratados, foram gerados quatro gráficos, que compõem os dashboards abaixo:
</p>
<p style='font-size: 20px;'>
1. Gráfico de linha que mostra a distribuição de casos por ano com relação ao sexo.<br>
2. Gráfico de barras com os grupos etários mais afetados.<br> 
3. Gráfico de barras empilhadas que mostra como a incidência varia ao longo do tempo.<br>
4. Gráfico de linha que permite observar tendências por grupo etário.<br>
</p>""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
# grafico 1  >>  Evolucao total de casos por ano
with col1:
    fig1 = px.line(df_sx_long, x="Ano", y="Casos", color="Sexo",
                   title="1.Evolução de Casos de AIDS por Sexo (2018–2023)", markers=True)
    st.plotly_chart(fig1, use_container_width=True)
# grafico 2  >>  Distribuicao por faixa etaria total (18-23)
with col2:
    df_total = pd.read_csv("dados.csv")
    casos_por_faixa = df_total[df_total["Ano Notificação"] == "TOTAL"][faixas].T.reset_index()
    casos_por_faixa.columns = ["Faixa Etaria", "Casos"]

    fig2 = px.bar(casos_por_faixa, x="Casos", y="Faixa Etaria", orientation='h',
                title="2.Distribuição total por faixa etária (2018-2023)")
    st.plotly_chart(fig2, use_container_width=True)

#===============================
# colunas de grafico 3 e 4
col3, col4 = st.columns(2)
# grafico 3  >>  Comparacao faixa etaria x ano
with col3:
    df_long = pd.melt(df, id_vars=["Ano Notificação"], value_vars=faixas,
                      var_name="Faixa Etaria", value_name="Casos")
    fig3 = px.bar(df_long, x="Ano Notificação", y="Casos", color="Faixa Etaria",
                  title="3.Casos por faixa etária ao longo dos anos", barmode="stack")
    st.plotly_chart(fig3, use_container_width=True)
# grafico 4  >>  faixa etaria predominante por ano
with col4:
    df_linhas = df[["Ano Notificação"] + faixas]
    df_long_line = pd.melt(df_linhas, id_vars="Ano Notificação", value_vars=faixas,
                           var_name="Faixa etaria", value_name="Casos")

    df_long_line["Ano Notificação"] = df_long_line["Ano Notificação"].astype(int)

    fig4 = px.line(df_long_line, x="Ano Notificação", y="Casos", color="Faixa etaria",
                   title="4.Evolução por faixa etária", markers=True)
    st.plotly_chart(fig4, use_container_width=True)




st.markdown("<h2 style='text-align: left; color: #004080;' >4. Conclusão</h2>", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 20px;'>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A partir da análise dos dados e gráficos, notou-se que no Maranhão, entre 2018 e 2023, a faixa etária mais afetada pelos casos de AIDS foi a de 20 a 39 anos, concentrando a maior parte das notificações ao longo do período. A distribuição por idade manteve-se estável, sem variações abruptas que indicassem mudanças significativas no perfil etário das pessoas acometidas.

De modo geral, os dados revelam uma tendência consistente de queda nos casos registrados ano após ano. Entretanto, em 2022, houve uma reversão pontual nessa trajetória: os números voltaram a subir, aproximando-se dos patamares de 2020, interrompendo a tendência de redução observada nos anos anteriores e configurando uma anomalia no comportamento dos dados.

Apesar desse aumento isolado, a comparação entre os extremos do período analisado mostra uma redução expressiva de 68,5% nos casos notificados entre 2018 e 2023, indicando um avanço significativo no controle da doença. Contudo, a recorrência de casos entre jovens adultos reforça a necessidade de políticas públicas direcionadas a essa população, com ênfase em prevenção, diagnóstico precoce e tratamento contínuo, a fim de consolidar o declínio da AIDS no estado e evitar retrocessos.<br>
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Este dashboard pode ser facilmente adaptado para análises de outros estados ou doenças notificáveis, promovendo a democratização dos dados e a ampliação do conhecimento baseado em evidências.<br>
</p>""", unsafe_allow_html=True)



#===============================
# rodape
st.markdown("---")
st.caption("Fonte: DATASUS/TabNet • Desenvolvido por Livius, Roberth, Elisei, Gabriel ©")
