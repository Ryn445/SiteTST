import pyautogui
import clipboard
import time
from PIL import ImageGrab
from functools import partial
import selenium
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
import urllib3
import re
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# CIDADES QUE ESTÃO NO RESSOA
capitais = ["BRASÍLIA", "BRASILIA", "RIO DE JANEIRO", "SÃO PAULO", "SAO PAULO", "SALVADOR", "BELO HORIZONTE", "FORTALEZA", "CURITIBA", "RECIFE",
    "PORTO ALEGRE", "MANAUS", "BELÉM", "BELEM", "GOIÂNIA", "GOIANIA", "CUIABÁ", "CUIABA", "CAMPO GRANDE", "NATAL", "TERESINA", "JOÃO PESSOA", "JOAO PESSOA",
    "SÃO LUÍS", "SAO LUIS", "SÃO LUIS", "MACEIO", "MACEIÓ", "ARACAJU", "VITÓRIA", "VITORIA", "FLORIANÓPOLIS", "FLORIANOPOLIS", "PALMAS", "MACAPÁ", "MACAPA",
    "RIO BRANCO", "PORTO VELHO", "BOA VISTA",  "GENEBRA", "LISBOA" ]




def verifica_capital(texto):
    texto_maiusculo = texto.upper()  
    for capital in capitais:
        if capital in texto_maiusculo:
            return True
    return False

def extrair_valor_monetario(texto):
    
    padrao = r'\d{1,3}(?:\.\d{3})*,\d{2}'
    
   
    resultado = re.search(padrao, texto)
    
    if resultado:
        return resultado.group()
    else:
        return 0
    

TOTAL  = input("informe a quantidade de páginas no pdf\n")
contPag = 0
indice = 0
listaGeral = []
contadorListaLocal = 0
while contPag < int(TOTAL):
 contPag += 1
 print("Pagina: " + str(contPag))   
 if contPag > 1:
  pyautogui.press('right') 
 pyautogui.click(2019,363)
 clipboard.copy(' - ')
 pyautogui.hotkey('Ctrl','a')
 pyautogui.hotkey('ctrl', 'c')
 time.sleep(1)
 texto = clipboard.paste()

 # array = texto.split("CTTRSPRQ")
 array= texto.split("Relatório: Transparência")
 cont = 0
 
 for parte in array:
  parte = parte.replace(" \n", "\n")  
  parte = parte.replace("CAMPO\r\n", "CAMPO ")
  parte = parte.replace("RIO DE\r\n", "RIO DE ")
  parte = parte.replace("CAXIAS DO\r\n", "CAXIAS DO ")
  parte = parte.replace("CAXIAS\r\n", "CAXIAS ")
  parte = parte.replace("BELO\r\n", "BELO ")
  parte = parte.replace("PORTO\r\n", "PORTO ")
  parte = parte.replace("JOÃO\r\n", "JOÃO ")
  parte = parte.replace("SÃO\r\n", "SÃO ")
  parte = parte.replace("RIO\r\n", "RIO ")
  parte = parte.replace("LISBOA\r\n", "LISBOA.\r\n")
  parte = parte.replace("BOA\r\n", "BOA ")
  parte = parte.replace("/\r\n", "/")
  parte = parte.replace("MARABA", "BELÉM")
  parte = parte.replace("MARABÁ", "BELÉM")
  parte = parte.replace("CAMPINAS", "SÃO PAULO")
  parte = parte.replace("MARINGA", "CURITIBA")
  parte = parte.replace("MARINGÁ", "CURITIBA")
  parte = parte.replace("NAVEGANTES", "FLORIANÓPOLIS")
  parte = parte.replace("CAXIAS DO SUL", "PORTO ALEGRE")
  periodo = parte.split("Período : ")   
   
  cont += 1   
  if (cont == 1):
   continue
  parte2 = periodo[1]
  pagina = parte2.split("\n")
  contPeriodo = 0
  for pg in pagina:
   pg = pg.replace("Cargo Documento Autorizador", "")   
   contPeriodo += 1 
   if contPeriodo == 1:
    continue
   if verifica_capital(pg) and "/" in pg and len(pg) > 12 and "ATO" not in pg and "ADMINISTRATIVA" not in pg:
    listaGeral.append(pg)    
    # print(pg)   
    indice += 1     
    
   elif extrair_valor_monetario(pg) != 0:
     novoValor = extrair_valor_monetario(pg) + "#" + str(listaGeral[contadorListaLocal]).replace("\r", "")  
     listaGeral[contadorListaLocal] =  novoValor 
     contadorListaLocal += 1  

for lista in listaGeral:
    dados = lista.split("#")
    partes = dados[1].split("/")
    if len(partes) == 2:
        # Caso haja duas partes
        variavel1 = partes[0].strip()
        variavel2 = partes[1].strip()
    elif len(partes) == 3:
        # Caso haja três partes
        variavel1 = partes[0].strip()
        variavel2 = partes[1].strip()
    else:
        # Caso haja apenas uma parte
        variavel1 = partes[0].strip()
        variavel2 = ""

    # O dados[0] sempre vai para variavel3
    variavel3 = dados[0].strip()

   
    print(f"\nvariavel1: {variavel1}")
    print(f"variavel2: {variavel2}")
    print(f"variavel3: {variavel3}")
