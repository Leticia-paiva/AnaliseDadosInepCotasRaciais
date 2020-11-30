# Analise de dados do inep do ensino superior com foco nas Cotas Raciais
Em 2009 foi criada a lei das cotas para acesso ao ensino superior, abrangendo des de vagas em universidades públicas a bolsas e financiamentos em universidades privadas. 

Foram criadas para alunos negros e pardos, uma vez que sua presença no ensino supeior era inexpressiva.

Para analisar a ação das cotas no ensino supeior foram analisados os microdados do ensino superior de 2009 a 2019, dados esses disponibilizados pelo inep no site:

https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados

# Extração dos dados
Os microdados disponibilizados pelo inep tem arquivos com mais de 3 gigas de extensão para cada ano, necessitando de um pré processamento dos dados.

Para isso foi desenvolvido um scrip , o **filter.py**, que transforma o CSV do inep em outro csv menor, apenas com as colunas que utilizei.

As colunas utilizadas e suas descrições estão no arquivo **MapaDosDadosFiltrados.txt**

Para utilizar o arquivo é necessário o seguinte comando :
```shell 
python3 filter.py ARQUIVO_DE_ENTRADA.CSV ALUNO_ANO_filtered.csv ANO
```
Os arquivos dos anos 2009 a 2016 estão com uma codificação diferente, por isso foi necessário a conversão para utf-8.
```shell 
iconv -f iso-8859-1 -t utf-8 ARQUIVO_DE_ENTRADA.CSV -o DM_ALUNO_ANO_utf8.CSV
```
# Manipulação e preparação dos dados
Os arquivos filtrados ainda têm uma extensão muito grande, desta forma foi utilizado a plataforma databricks : https://community.cloud.databricks.com/

O script abaixo utiliza ferramentas do pySpark e foi utilizado para gerar um csv contendo as informações condensadas de 2009 a 2019:

https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/6182606293192259/3377624785629858/5332627302389073/latest.html

O csv gerado foi o **inep_dados.csv**.

# Analise exploratoria dos dados

Utilizando o arquivo inep_dados.csv , através do **Google Colab**, foi possível construir gráficos comparativos utilizando python, pandas, plotly e demais bibliotecas.

https://colab.research.google.com/drive/1HAce4nBYZixKiuypO6Exc9A8OcKxHX-p?usp=sharing

Através dos gráficos foi possível acompanhar o impacto das cotas no ensino superior, tentando mitigar a discrepância que há entre a composição étnica e racial da sociedade 

brasileira e a presença de negros e pardos no ensino superior. 

Foi possível analisar dados de 2009 a 2019, onde se pode observar o crescimento de negros e pardos na rede pública e privada, mas também um menor crescimento de alunos que 

conseguem concluir a universidade. Também foi analisado a concentração de alunos que concluíram o ensino médio em escolas públicas e ingressaram na universidade,

mostrando que a diferença etcnica ainda é muito discrepante, mesmo em um grupo que provavelmente pertence na mesma classe social.
Ainda estamos muito longe de uma igualdade, mas o progresso é importante. 


