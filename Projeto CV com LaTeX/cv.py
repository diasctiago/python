# -*- coding: utf-8 -*-

import os  

arquivo = open('cv.tex','w', encoding="utf8")
arquivo2 = open('config.cls','w', encoding="utf8")

cv = '''
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Resume/CV
% LaTeX Template
% Version 1.0 (24/04/2019)
% Adaptado por Tiago Costa Dias
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%----------------------------------------------------------------------------------------
%	PACKAGES AND OTHER DOCUMENT CONFIGURATIONS
%----------------------------------------------------------------------------------------

\documentclass[letterpaper]{config} % a4paper for A4

'''

print('-----------------------------------------')
print('|            DADOS PESSOAIS             |')
print('-----------------------------------------')
print('\n')

nome = input('Insira seu Nome: ')
cv = cv + '\n' + '\\cvname{' + nome + '}'

carreira = input('Insira sua Carreira: ')
cv = cv + '\n' + '\\cvjobtitle{' + carreira + '} '

linkedin = input('Insira seu Linkedin: ')
cv = cv + '\n' + '\\cvlinkedin{' + linkedin + '}'

telefone = input('Insira seu Telefone: ')
cv = cv + '\n' + '\\cvnumberphone{' + telefone + '} '

email = input('Insira seu Email: ')
cv = cv + '\n' + '\\cvmail{' + email + '}'

print('\n')

cv = cv + '\n\n' + '''
\\begin{document}

\makeprofile % Print the sidebar
'''

print('-----------------------------------------')
print('|               FORMAÇÃO                |')
print('-----------------------------------------')

print('\n')
print('Possui Formação Superior???')
formacao = input('(1 - Sim e 2 - Não): ')
	
if formacao == '1':
	cv = cv + '\n\n' + '''

	\section{Educação}

	\\begin{twenty} % Lista de formação
	'''

	escolaridade = input('Escolaridade \n 1-Graduação \n 2-Pós-Graduação \n 3-Mestrado \n 4-Doutorado \n Informe sua Escolaridade: ')
	print('\n')

	d = '1'
	if escolaridade == '4':
		while d == '1':
			print('Informe os dados do Doutorado')
			datad = input('Insira o Periodo (Ex.: 2018-2019): ')
			cv = cv + '	\t \\twentyitem' + '\n' + '{' + datad + '}'
			cursod = input('Insira o Curso: ')
			cv = cv + '\n' + '{' + cursod + '}'
			faculdaded = input('Insira a Faculdade: ')
			cv = cv + '\n' + '{' + faculdaded + '}'
			locald = input('Insira o Local (Ex.: Salvador BA)::: ')
			cv = cv + '\n' + '{' + locald + '}'
			trabalhod = input('Insira o Trabalho de Conclusão: ')
			cv = cv + '\n' + '{' + trabalhod + '}'
			d = input('Outro Doutorado (1 - Sim e 2 - Não): ')

	m = '1'
	if escolaridade == '4' or escolaridade == '3':
		while m == '1':
			print('Informe os dados do Mestrado')
			datam = input('Insira o Periodo (Ex.: 2018-2019): ')
			cv = cv + '	\t \\twentyitem' + '\n' + '{' + datam + '}'
			cursom = input('Insira o Curso: ')
			cv = cv + '\n' + '{' + cursom + '}'
			faculdadem = input('Insira a Faculdade: ')
			cv = cv + '\n' + '{' + faculdadem + '}'
			localm = input('Insira o Local (Ex.: Salvador BA)::: ')
			cv = cv + '\n' + '{' + localm + '}'
			trabalhom = input('Insira o Trabalho de Conclusão: ')
			cv = cv + '\n' + '{' + trabalhom + '}'
			m = input('Outro Mestrado (1 - Sim e 2 - Não): ')

	p = '1'
	if escolaridade == '4' or escolaridade == '3' or escolaridade == '2':
		while p == '1':
			print('Informe os dados da Pós-Graduação')
			datap = input('Insira o Periodo (Ex.: 2018-2019): ')
			cv = cv + '	\t \\twentyitem' + '\n' + '{' + datap + '}'
			cursop = input('Insira o Curso: ')
			cv = cv + '\n' + '{' + cursop + '}'
			faculdadep = input('Insira a Faculdade: ')
			cv = cv + '\n' + '{' + faculdadep + '}'
			localp = input('Insira o Local (Ex.: Salvador BA)::: ')
			cv = cv + '\n' + '{' + localp + '}'
			trabalhop = input('Insira o Trabalho de Conclusão: ')
			cv = cv + '\n' + '{' + trabalhop + '}'
			p = input('Outra Pós-Graduação (1 - Sim e 2 - Não): ')

	g = '1'
	if escolaridade == '4' or escolaridade == '3' or escolaridade == '2' or escolaridade == '1':
		while g == '1':
			print('Informe os dados da Graduação')
			datag = input('Insira o Periodo (Ex.: 2018-2019): ')
			cv = cv + '	\t \\twentyitem' + '\n' + '{' + datag + '}'
			cursog = input('Insira o Curso: ')
			cv = cv + '\n' + '{' + cursog + '}'
			faculdadeg = input('Insira a Faculdade: ')
			cv = cv + '\n' + '{' + faculdadeg + '}'
			localg = input('Insira o Local (Ex.: Salvador BA)::: ')
			cv = cv + '\n' + '{' + localg + '}'
			trabalhog = input('Insira o Trabalho de Conclusão: ')
			cv = cv + '\n' + '{' + trabalhog + '}'
			g = input('Outra Graduação (1 - Sim e 2 - Não): ')
		
	cv = cv + '\n\n' + '''
	\end{twenty}
	'''

print('-----------------------------------------')
print('|              EXPERIÊNCIA              |')
print('-----------------------------------------')

print('\n')
print('Possui Experiências???')
experiencias = input('(1 - Sim e 2 - Não): ')
print('\n')

if experiencias == '1':
	cv = cv + '\n\n' + '''

	\section{Experiência}

	\\begin{twenty} % Lista de formação
	'''

	print('Para um currículo objetivo informar as últimas 4 experiências em ordem cronológica decrescente!!!')
	print('\n')

	e = '1'
	while e == '1':
		print('Informe os dados da empresa')
		datae = input('Insira o Periodo (Ex.: 2018-2019): ')
		cv = cv + '	\t \\twentyitem' + '\n' + '{' + datae + '}'
		cargoe = input('Insira o Cargo: ')
		cv = cv + '\n' + '{' + cargoe + '}'
		empresae = input('Insira a Empresa: ')
		cv = cv + '\n' + '{' + empresae + '}'
		print('Resuma em 4 itens suas atividades')
		item1 = input('Atividades 1: ')
		item2 = input('Atividades 2: ')
		item3 = input('Atividades 3: ')
		item4 = input('Atividades 4: ')
		cv = cv + '\t\n' + '{}' + '\n' + '{' + '\\begin{itemize}'
		cv = cv + '\t\t\n' + '\item ' + item1
		cv = cv + '\t\t\n' + '\item ' + item2
		cv = cv + '\t\t\n' + '\item ' + item3
		cv = cv + '\t\t\n' + '\item ' + item4
		cv = cv + '\t\n' + '\end{itemize}' + '\n' +'}'
		e = input('Outra Experiência (1 - Sim e 2 - Não): ')

	cv = cv + '\n\n' + '''
	\end{twenty}
	'''

print('-----------------------------------------')
print('|              VOLUNTÁRIO               |')
print('-----------------------------------------')

print('\n')
print('Ja participou de programes de voluntários???')
voluntariados = input('(1 - Sim e 2 - Não): ')
print('\n')

if voluntariados == '1':
	cv = cv + '\n\n' + '''

	\section{Voluntário}

	\\begin{twenty} % Lista de Voluntariados
	'''

	print('Para um currículo objetivo informar as últimas 4 atividades voluntárias em ordem cronológica decrescente!!!')
	print('\n')

	v = '1'
	while v == '1':
		print('Informe os dados do ato voluntário')
		datav = input('Insira o Periodo (Ex.: 2018-2019): ')
		cv = cv + '	\t \\twentyitem' + '\n' + '{' + datav + '}'
		funcaov = input('Insira a Função: ')
		cv = cv + '\n' + '{' + funcaov + '}'
		empresav = input('Insira a Empresa: ')
		cv = cv + '\n' + '{' + empresav + '}'
		localv = input('Insira o Local (Ex.: Salvador BA)::: ')
		cv = cv + '\n' + '{' + localv + '}'
		print('Resuma em 2 itens suas atividades')
		item1 = input('Atividades 1: ')
		item2 = input('Atividades 2: ')
		cv = cv + '\t\n'  + '{' + '\\begin{itemize}'
		cv = cv + '\t\t\n' + '\item ' + item1
		cv = cv + '\t\t\n' + '\item ' + item2
		cv = cv + '\t\n' + '\end{itemize}' + '\n' +'}'
		v = input('Outro Voluntáriado (1 - Sim e 2 - Não): ')
		

	cv = cv + '\n\n' + '''
	\end{twenty}
	'''

print('-----------------------------------------')
print('|               IDIOMAS                 |')
print('-----------------------------------------')

print('\n')
print('Possui outros idiomas???')
idiomas = input('(1 - Sim e 2 - Não): ')
print('\n')

if idiomas == '1':
	cv = cv + '\n\n' + '''

	\section{Idiomas}

	\\begin{twenty} % Lista de Idiomas
	'''

	print('Informar os Idiomas!!!')
	print('\n')

	i = '1'
	while i == '1':
		print('Informações do Idioma')
		lingua = input('Insira o Idioma: ')
		cv = cv + '	\t \\twentyitem' + '\n' + '{}' + '\n' + '{' + lingua + '}'
		escola = input('Insira a Escola: ')
		cv = cv + '\n' + '{' + escola + '}'
		print('Informe os níveis em casa atividades')
		escrita = input('Nivel de Escrita (Básico | Intermediário | Avançado | Fluente): ')
		leitura = input('Nivel de Leitura (Básico | Intermediário | Avançado | Fluente): ')
		conversacao = input('Nivel de Conversação (Básico | Intermediário | Avançado | Fluente): ')
		cv = cv + '\t\n' + '{}' + '\n' +'{\\textit{Escrita: ' + escrita + ' | Leitura: ' + leitura + ' | Conversação: ' + conversacao + '}}'
		i = input('Outro Idioma (1 - Sim e 2 - Não): ')
		
	cv = cv + '\n\n' + '''
	\end{twenty}
	'''

print('-----------------------------------------')
print('|                CURSOS                 |')
print('-----------------------------------------')

print('\n')
print('Possui cursos na área???')
cursos = input('(1 - Sim e 2 - Não): ')
print('\n')

if cursos == '1':
	cv = cv + '\n\n' + '''

	\section{Cursos}

	\\begin{twenty} % Lista de Cursos
	'''

	print('Informar os Cursos mas relevantes para sua área!!!')
	print('\n')

	c = '1'
	while c == '1':
		print('Informações do Curso')
		cursoc = input('Insira o Curso: ')
		cv = cv + '	\t \\twentyitem' + '\n' + '{}' + '\n' + '{' + cursoc + '}'
		empresac = input('Insira a Empresa: ')
		cv = cv + '\n' + '{' + empresac + '}'
		print('Resuma em poucas palavras o conteudo do curso')
		conteudo = input('Conteudo do Curso: ')
		cv = cv + '\t\n' + '{}' + '\n' +'{\\textit{' + conteudo + '}}'
		c = input('Outro Curso (1 - Sim e 2 - Não): ')
		
	cv = cv + '\n\n' + '''
	\end{twenty}
	'''

cv = cv + '\n\n' + '''

\end{document}
'''

config = '''
\ProvidesClass{config}[2015/02/28 CV class]
\LoadClass{article}
\\NeedsTeXFormat{LaTeX2e}

%----------------------------------------------------------------------------------------
%	 REQUIRED PACKAGES
%----------------------------------------------------------------------------------------

\\RequirePackage[quiet]{fontspec}
\\RequirePackage[sfdefault]{ClearSans}
\\RequirePackage{tikz}
\\RequirePackage{xcolor}
\\RequirePackage[absolute,overlay]{textpos}
\\RequirePackage{ragged2e}
\\RequirePackage{etoolbox}
\\RequirePackage{ifmtarg}
\\RequirePackage{ifthen}
\\RequirePackage{pgffor}
\\RequirePackage{marvosym}
\\RequirePackage{parskip}

\\usepackage{enumitem}
\setlist[itemize]{leftmargin=*}

\\RequirePackage[hidelinks]{hyperref}
\hypersetup{
    pdftitle={},
    pdfauthor={},
    pdfsubject={},
    pdfkeywords={},
    colorlinks=false,           % no lik border color
    allbordercolors=white       % white border color for all
}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\\relax

\ifxetex
  \\usepackage{letltxmacro}
  \setlength{\\XeTeXLinkMargin}{1pt}
  \LetLtxMacro\SavedIncludeGraphics\includegraphics
  \def\includegraphics#1#{% #1 catches optional stuff (star/opt. arg.)
    \IncludeGraphicsAux{#1}%
  }%
  \\newcommand*{\IncludeGraphicsAux}[2]{%
    \\XeTeXLinkBox{%
      \SavedIncludeGraphics#1{#2}%
    }%
  }%
\\fi

%----------------------------------------------------------------------------------------
%	 COLOURS
%----------------------------------------------------------------------------------------

\definecolor{white}{RGB}{255,255,255}
\definecolor{gray}{HTML}{4D4D4D}
\definecolor{sidecolor}{HTML}{E7E7E7}
\definecolor{mainblue}{HTML}{0E5484}
\definecolor{maingray}{HTML}{B9B9B9}
\definecolor{pblue}{HTML}{0395DE}
\definecolor{darkgray}{HTML}{333333}
\definecolor{gray}{HTML}{4D4D4D}
\definecolor{lightgray}{HTML}{999999}
\definecolor{green}{HTML}{C2E15F}
\definecolor{orange}{HTML}{FDA333}
\definecolor{purple}{HTML}{D3A4F9}
\definecolor{red}{HTML}{FB4485}
\definecolor{blue}{HTML}{6CE0F1}
\definecolor{pblue}{HTML}{0395DE}
\definecolor{materialpurple}{HTML}{9C27B0}
\definecolor{materialindigo}{HTML}{3F51B5}
\definecolor{materialblue}{HTML}{2196F3}
\definecolor{materialcyan}{HTML}{00BCD4}
\definecolor{materialteal}{HTML}{009688}
\definecolor{materialgreen}{HTML}{4CAF50}
\definecolor{materiallime}{HTML}{CDDC39}
\definecolor{materialamber}{HTML}{FFC107}
\definecolor{materialbrown}{HTML}{795548}
\definecolor{materialred}{HTML}{FF4436}
\definecolor{materialorange}{HTML}{FF5722}

\ifdefined\@cv@print
  \colorlet{green}{gray}
  \colorlet{orange}{gray}
  \colorlet{purple}{gray}
  \colorlet{red}{gray}
  \colorlet{blue}{gray}
  \colorlet{fillheader}{white}
  \colorlet{header}{gray}
\else
  \colorlet{fillheader}{white}
  \colorlet{header}{gray}
\\fi
\colorlet{textcolor}{gray}
\colorlet{headercolor}{gray}

%----------------------------------------------------------------------------------------
%	 MISC CONFIGURATIONS
%----------------------------------------------------------------------------------------

% \\renewcommand{\\bfseries}{\color{black}} % Make \\textbf produce coloured text instead

\pagestyle{empty} % Disable headers and footers

\setlength{\parindent}{0pt} % Disable paragraph indentation

% --------------------------------------------------------------------------------------
% 	FONTS
%-------------------------------------------------------------------------------------

\\newfontfamily\headingfont[Path = fonts/]{segoeuib.ttf}

%----------------------------------------------------------------------------------------
%	 SIDEBAR DEFINITIONS
%----------------------------------------------------------------------------------------

\setlength{\TPHorizModule}{1cm} % Left margin
\setlength{\TPVertModule}{1cm} % Top margin

\\newlength\imagewidth
\\newlength\imagescale
\pgfmathsetlength{\imagewidth}{5cm}
\pgfmathsetlength{\imagescale}{\imagewidth/600}

\\newcommand{\profilesection}[2]{\\vspace{8pt}{\color{black!80} \huge #1 \\rule[0.15\\baselineskip]{#2}{1pt}}}

% Define custom commands for CV info
\\newcommand{\\cvdate}[1]{\\renewcommand{\\cvdate}{#1}}
\\newcommand{\\cvlinkedin}[1]{\\renewcommand{\\cvlinkedin}{#1}}
\\newcommand{\\cvmail}[1]{\\renewcommand{\\cvmail}{#1}}
\\newcommand{\\cvnumberphone}[1]{\\renewcommand{\\cvnumberphone}{#1}}
\\newcommand{\\cvaddress}[1]{\\renewcommand{\\cvaddress}{#1}}
\\newcommand{\\cvsite}[1]{\\renewcommand{\\cvsite}{#1}}
\\newcommand{\\aboutme}[1]{\\renewcommand{\\aboutme}{#1}}
\\newcommand{\profilepic}[1]{\\renewcommand{\profilepic}{#1}}
\\newcommand{\\cvname}[1]{\\renewcommand{\\cvname}{#1}}
\\newcommand{\\cvjobtitle}[1]{\\renewcommand{\\cvjobtitle}{#1}}

% Command for printing the contact information icons
\\newcommand*\icon[1]{\\tikz[baseline=(char.base)]{\\node[shape=circle,draw,inner sep=1pt, fill=mainblue,mainblue,text=white] (char) {#1};}}

% Command for printing skill progress bars
\\newcommand\skills{ 
	~
	\smartdiagram[bubble diagram]{
'''

print('\n')
print('-----------------------------------------')
print('|            CONHECIMENTOS              |')
print('-----------------------------------------')
print('\n')

bd = '1'
countc = 1
while bd == '1' and countc < 8:
	print('Informe no mínimo 1 e no máximo 7 áreas de conhecimentos!!!')
	conhecimento = input('Informe sua área de conhecimento: ')
	config = config + '\t\t' + '\\textbf{' + conhecimento + '}'
	bd = input('Outro Conhecimento (1 - Sim e 2 - Não): ')
	countc = countc + 1
	if bd == '1':
		config = config + ',' + '\n'

config = config + '''	
    }
}

% Command for printing skill progress bars
\\newcommand\interests[1]{ 
	\\renewcommand{\interests}{
		\\begin{tikzpicture}
			\\foreach [count=\i] \\x/\y in {#1}{
				\draw[fill=maingray,maingray] (0,\i) rectangle (6,\i+0.4);
				\draw[fill=white,mainblue](0,\i) rectangle (\y,\i+0.4);
				\\node [above right] at (0,\i+0.4) {\\x};
			}
		\end{tikzpicture}
	}
}

%----------------------------------------------------------------------------------------
%  SIDEBAR LAYOUT
%----------------------------------------------------------------------------------------

\\newcommand{\makeprofile}{
    \\begin{tikzpicture}[remember picture,overlay]
		\\node [rectangle, fill=sidecolor, anchor=north, minimum width=9cm, minimum height=\paperheight+1cm] (box) at (-5cm,0.5cm){};
    \end{tikzpicture}

    %------------------------------------------------

    \\begin{textblock}{6}(0.5, 0.2)

    %------------------------------------------------
    
    \\vspace{4mm}
    {\Huge\color{pblue}\\cvname}

    %------------------------------------------------
    
    {\Large\color{black!80}\\cvjobtitle}

    %------------------------------------------------
    
    \\vspace{5mm}
    \\renewcommand{\\arraystretch}{1.6}
    \\begin{tabular}{p{1cm} @{\hskip 0.5cm}p{5cm}}
        
        \ifthenelse{\equal{\\cvlinkedin}{}}{}{
            {$
              \\begin{array}{l}
              {\href{\\cvlinkedin}{\includegraphics[scale=0.04]{img/LinkedIn_Logo.png}}}
              \end{array}
              $} 
            & \href{\\cvlinkedin}{\hspace{16mm}/in/\\cvlinkedin} \\\}
        \ifthenelse{\equal{\\cvnumberphone}{}}{}{
            {$
              \\begin{array}{l}
              \includegraphics[scale=0.1]{img/tel.png}
              \end{array}
              $} 
            & \\cvnumberphone\\\}
        \ifthenelse{\equal{\\cvmail}{}}{}{
            {$
              \\begin{array}{l}
              {\href{mailto:\\cvmail}{\includegraphics[scale=0.05]{img/email.png}}}
              \end{array}
              $} 
            & \href{mailto:\\cvmail}{\\cvmail}}
    \end{tabular}
    %------------------------------------------------
        
        \profilesection{Conhecimentos}{1.35cm}

    	\skills
        
        %------------------------------------------------
        
        \profilesection{Interesses}{3cm} 
'''

print('\n')
print('-----------------------------------------')
print('|             INTERESSES                |')
print('-----------------------------------------')
print('\n')

config = config + '''	
		\interests{
'''

bd = '1'
counti = 1
while bd == '1' and counti < 5:
	print('Informe no mínimo 1 e no máximo 5 áreas de interesse!!!')
	interesse = input('Informe sua área de intesse: ')
	niveli = input('Informe seu nivel de intesse (1-Muito pouco | 2-Pouco | 3-Médio | 4-Alto | 5-Muito alto | 6-Total): ')
	config = config + '\t\t' + '{' + interesse + '/' + niveli + '}'
	bd = input('Outro Conhecimento (1 - Sim e 2 - Não): ')
	counti = counti + 1
	if bd == '1':
		config = config + ',' +'\n'

config = config + '''}
		\interests
'''

config = config + '''	
        \profilesection{Ferramentas}{2.28cm} 

		\\begin{tikzpicture}[font=\sffamily\\bfseries\large, 
			 text=gray, 
			 border/.style={line width=14mm}]
		\\foreach \\angle/\col [remember=\\angle as \last (initially 0)] in 
			{90/blue, 125/cyan, 160/green!30!black, 210/green, 270/orange, 360/red}{
				\draw[\col, border] (\last:1.5cm) 
					 arc[start angle=\last, end angle=\\angle, radius=1.5cm];
				\draw[white, line width=1mm] (\last:1)--++(\last:1.2);
		}
'''

print('\n')
print('-----------------------------------------')
print('|             FERRAMENTAS               |')
print('-----------------------------------------')
print('\n')

print('Resuma as 7 ferramentas tecnológicas da que você mais domina a que tem conhecimento mais domina pouco!!!')
ferramenta1 = input('Informa a Ferramenta que você mais domina: ')
ferramenta2 = input('Informa a Ferramenta que você é tão bom quanto a primeira: ')
ferramenta3 = input('Informa a Ferramenta que você sabe muito: ')
ferramenta4 = input('Informa a Ferramenta que você ta evoluindo: ')
ferramenta5 = input('Informa a Ferramenta que você ja estudou: ')
ferramenta6 = input('Informa a Ferramenta que você não domina tanto: ')
ferramenta7 = input('Informa a Ferramenta que você menos domina: ')
config = config + '\n\t\t' + '\\node[line width=1mm, draw, circle, minimum width=2cm, white, fill=blue!80] {' + ferramenta1 + '};'
config = config + '\n\t\t' + '\\node at (45:1.6cm)  {' + ferramenta2 + '};'
config = config + '\n\t\t' + '\\node at (-45:1.6cm) {' + ferramenta3 + '};'
config = config + '\n\t\t' + '\\node at (240:2cm)   {' + ferramenta4 + '};'
config = config + '\n\t\t' + '\\node at (185:2cm)   {' + ferramenta5 + '};'
config = config + '\n\t\t' + '\\node at (143:2cm)   {' + ferramenta6 + '};'
config = config + '\n\t\t' + '\\node at (108:2cm)   {' + ferramenta7 + '};'

config = config + '''	
		\end{tikzpicture}

	\end{textblock}
}

%----------------------------------------------------------------------------------------
%	 COLOURED SECTION TITLE BOX
%----------------------------------------------------------------------------------------

% Command to create the rounded boxes around the first three letters of section titles
\\newcommand*\\round[2]{%
	\\tikz[baseline=(char.base)]\\node[anchor=north west, draw,rectangle, rounded corners, inner sep=1.6pt, minimum size=5.5mm, text height=3.6mm, fill=#2,#2,text=white](char){#1};%
}

\def\@sectioncolor#1#2#3{%
	{%
		\color{pblue} #1#2#3%
	}%
}

\\renewcommand{\section}[1]{
  \par\\vspace{\parskip}
	{%
		\LARGE\headingfont\color{headercolor}%
		\@sectioncolor #1%
	}
  \par\\vspace{\parskip}
}

\\renewcommand{\subsection}[1]{
	\par\\vspace{.5\parskip}{%
		\Large\headingfont\color{headercolor} #1%
	}
	\par\\vspace{.25\parskip}%
}

\pagestyle{empty}

%----------------------------------------------------------------------------------------
%	 LONG LIST ENVIRONMENT
%----------------------------------------------------------------------------------------

\setlength{\\tabcolsep}{0pt}

% New environment for the long list
\\newenvironment{twenty}{%
	\\begin{tabular*}{\\textwidth}{@{\extracolsep{\\fill}}ll}
}{%
	\end{tabular*}
}

\\newcommand{\\twentyitem}[5]{%
	#1&\parbox[t]{0.83\\textwidth}{%
		\\textbf{#2}% 
		\hfill%
		{\\footnotesize#3}\\\%
        \ifblank{#4}{}{#4 \\\}
		#5\\vspace{\parsep}%
	}\\\\
}

%----------------------------------------------------------------------------------------
%	 SMALL LIST ENVIRONMENT
%----------------------------------------------------------------------------------------

\setlength{\\tabcolsep}{0pt}

% New environment for the small list
\\newenvironment{twentyshort}{%
	\\begin{tabular*}{\\textwidth}{@{\extracolsep{\\fill}}ll}
}{%
	\end{tabular*}
}

\\newcommand{\\twentyitemshort}[2]{%
	#1&\parbox[t]{0.83\\textwidth}{%
		#2%
	}\\\\
}

%----------------------------------------------------------------------------------------
%	 MARGINS AND LINKS
%----------------------------------------------------------------------------------------

\\RequirePackage[left=7.6cm,top=0.1cm,right=1cm,bottom=0.2cm,nohead,nofoot]{geometry}

\\usepackage{smartdiagram}
\smartdiagramset{
    bubble center node font = \\footnotesize,
    bubble node font = \\footnotesize,
    % specifies the minimum size of the bubble center node
    bubble center node size = 0.5cm,
    %  specifies the minimum size of the bubbles
    bubble node size = 0.5cm,
    % specifies which is the distance among the bubble center node and the other bubbles
    distance center/other bubbles = 0.3cm,
    % sets the distance from the text to the border of the bubble center node
    distance text center bubble = 0.5cm,
    % set center bubble color
    bubble center node color = pblue,
    % define the list of colors usable in the diagram
    set color list = {lightgray, materialcyan, orange, green, materialorange, materialteal, materialamber, materialindigo, materialgreen, materiallime},
    % sets the opacity at which the bubbles are shown
    bubble fill opacity = 0.6,
    % sets the opacity at which the bubble text is shown
    bubble text opacity = 1,
}
'''

arquivo.write(cv)
arquivo.close()

arquivo2.write(config)
arquivo2.close()

os.system("xelatex cv.tex")
os.system("cv.pdf")

os.system("del cv.aux")
os.system("del cv.log")
os.system("del cv.out")
os.system("del cv.tex")
os.system("del config.cls")