# projeto referente a uma analise de dados de infeccao de AIDS no maranhao (2018-2023) (python)

cadeira: logica e matematica discreta
alunos: 
  - Livius Penha
  - Eliseu
  - Rebert Furtado
  - Gabriel

1. INTRODUCAO
    A AIDS (Síndrome da Imunodeficiência Adquirida) continua sendo um dos maiores desafios de saúde pública no Brasil.  Embora haja avanços significativos na prevenção e no tratamento, a incidência da doença ainda exige atenção constante dos gestores públicos e da sociedade. Este relatório tem como foco os casos notificados de AIDS no *estado do Maranhão, entre os anos de **2018 e 2023*, com o objetivo de analisar padrões de ocorrência por ano e faixa etária.  A escolha do Maranhão justifica-se por sua importância estratégica na Região Nordeste, além de ser um estado com desafios históricos em relação à cobertura de saúde e vigilância epidemiológica.

2. Metodologia
    Os dados utilizados neste dashboard foram coletados na plataforma *DATASUS, por meio do sistema **TABNET/SINAN*, que disponibiliza informações públicas sobre doenças e agravos de notificação em todo o território brasileiro.
Foi realizado um recorte específico para o estado do Maranhão, abrangendo o período de 2018 a 2023. 
Esses dados foram exportados em formato .csv e processados com a linguagem *Python*, utilizando as bibliotecas:
- *pandas* para manipulação dos dados,
- *plotly.express* para construção dos gráficos interativos,
- *streamlit* para desenvolvimento do dashboard apresentado.
Todo o tratamento e visualização foram feitos de forma automatizada, com foco em facilitar a análise e interpretação por profissionais da saúde e gestores públicos.

3. CONCLUSAO
     A análise dos dados de AIDS no Maranhão entre 2018 e 2023 revelou que os casos concentram-se principalmente nas faixas etárias entre *20 e 39 anos*, o que reforça a importância de campanhas direcionadas ao público jovem e adulto. Além disso, observou-se uma redução no número total de casos nos últimos anos, embora ainda existam variações significativas por grupo etário. O uso do Python e das bibliotecas modernas de visualização foi essencial para organizar, analisar e apresentar os dados de forma clara e acessível, contribuindo para uma *tomada de decisão mais assertiva em saúde pública*.

    Este dashboard pode ser facilmente adaptado para análises de outros estados ou doenças notificáveis, promovendo a democratização dos dados e a ampliação do conhecimento baseado em evidências.
