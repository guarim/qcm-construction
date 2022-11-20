import PyPDF3 
import pikepdf
import fitz
from time import time 

FILE = "/home/fenarius/Travail/Cours/fabricenativel.github.io/docs/Premiere/files/Projets/forcebrute/suivi_projet_protege.pdf"
READER = PyPDF3.PdfFileReader(FILE)
DOC = fitz.Document(FILE)


def test_password(file,password):    
    test_decode = READER.decrypt(password)
    return test_decode==1

def tp(file,password):
    try :
        pikepdf.open(FILE,password=password)
        return True
    except :
        return False

def tp3(file,password):
    return DOC.authenticate(password)

debut = time()
for i in range(1,10000):
    if tp3(FILE,str(i).zfill(4)):
        print(f"Mot de passe trouvé : {str(i).zfill(4)}")
fin = time()

print(fin-debut)

