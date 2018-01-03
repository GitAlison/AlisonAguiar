import urllib.request
import time
rep = 99
while rep >=2:
	pagina = urllib.request.urlopen('https://www12.senado.leg.br/ecidadania/visualizacaomateria?id=129022&voto.html')
	texto = pagina.read().decode('utf8')

	paginafavor = texto.find('contabilizacao-favor')
	paginacontra = texto.find('contabilizacao-contra')

	inicio = paginafavor + 22
	fim = inicio + 7

	inicio2 = paginacontra + 23
	fim2 = inicio2 +7

	afavor= float(texto[inicio:fim])
	contra = float(texto[inicio2:fim2])
	if afavor < contra:
		diferencia = contra - afavor
	else:
		diferencia =  afavor - contra
	

	if afavor != 2 or contra != 2:
		time.sleep(1)
		print('==================================================================')
		print('============           SENADO FEDERAL              ===============')
		print('==================================================================')
		print(' CONSULTA PÚBLICA')
		print(' SUG 11/2017')
		print(' SUGESTÃO nº 11 de 2017')
		print('==================================================================')
		print(" Ementa Anistia ao Senhor Deputado Federal Jair Messias Bolsonaro")
		print(" Anistia ao Bolsonaro no caso Maria do Rosário")
		print(" 	")
		
		print('     Votos A favor 		--->:    ',afavor,'  Votos ')
		print('     Votos Contra 		--->:    ',contra,'  Votos ')
		print('     Diferença de votos         --->:      %.3f'%diferencia,'  Votos ')
		print('==================================================================')
#print('Contra',paginacontra)