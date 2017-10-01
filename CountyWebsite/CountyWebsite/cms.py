import os
import mammoth
from CountyWebsite import database

def convertWordDocToHTMLFile(filename, id):
    path = os.getcwd() + "\\CountyWebsite\\news\\" + filename
    with open(path, "rb") as file:
        result = mammoth.convert_to_html(file)
        html = result.value
    with open(os.getcwd() + 'newsStories\\newsPart1.html', 'r') as part1:
        htmlPart1 = part1.read()
    with open(os.getcwd() + 'newsStories\\newsPart1.html', 'r') as part2:
        htmlPart2 = part2.read()

    fullFile = part1 + html + part2
    headline = database.getHeadline(id)
    with open(os.getcwd() + 'CountyWebsite\\newsPage\\' + headline + '.html', 'r') as file:
        file.write(fullFile)
    