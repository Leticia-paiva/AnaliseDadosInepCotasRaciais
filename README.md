# Analis de dados do inep do ensino superior com foco nas Cotas Raciais
Em 2009 foi criada a lei das cotas para acesso ao ensino superior, abrangendo des de vagas em universidades públicas a bolsas e financiamentos em universidades privadas. 

Foram criadas para alunos negros e pardos, uma vez que sua presença no ensino supeior era inexpressiva.

Para analisar a ação das cotas no ensino supeior foram analisados os microdados do ensino superior de 2009 a 2019, dados esses disponibilizados pelo inep no site:

https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados

# Extração dos dados
Os microdados disponibilizados pelo inep tem arquivos com mais de 3 gigas de extensão para cada ano, necessitando de um pré processamento dos dados.
Para isso foi desenvolvido um scrip , o **filter.py**, que transforma o CSV do inep em outro csv menor, apenas com as colunas que utilizei. 
