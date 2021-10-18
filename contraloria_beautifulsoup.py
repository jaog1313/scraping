from urllib.request import urlopen
from bs4 import BeautifulSoup
def scrap_url(url, id_number, type_id)
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    bsObj = BeutifulSoup(html)
    namelist = bsObj.findAll(id="ddTipoDocumento")
    

if __name__ == "__main__":
    url = "https://www.contraloria.gov.co/control-fiscal/responsabilidad-fiscal/control-fiscal/responsabilidad-fiscal/certificado-de-antecedentes-fiscales/persona-natural"
    id_number = 123456789
    n = len(sys.argv)
    if(n==1):
        scrap_url(url, id_number, "1")
    elif(n==2):
        if(re.search(".csv", sys.argv[1])!=None):
            print("Read the database")
        else:
            scrap_url(url, sys.argv[1], "1")
    elif(n==3):
            scrap_url(url, sys.argv[1], sys.argv[2])