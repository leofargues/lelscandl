# librairie
import requests
from colorama import Fore, Back, Style
import zipfile
import os
# definir la fonction de téléchargement
urldwl = ""
filename = "file1"
def downloadimg():
    img_data = requests.get(urldwl).content
    with open(filename + '.jpg', 'wb') as handler:
        handler.write(img_data)
print(r"""
   _____                    __      ________          _     _____  _      
  / ____|                   \ \    / /  ____|        | |   |  __ \| |     
 | (___   ___ __ _ _ __ _____\ \  / /| |__ _ __   ___| |_  | |  | | |     
  \___ \ / __/ _` | '_ \______\ \/ / |  __| '_ \ / _ \ __| | |  | | |     
  ____) | (_| (_| | | | |      \  /  | |_ | | | |  __/ |_  | |__| | |____ 
 |_____/ \___\__,_|_| |_|       \/   |_(_)|_| |_|\___|\__| |_____/|______|                                                                                                                                                    
""")
print("Scan-VF.net Downloader version 0.2")
print("https://github.com/leofargues/scanvf-net-dl")
patchnote = "y"
if patchnote == "y":
    print("")
    print(">> Quoi de neuf ?")
    print("La version 0.2 apporte : ")
    print("- L'ajout des fichier .cbz")
    print("- Une compatibilité avec les liseuses et app de scan (grâce au .cbz)")
    print("- Une plus belle UI")
    print("")
    print("Pour supprimer ce message, supprimer le code la ligne 22 à 31")
print("")
#weburl = "https://www.scan-vf.net/uploads/manga/"
#manga = input("Manga name : ")
#chapter = input()
weburl = "https://www.scan-vf.net/uploads/manga/"
print("Nom du", Fore.RED + 'manga', Style.RESET_ALL + ' (dans un format type : jujutsu-kaisen) : ')
manga = input()
print("Quel", Fore.RED + 'chapitre', Style.RESET_ALL + ' : ')
chapter = input()
print("Combien", Fore.RED + 'pages', Style.RESET_ALL + ' : ')
pages = int(input())
# valeur numérique pour les boucles for et autres
#pages = int(input("Nombre de page : "))
# valeur textuel pour la génération d'une url
pagestourl = str(pages)
print("")
actualpage = 1
actualpagefilename = 1

for x in range(pages):
    if actualpage == 1:
        actpagetxt = str(actualpage)
        actfilename = str(actualpagefilename)
        filename = (manga + " page " + actfilename) 
        print(Fore.RED + 'Page', Style.RESET_ALL + actfilename, "téléchargée")
        urldwl = (weburl + manga + "/chapters/chapitre-" + chapter + "/0" + actpagetxt + ".webp")
        downloadimg()
        actualpage = actualpage + 3
        actualpagefilename = actualpagefilename + 1
    else:
        if actualpage <= 9:
            actpagetxt = str(actualpage)
            actfilename = str(actualpagefilename)
            filename = (manga + " page " + actfilename) 
            print(Fore.RED + 'Page', Style.RESET_ALL + actfilename, "téléchargée")
            urldwl = (weburl + manga + "/chapters/chapitre-" + chapter + "/0" + actpagetxt + ".webp")
            downloadimg()
            actualpage = actualpage +  1
            actualpagefilename = actualpagefilename + 1
        else:
           actpagetxt = str(actualpage)
           actfilename = str(actualpagefilename)
           filename = (manga + " page " + actfilename) 
           print(Fore.RED + 'Page', Style.RESET_ALL + actfilename, "téléchargée")
           urldwl = (weburl + manga + "/chapters/chapitre-" + chapter + "/" + actpagetxt + ".webp")
           downloadimg()
           actualpage = actualpage +  1 
           actualpagefilename = actualpagefilename + 1
mangazip = manga.replace("-", " ")
if os.path.exists(mangazip + " " + chapter + '.zip'):
    print("Ce fichier existe déja")
    zipcompleted = 0
    format = "Zip"
    print("Fichier téléchargé au format " + format + ".")
else :
    handle = zipfile.ZipFile(mangazip + " " + chapter + '.zip', 'w')
    for x in os.listdir():
        if x.endswith('.jpg'):
            handle.write(x, compress_type = zipfile.ZIP_DEFLATED)
    handle.close()
    zipcompleted = 1
if zipcompleted == 1:
    zipname = (mangazip + " " + chapter + '.zip')
    zipname2 = (mangazip + " " + chapter + '.cbz')
    print("")
    if os.path.exists(mangazip + " " + chapter + '.cbz'):
        print("Un fichier du nom de " + zipname2 + " existe déja, conversion annulée")
        format = "Zip"
    else:
        os.rename(zipname, zipname2)
        format = "Cbz"
    print("")
    print("Fichier téléchargé au format " + format + ".")
test = os.listdir()
for item in test:
    if item.endswith(".jpg"):
        os.remove(os.path.join(item))
