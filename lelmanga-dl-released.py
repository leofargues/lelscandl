import requests
from bs4 import BeautifulSoup
import os
import zipfile
def downloading():
    img_data = requests.get(finalimage[queue]).content
    with open("manga" + strqueue + '.jpg', 'wb') as handler:
        handler.write(img_data)

validurl = 0
while validurl == 0:    
    manga = input("Nom du manga : ")
    mangabrut = manga
    chapitre = input("Chapitre : ")
    manga = manga.replace(" ", "-")
    print("1 - Chapitre / 2 - Volume")
    type = input()
#url = 'https://www.lelmanga.com/jujutsu-kaisen-1'
#url = 'https://www.lelmanga.com/one-punch-man-262'
    print("Téléchargement en cours")
    url = ("https://www.lelmanga.com/" + manga + "-" + chapitre)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    check = (soup.title.string)
    if 'not' in check:
        print("")
        print("Si tu vois ce message, tu a peut être mal écrit le titre du manga (ne pas")
        print("mettre le - mais un espace) ou choisis un chapitre qui n'existe pas")
        print("")
    else:
        validurl = 1
if type == "1":
    type = "chapitre"
elif type == "2":
    type = "volume"
else:
    type = ""
images = soup.find_all('img')
allimglist = []
for image in images :
    link = (image['src'])
    allimglist.append(link)
finalimage = []

queue = 0
lenght = len(allimglist)
queue = 0
for i in range(lenght):
    if '?' in allimglist[queue]:
        #print(allimglist[queue])
        queue = queue + 1
    elif 'logo' in allimglist[queue]:
        #print(allimglist[queue])
        queue = queue + 1
    elif 'blogspot' in allimglist[queue]:
        #print(allimglist[queue])
        queue = queue + 1
    elif 'themes' in allimglist[queue]:
        #print(allimglist[queue])
        queue = queue + 1
    else:
        #print(queue)
        pages = allimglist[queue]
        finalimage.append(pages)
        queue = queue + 1
#print(len(finalimage))

queue = 0
for x in range(len(finalimage)):
    #print(finalimage[queue])
    queueforname = queue + 1
    strqueue = str(queueforname)
    downloading()
    queue = queue + 1

handle = zipfile.ZipFile(mangabrut + " " + chapitre + '.zip', 'w')
for x in os.listdir():
    if x.endswith('.jpg'):
        handle.write(x, compress_type = zipfile.ZIP_DEFLATED)
handle.close()

zipname = (mangabrut + " " + "type" + chapitre + '.zip')
zipname2 = (mangabrut + " " + "type" + chapitre + '.cbz')
os.rename(zipname, zipname2)
format = "Cbz"

test = os.listdir()
for item in test:
    if item.endswith(".jpg"):
        os.remove(os.path.join(item))   
print("Le fichier", zipname2, "a été téléchargé")
print("Il contient", len(finalimage), "fichier")
print("téléchargement complété")
