import os
import mammoth

def convertWordDocToHTML(filename):
    path = os.getcwd() + "\\CountyWebsite\\news\\" + filename
    with open(path, "rb") as file:
        result = mammoth.convert_to_html(file)
        html = result.value
    return html