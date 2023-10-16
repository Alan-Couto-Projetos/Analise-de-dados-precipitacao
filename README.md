# Analise-de-dados-precipitacao

Esse projeto foi feito para o meu curso na PUC, e foi a primeira vez que tive contato com todas as biblioteca utilizadas, ademais todo o conhecimento de python utilizado nesse projeto foi
desenvolvimento pelas aulas do curso e o livro Introdução à Programação com Python: Algoritmos e Lógica de Programação Para Iniciantes por Nilo Ney Coutinho Menezes, logo eu ainda não 
possuia muito conhecimento sobre python e suas bibliotecas.

Nesse projeto foi solicitado os seguintes itens:

	1 - O tratamento dos dados.
	2 - Criação de um programa que realize as atividades listadas abaixo:

		1 - Exibição do mês com a maior soma de precitação. 
		2 - O mês/ano com a maior precipitação  em um único dia e o volume de chuva nesse dia.
		3 - Visualização do intervalo de dados em um limite final e inicial de mês/ano escolhido pelo usuário.
			3.1 - A visualização só pode ser feita entre a data de 01/01/1961 a 10/07/2016.
			3.2 - A visualização só pode ser feita em uma faixa de valores que o ano final seja maior que o ano incial, caso contrário exibirá a mensagem solicitando um ano maior.
			3.3 - É aceito apenas valores inteiros positivos para o mês e ano, qualquer entrada que não siga essa regra exibirá um erro, e solicitará uma entrada nova.
			3.4 - Há quatro formas de escolher a exibição do dados após de escolher o mês/ano, sendo elas:
			      3.4.1 - Todos os dados, fazendo a exibição de toda as colunas.
			      3.4.2 - Apenas a coluna de precipitação.
			      3.4.3 - Apenas a coluna de temperatura.
			      3.4.4 - Apenas a coluna de umidade e vento.
			      3.4.5 - A opção de sair e retorna ao menu de opções inicial.
	 
 		4 - Média da temperatura mínima de um determinado mês para todos os anos de uma faixa fixa de anos.
			4.1 - Apenas o meses de 01 a 07, e o ano de 2006 a 2016.
			4.2 - É aceito apenas valores inteiros positivos para o mês, qualquer entrada que não siga essa regra exibirá um erro, e solicitará uma entrada nova.
			4.3 - Criação de um gráfico de barras que exiba a média da temperatura mês a mês entre os anos de 2006 a 2016.
		
Vale salientar que o tratamento dos dados irá ignorar qualquer zero digitado a esquerda do numero, assim transforma 000123 em 123 o q gerará um erro caso esteja fora do limite máximo 
e mínimo, limite esse que corresponde ao parâmetro que é passado para a função, neste caso sendo o ano ou o mês, portanto só irá usar os dados na faixa de valor especificada.

Todo o projeto foi desenvolvido pelo Visual Studio Code, e para realizar o teste do código, tendo em vista a versão do python e das bibliotecas usadas, vou deixar o passo a passo de como
criar um ambiente virtual pelo Visual Studio Code com a versão correta do python e demais bibliotecas para evitar eventuais erros no código devido a novas atualizações.

Dowloand do visual studio code, siga os passos listados:

	1 - Acesse o site oficial do Visual Studio Code em https://code.visualstudio.com/
	2 - Clique no botão "Download" para baixar o instalador apropriado para o seu sistema operacional (Windows, macOS ou Linux).
	3 - Execute o instalador e siga as instruções para instalar o VS Code no seu computador.
	4 - Abra o VS Code após a instalação.

	Vá para a aba extensão  na barra lateral à esquerda e procure por "Python". Se você não encontrar essa aba você pode abrir usando ctrl+shift+x.

	Após instalar a extensão Python, você verá um ícone de engrenagem no canto superior direito do VS Code. Clique nele e selecione "Python: Select Interpreter". Isso permite que 		você escolha a versão do Python que deseja usar, mas para isso você precisa baixar a versão utlizada nesse projeto, para fazer isso acesse o site 					https://www.python.org/downloads/ e instale a versão python==3.11.4.

Para testar o código é necessário criar um ambiente virtual com as versões do python e das bibliotecas utilizadas no projeto, para isso copie e cole um a um o código a seguir no terminal
do VS code:

	Abra o terminal integrado no VS Code com o atalho Ctrl+`
	
	# Criando um ambiente virtual
	No macOS ou Linux:
	python3.11 -m venv myenv
	
	No Windows:
	python3.11 -m venv myenv
	
	
	
	# Ativando o ambiente virtual
	No macOS ou Linux:
	source myenv/bin/activate
	
	No Windows:
	.\myenv\Scripts\activate

	Obs.: Talvez o powershell não permita a ativação do ambiente, então execute os passos a seguir:

	1 - Abra o Prompt de Comando como administrador. Para fazer isso, pressione Win+X e escolha "Prompt de Comando 	(Admin)" no Windows, ou clique em win e pesquise por prompt de 
            comando, clique com o botão direito e execute como administrador.

	2 - Navegue até a pasta do seu ambiente virtual:
	cd caminho\para\pasta\Scripts (para isso vá até a pasta e clique com o botão direito na região do topo da página que exiba algo parecido com arquivos > nome da pasta).

	3 - Execute activate:
	activate

	Isso ativará o ambiente virtual usando o prompt de comando.

	# Instalando as dependências
	pip install -r requisitos.txt
	
	#execute o teste do arquivo
	python Analise_precipitação.py
	
	Após testar o código você pode desativar o ambiente virtual usando o comando deactivate no macOS e no Linux, ou .\myenv\Scripts\deactivate no Windows.
	
