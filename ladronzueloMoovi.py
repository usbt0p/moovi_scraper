from bs4 import BeautifulSoup
import csv

'''Coloca aquí o path do teu ficheiro de html
A poder ser, non descargues nen lle deas a 'guardar como' para evitar problemas de formateado.
No seu lugar, unha vez no exame escribe na barra de busca 'view-source' ao principio da query:
    view-source:https://moovi.uvigo.gal/mod/quiz/review.php...
Dalle a Ctrl+A para seleccionalo todo, cópiao e pégao nun arquivo html no directorio no que o vaias ler.'''

path = 'ficheiros_preguntas/ex2_copiafirefox.html'

# O nome do novo ficheiro procesado: pon o teu nome e apelidos ou algún nome único para que non se repitan
# O output será un csv
newfile_name = 'ficheiros_preguntas/lucasc2.csv' 

with open(path, encoding='utf-8') as html_file:
    content = html_file.read()
    page = BeautifulSoup(content, 'html.parser')
    
    # Por se algún test futuro ten mais de 10 preguntas...
    num_preguntas = len(page.find_all('div', class_ = 'qtext'))

    with open(newfile_name, "w", newline="", encoding='utf-8') as csvfile:

        writer = csv.writer(csvfile, delimiter='\t')
        columnames = ['pregunta', 'opcion', 'resposta', 'feedback']
        writer.writerow(columnames)  # Escribir nomes das columnas

        for i in range(num_preguntas):

            # Colle as preguntas e opcións do div parent
            formulation = page.find_all('div', class_ = 'formulation clearfix')

            preguntas = formulation[i].find('div', class_ = 'qtext')

            opciones = formulation[i].find_all('div', class_ = 'flex-fill ml-1')
            opciones = [elem.text for elem in opciones]

            linequestions = [preguntas.text, opciones]

            # Colle a sección coa pregunta e feedback, e inclúe o feedback se a pregunta o ten 
            feedback = page.find_all('div', class_ = 'feedback')
            
            generalfeedback = feedback[i].find('div', class_ = 'generalfeedback')
            respostas = feedback[i].find('div', class_ = 'rightanswer')

            if generalfeedback != None:
                linequestions.extend([respostas.text, generalfeedback.text])
            else:
                linequestions.extend([respostas.text , 'None'])

            writer.writerow(linequestions)
                        
        

