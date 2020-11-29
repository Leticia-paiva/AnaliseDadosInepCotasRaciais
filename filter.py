import sys
year = sys.argv[3]
index = 0
columnMap = {
    '2019': [2, 6, 7, 8, 14, 15, 19, 22, 38, 55, 57, 58, 60, 74, 81, 90, 100],
    '2018': [2, 6, 7, 8, 14, 15, 19, 22, 38, 55, 57, 58, 60, 74, 81, 90, 100],
    '2017': [2, 6, 7, 8, 17, 18, 22, 25, 41, 58, 60, 61, 63, 77, 84, 93, 103],
    '2016': [2, 9, 11, 13, 28, 30, 35, 39, 55, 70, 72, 73, 75, 89, 96, 105, 115],
    '2015': [2, 9, 11, 13, 28, 30, 35, 39, 55, 70, 72, 73, 75, 89, 96, 105, 115],
    '2014': [2, 9, 11, 13, 28, 30, 35, 39, 55, 68, 70, 71, 73, 87, 94, 103, 113],
    '2013': [2, 9, 11, 13, 27, 29, 34, 39, 43, 70, 72, 73, 61, 86, 93, 102, 106],
    '2012': [2, 9, 11, 13, 19, 21, 26, 31, 35, 59, 61, 62, 53, 77, 84, 93, 97],
    '2011': [2, 48, 8, 10, 16, 18, 23, 26, 28, 54, 56, 57, 46, 72, 44, 87, 89],
    '2010': [2, 41, 8, 9, 13, 15, 20, 23, 25, 47, 49, 50, 38, 66, 72, 79, 81],
    '2009': [2, 0, 10, 9, 67, 66, 73, 26, 13, 39, 38, 41, 52, 21, 43, 0, 75],
}
situationMap = {
    '2019': 38,
    '2018': 38,
    '2017': 41,
    '2016': 55,
    '2015': 55,
    '2014': 55,
    '2013': 43,
    '2012': 35,
    '2011': 28,
    '2010': 25,
    '2009': 13
}
currentColums = columnMap[year]
currentSituation = situationMap[year]

with open(sys.argv[2], 'a') as file_out:
    with open(sys.argv[1]) as file_in:
        for line in file_in:
            columns = line.split('|')
            if columns[currentSituation] not in ['3', '4', '5', '7']:
                joinColums = []
                joinColums.append(columns[currentColums[0]])
                if year == '2009':
                    joinColums.append('') # 2009 has no "TP_TURNO" information
                else:
                    joinColums.append(columns[currentColums[1]])
                joinColums.append(columns[currentColums[2]])
                joinColums.append(columns[currentColums[3]])
                joinColums.append(columns[currentColums[4]])
                joinColums.append(columns[currentColums[5]])
                joinColums.append(columns[currentColums[6]])
                joinColums.append(columns[currentColums[7]])
                joinColums.append(columns[currentColums[8]])
                joinColums.append(columns[currentColums[9]])
                joinColums.append(columns[currentColums[10]])
                joinColums.append(columns[currentColums[11]])
                joinColums.append(columns[currentColums[12]])
                joinColums.append(columns[currentColums[13]])
                joinColums.append(columns[currentColums[14]])
                if year == '2009':
                    joinColums.append('') # 2009 has no "TP_ESCOLA_CONCLUSAO_ENS_MEDIO" information
                else:
                    joinColums.append(columns[currentColums[15]])
                joinColums.append(columns[currentColums[16]])
                importantColumns = '|'.join(joinColums)
                if index == 0:
                    file_out.write('NU_ANO_CENSO|TP_CATEGORIA_ADMINISTRATIVA|TP_TURNO|TP_GRAU_ACADEMICO|TP_MODALIDADE_ENSINO|TP_COR_RACA|TP_SEXO|NU_IDADE|CO_UF_NASCIMENTO|TP_SITUACAO|IN_RESERVA_ETNICO|IN_RESERVA_ENSINO_PUBLICO|IN_RESERVA_RENDA_FAMILIAR|IN_FINANCIAMENTO_ESTUDANTIL|IN_APOIO_SOCIAL|IN_ATIVIDADE_EXTRACURRICULAR|TP_ESCOLA_CONCLUSAO_ENS_MEDIO|IN_CONCLUINTE\n')
                else:
                    file_out.write(year+'|'+importantColumns+'\n')
                index += 1
