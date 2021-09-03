import os
import random
import script_renovacao

meses = [
	"janeiro",
	"fevereiro",
	"marco",
	"abril",
	"maio",
	"junho",
	"julho",
	"agosto",
	"setembro",
	"outubro",
	"novembro",
	"dezembro"
]

meses_acento = [
	"janeiro",
	"fevereiro",
	"março",
	"abril",
	"maio",
	"junho",
	"julho",
	"agosto",
	"setembro",
	"outubro",
	"novembro",
	"dezembro"
]

eventos = [
	'Vestibular Insper',
	'FUVEST',
	'Vestibular UNICAMP',
	'Prazo de inscrição Insper',
	'Prazo de inscrição FUVEST',
	'Segunda fase vestibular do Zé',
	'Rolê no Sujus',
	'Rolezinho do Neymar',
	'Prazo de inscrição vestibular X'
]

base_html = '''<!-- Representa a página da agenda do mês de %s -->

<!DOCTYPE html>

<html lang="pt-BR">

    <head>  <!-- cláusula de metadados -->
        <title>STUDYING - Agenda %s</title>
        <meta charset="UTF-8">
    </head>

    <body> <!-- cláusula de conteúdo -->

        <img src="../recursos/icone_menu.jpg" alt="Link do Menu (WIP)" height="50" width="50">  <!-- imagem do link do menu, não tem função ainda -->
        
        <h1> <a href="pagina_principal.html"> STUDYING </a> </h1>    <!-- título do aplicativo -->

        <h3> <a href="agenda.html"> AGENDA </a> </h3>

        <h4> %s </h4>

        <ul>   <!-- lista de opções -->
            <li> Dia %d: %s </li>
            <li> Dia %d: %s </li>
        </ul>

    </body>

</html>
'''

for i in range(12):

	dias = [random.randint(1, 29), random.randint(1, 29)]
	dias.sort()

	conteudo = (
		meses_acento[i],
		meses_acento[i].title(),
		meses_acento[i].title(),
		dias[0],
		random.choice(eventos),
		dias[1],
		random.choice(eventos)
	)

	html = base_html % conteudo

	with open('html/agenda_%s.html' % meses[i], 'x') as file: file.write(html)



