## O ladronzuelo de Moovi

Executa o script seguindo as instruccións para sacar as preguntas de exames de Moovi (polo menos os de Redes, igual o resto non funcionan):

1. Clona o repositorio ou descarga o zip (no botón verde arriba á dereita), ou mesmo descarga o script por separado.
2. Crea un ficheiro ``HTML`` no teu directorio.
3. Vai ao exame de Moovi, non descargues nen lle deas a 'guardar como' para evitar problemas de formateado. No canto, unha vez no exame escribe na barra de busca 'view-source' ao principio da query (como se indica aquí):
    ``view-source:https://moovi.uvigo.gal/mod/quiz/review.php...``
Dalle a Ctrl+A para seleccionalo todo, cópiao e pégao no aquivo ``HTML`` no directorio no que o vaias ler.
4. Pon no script o ``path`` correcto do arquivo ``HTML`` e o nome do arquivo que se vai crear, que será un ``.csv`` e execútao.
5. O teu ficheiro coas preguntas e respostas crearase, e xa debería estar todo. Se hai algún problema escríbeme ou abre un issue. 👺🤝