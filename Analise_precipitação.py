import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

#Def para pular linhas
def pularlinha (Nlinhas):
    print("\n" * Nlinhas)

#Def usado em tratamentoentrada para erros no valor de entrada
def validaçãoentrada (entrada):
    if type(entrada) != int:
        return False
    else:
        return True    

#Usado para verificar se não há erros nos parâmetros de entrada
def tratamentoentrada (lista, frasesolicitação, min, max):
    entrada = False
    while not validaçãoentrada(entrada):
        try:
            entrada = int(input(frasesolicitação))
        except ValueError:
            entrada = False
        #Valores que não estão na formatação correta
        if not validaçãoentrada(entrada):
            pularlinha(1)
            print("Digite o valor de entrada na formatação correta")
        if validaçãoentrada(entrada) is True:
            #Caso o valor esteja fora do máximo e mínimo
            if entrada < min or entrada > max:
                pularlinha(1)
                print(f"O valor deve estar entre {min} e {max}, você digitou {entrada}")
                entrada = None
            if entrada != None:
                if entrada >= min and entrada <= max:
                    #Inserindo o prefixo 0 que vem antes dos meses que vão de 1 até 9
                    if entrada < 10 and entrada > 0:
                        strentrada = str(entrada)
                        strentrada = '0' + strentrada
                        lista.append(strentrada)
                        return entrada
                    else:
                        lista.append(entrada)
                        return entrada

#Usado para não permitir que o ano final seja menor que o inicial 
def entradaanofinal (listaanos):
    if int(listaanos[1]) < int(listaanos[0]):
        ano = False
        while not validaçãoentrada(ano):
            try:
                print("O ano final deve ser maior que a o ano inicial que é ",listaanos[0])
                ano = int(input("Digite novamente o ano final: "))
                if (ano > int(listaanos[0])) is False or ano > 2016:
                    ano = False
            except ValueError:
                print("Digite apenas valores númericos!")
#Abertura do arquivo de dados
dftabela = pd.read_csv("OK_Anexo_Arquivo_Dados_Projeto.csv", delimiter=';')
df = dftabela.copy()

#tratamento de erros nos dados de precipitação
def correção (nomecoluna, nomenovocoluna, parametromax):
    global df, df_colunaerros, dftabela

    df_colunaerros = dftabela[nomecoluna].copy()
    df = dftabela.drop(columns=nomecoluna)
    #Criação de uma nova coluna com todos os valores sendo zero
    df[nomenovocoluna]= 0
    numerolinhaserro = df_colunaerros[df_colunaerros < parametromax].index.tolist()
    #Substituição de todos os valores com valor negativo
    for e in numerolinhaserro:
        df_colunaerros[e] = 1
    #Adicionando os valores de precipatação tratados na coluna nova criada
    df[nomenovocoluna] = df_colunaerros

#dicionário com chave na data e valores para os dados
def disponibilizandodados(nomecoluna):
    global df
    #Fazendo a disponibilização do dados na memória
    dictdados = dict([(i,[a]) for i,a in zip(df['data'], df[nomecoluna])])

correção('precip', 'precipitação', 0)


#Filtra e adiciona em um dicionário os dados do mês/ano com a maior precipitação
def maischuvoso ():
    global df
    maischuva = df['precipitação'].max()
    valorlinha = df['precipitação'].loc[df['precipitação'] == maischuva].index.tolist()
    #soma do valor de precipitação para todo o mês
    datainicial = df['data'].loc[0]
    datafinal = df['data'].loc[(df[df.columns[0]].count() - 1)]
    datacontagem = datainicial
    print("Aguarde processando todos os dados...")
    while True:
            #Verificador para não atualizar o mês mais de uma vez, como no caso de trocar 12 por 01 logo após ser alterado de 11 para 12
            verificadortroca = False
            if datacontagem == datainicial:
                separador = datacontagem.find('/')
                #listando a data, pois strings são imutáveis
                L_ldata = datacontagem.split('/')
                #Alterar o valor do mes e o valor do ano
                if int(datacontagem[separador + 1]) != 0 and verificadortroca is False:
                    valormes = int(datacontagem[separador + 2])
                    #Para quando o mês corresponder a 12
                    if valormes == 2:
                        L_ldata[1] = '01'
                        #caso o ano seja 1999
                        if int(datacontagem[-1]) == 9 and int(datacontagem[-2]) == 9:
                            L_ldata[-1] = '2000'
                            print("Estamos quase acabando.")
                        #para os demais anos
                        else:
                            ano = [L_ldata[-1]]
                            if L_ldata[-1][0] == 1:
                                if int(L_ldata[-1][-1]) == 9 and int(L_ldata[-1][-2]) != 9:
                                    L_ldata[-1][-1] = '0' + str(int( L_ldata[-1][-2]) + 1)
                            else:
                                if L_ldata[-1][-1] != 9:
                                    #Atualizando a dezena do ano, como de 1969 para 1970
                                    if int( L_ldata[-1][-1]) == 9:
                                        dezenadoano = int( L_ldata[-1][-2]) + 1
                                        unidadeano = '0'
                                    else:
                                        dezenadoano = int(L_ldata[-1][-2])
                                        unidadeano = int(L_ldata[-1][-1]) + 1
                                    L_ldata[-1] = str(L_ldata[-1][:-2]) + str(dezenadoano) + str(unidadeano)
                                else:
                                    L_ldata[-1] = '2010'
                        verificadortroca = True
                    if valormes != 2:
                        valormes = valormes + 1
                        L_ldata[1] = str(L_ldata[1][0]) + str(valormes)
                        verificadortroca = True
                if int(datacontagem[separador + 1]) == 0 and verificadortroca == False:
                    valormes = int(datacontagem[separador + 2])
                    if valormes == 9:
                        L_ldata[1] = '10'
                        verificadortroca = True
                    if valormes != 9 and verificadortroca == False:
                        L_ldata[1] = '0' + str(int(L_ldata[1][1]) + 1)
                        verificadortroca = True
                datacontagem = L_ldata[0] + '/' + L_ldata[1] + '/' + L_ldata[2]
            #formatando a data para poder filtrar os dados
            auxdatainicial = pd.to_datetime(str(datainicial), format='%d/%m/%Y')
            auxdatacontagem = pd.to_datetime(str(datacontagem), format='%d/%m/%Y')
            df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
            #filtragem dos dados
            dadosparasomar = df.loc[(df['data'] >= auxdatainicial) & (df['data'] <= auxdatacontagem)]
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            #O valor da precipitação da data que corresponde ao próximo mês 
            indicelinha = dadosparasomar[dadosparasomar['data'] == auxdatacontagem].index.tolist()
            retirardasoma = dadosparasomar.loc[indicelinha, 'precipitação']
            #avaliação para datas vazias
            if retirardasoma.index.empty is False:
                #tratamento para meses sem valor
                somaprecipitação = dadosparasomar['precipitação'].sum() - float(retirardasoma.iloc[0])
                #Acessando apenas o mês e o ano
                #Adicionando o primeiro valor ao dicionário usando a data inicial
                if datainicial == '01/01/1961':
                    chave = datainicial[3:]
                    diciosoma = {chave : (somaprecipitação)}
                else:
                    if float(diciosoma[chave]) < somaprecipitação:
                        del diciosoma[chave]
                        chave = datainicial[3:]
                        diciosoma[chave] = somaprecipitação
            if datacontagem  == '01/08/2016':
                pularlinha(1)
                print(f"A maior soma de precipitação foi de {diciosoma[chave]}, sendo no mês/ano de {chave}")
                print(diciosoma)
                pularlinha(2)
                break
            #atualizando a datainicial
            datainicial = datacontagem

    #Transformando o type list em um int
    valorlinha = int(valorlinha[0])
    #Acessando o valor da data no dataframe
    dataprecip = str(df['data'][valorlinha])
    #formatando a data da maior precipitação
    separador = dataprecip.find(" ")
    dataparaformatar = dataprecip[:separador]
    dataformatada = dataparaformatar.split("-")
    dataformatada = str(dataformatada[-2]) + "/" + str(dataformatada[-3])

    diciomaischuva = {dataformatada: str(maischuva)}
    
    print(f"O mês/ano com a maior precipitação em um único dia foi em {dataformatada}, sendo o volume de precipitação de {maischuva}.")
    print(diciomaischuva)
    pularlinha(2)

#Filtragem da datas para exibição do dados conforme solicitado pelo usuário
def dadosparaexibição (listameses, listaanos, valoroperação):
    colunadatas = df['data']
    datas = []
    #Unindo o mes/ano inicial e final em uma lista
    for mes,ano in zip(listameses, listaanos):
            junçãodata = '01/' + str(mes) + '/' + str(ano)
            datas.append(junçãodata)
   
    #Alteração na formatação das datas para filtragem dos intervalos de data
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    dadosparaexibição = df.loc[(df['data'] >= datas[0]) & (df['data'] <= datas[1])]
    pd.set_option('display.max_rows', None)
    #reestrigindo a exibição das colunas
    if valoroperação == 1:
        dadosparaexibição = dadosparaexibição.rename(columns={'maxima':'temperatura_maxima', 'minima':'temperatura_minima', 'um_relativa':'umidade_relativa', 'vel_vento':'velocidade_vento'})
        print(dadosparaexibição)
        pularlinha(2)
    if valoroperação == 2:
        print(dadosparaexibição[['data', 'precipitação']])
        pularlinha(2)
    if valoroperação == 3:
        dadosparaexibição = dadosparaexibição.rename(columns={'maxima':'temperatura_maxima'})
        print(dadosparaexibição[['data', 'temperatura_maxima']])
        pularlinha(1)
        dadosparaexibição = dadosparaexibição.rename(columns={'minima':'temperatura_minima'})
        print(dadosparaexibição[['data', 'temperatura_minima']])
        pularlinha(2)
    if valoroperação == 4:
        dadosparaexibição = dadosparaexibição.rename(columns={'um_relativa':'umidade_relativa'})
        print(dadosparaexibição[['data', 'umidade_relativa']])
        pularlinha(1)
        dadosparaexibição = dadosparaexibição.rename(columns={'vel_vento':'velocidade_vento'})
        print(dadosparaexibição[['data', 'velocidade_vento']])
        pularlinha(2)

def media_temperatura_minima(df, G_lmeses):
    datas = []
    lanos = ['2006']
    #Unindo a data com o mês informado pelo usuário e o ano inicial
    junçãodata = '01/' + str(G_lmeses[0]) + '/' + str(lanos[0])
    datas.append(junçãodata)
    #variavel para somar toda as temperatura minima, numero de linhas e numero de linhas q corresponde a primeira data do próximo mês
    somatotal = 0
    numerototallinha = 0
    valorretiralinha = 0
    #dicionário para o dataframe
    diciomediames = {'datas' : [], 'média_temperatura' : [] }
    listamedia = []
    listadatas = []
    while True:
        #Atualizando data final
        atualizandodata = datas[0].split("/")
        datafinal = atualizandodata[0] + "/" + atualizandodata[1] + "/" + str(int(atualizandodata[2]) + 1)
        #Atualizando o mês/ano para um formato como agosto/2000
        nomemees = {'01' : 'Janeiro', '02' : 'Fevereiro', '03' : 'Março', '04' : 'Abril', '05' : 'Maio', '06' : 'Junho', '07' : 'julho', '08' : 'Agosto', '09' : 'Setembro', '10' : 'Outubro', '11' :'Novembro', '12' : 'Dezembro'}
        datacomnome = str(nomemees[atualizandodata[1]]) + '/' + atualizandodata[2]
        if len(datas) == 1:
            datas.append(datafinal)
        else:
            datas[1] = datafinal
       #formatando a data para consulta no DataFrame
        data_formatada1 = datetime.strptime(str(datas[0]), "%d/%m/%Y").strftime("%m-%d-%Y")
        data_formatada2 = datetime.strptime(str(datas[1]), "%d/%m/%Y").strftime("%m-%d-%Y")
        #Armazenanda a Series resultante em uma variável
        consulta = df[df['data'] == data_formatada1]
        if consulta.empty != True:
            print("a faixa de datas é de",datas)
            #Data para saber quando chegou ao final do dados
            datacontagemfinal = atualizandodata[0] + "/" + atualizandodata[1] + "/" + '2017'
            #Filtragem da faixa de datas

            dadosparaexibição = df[['data','minima']][(df['data'] >= data_formatada1) & (df['data'] <= data_formatada2)]
            #somando a temperatura e contando o número de linhas para calcular a média
            dadosparaexibição = dadosparaexibição.rename(columns={'minima':'temperatura_minima'})
            somadatemperatura = dadosparaexibição['temperatura_minima'].sum()
            numerolinhas = dadosparaexibição['temperatura_minima'].index.tolist()
            #retirando o valor da temperatura minima que corresponde ao primeiro dia do proximo mês
            if datas[1] != datacontagemfinal:
                valoretirar = dadosparaexibição.loc[(int(numerolinhas[-1]), 'temperatura_minima')]
                #valor de linhas que precisarão ser retirados do numero total de linhas
                valorretiralinha += 1
                somadatemperatura = somadatemperatura - valoretirar
            #soma da precipatação de todo o período e o total de dias para a média geral
            somatotal = somatotal + somadatemperatura
            numerototallinha = numerototallinha + int(len(numerolinhas))
            #Caso o número de linhas seja igual a zero isso quer dizer que não existe dados no DataFrame
            if int(len(numerolinhas)) == 0:
                print(f"Não existe valores para a data de {datas[0]} no DataSet")
            else:
                mediageralminima = float(somadatemperatura) / int(len(numerolinhas))
                
                #lista de dados para adicionar no dicionário da média ao longo dos 11 anos 
                listadatas.append(datas[0]) 
                listamedia.append(f"%.2f" % mediageralminima)
                pularlinha(1)
                print(f"A média geral da temperatura para o mês/ano de {datacomnome} é %.2f" % mediageralminima)
                pularlinha(2)
                datas[0] = datafinal
                if datas[0] == datacontagemfinal:
                    media11anos = somatotal / (numerototallinha - valorretiralinha)
                    print(f"A média geral para a faixa de dados de {nomemees[atualizandodata[1]]}/2006 a {nomemees[atualizandodata[1]]}/2016 é %.2f" % media11anos)

        else:
            break
    #Adicionando a lista de dados no dicionário
    diciomediames['datas'], diciomediames['média_temperatura'] = listadatas, listamedia
    #Criação do dataframe para gerar o gráfico
    dfmediames = pd.DataFrame(diciomediames)
    #Alterado o tipo de dado de object para float   
    dfmediames['média_temperatura'] = dfmediames['média_temperatura'].astype(float)
    #Criação do gráfico
    dfmediames.plot(x='datas', y='média_temperatura', kind='bar')
    #Adicionando nome no eixo Y, título e ajustando os subplots para a exibição do nomes das colunas no eixo X
    plt.ylabel("Média da temperatura mínima")
    plt.title("Média da temperatura para o mês informado de 2006 a 2016")
    plt.subplots_adjust(bottom=0.229, top=0.905)
    plt.show()
    pularlinha(2)
    
maischuvoso()


disponibilizandodados('maxima')

while True:

    print("Você pode fazer a visualização do intervalo de dados em um limite final e inicial de sua escolha ou obter a média da temperatura mínima de um determinado mês \ne a média geral da temperatura mínima para todo o período de 2006 a 2016 (11 anos).")
    itemescolha = input("Digite qual do dois itens deseja executar, \nsendo 'visualização' para acessar o primeiro e 'média da temperatura' para o segundo, ou 'sair' para encerrar: ")
    
    if itemescolha == 'sair':
        break

    if itemescolha != "visualização" and itemescolha != "média da temperatura":
        print("Digite apenas 'visualização', 'média da temperatura' ou sair para encerrar o programa.")
        itemescolha = input("Digite novamente o nome da operação: ")
        if itemescolha == "sair":
            break

    if itemescolha == "visualização":
        G_lmes = []
        G_lano = []
        G_loperação = []

        tratamentoentrada(G_lmes,"Digite o valor correspodente ao mês inicial: ", 1, 12)
        pularlinha(1)
        tratamentoentrada(G_lano, "Digite o valor correspodente ao ano inicial: ", 1961, 2016)
        pularlinha(1)
        tratamentoentrada(G_lmes,"Digite o valor correspodente ao mês final: ", 1, 12)
        pularlinha(1)
        tratamentoentrada(G_lano, "Digite o valor correspodente ao ano final: ", 1961, 2016)
        pularlinha(2)
        entradaanofinal(G_lano)

        while True:
            print("A operações que você pode escolher são: 1 - Todos os dados; 2 - Apenas os de precipitação;\n 3 - Apenas os de temperatura; 4 - Apenas os de umidade e vento para o período informado")
            print("Caso desejar encerrar o programa digite 5")
            pularlinha(1)
            operações = tratamentoentrada(G_loperação, "Digite o valor referente a operação que deseja realizar: ", 1, 5)
            pularlinha(2)
            match operações:
                case 1:
                    dadosparaexibição(G_lmes, G_lano, 1)
                case 2:
                    dadosparaexibição(G_lmes, G_lano, 2)
                case 3:
                    dadosparaexibição(G_lmes, G_lano, 3)
                case 4:
                    dadosparaexibição(G_lmes, G_lano, 4)
                case 5:
                    print("Programa encerrado")
                    break
   
    if itemescolha == "média da temperatura":
        G_lmeses = []
        tratamentoentrada(G_lmeses, "Informe o mês que deseja saber a média da temperatura: ", 1, 12)
        media_temperatura_minima(df, G_lmeses)
