import os

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

for mes in meses: os.system('rm html/agenda_%s.html' % mes)
