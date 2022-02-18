import os
import subprocess

def foldernamefinder(githuburl):
    githuburl.split("/")
    print(githuburl)

githuburl = "https://github.com/LunaAstris16/testing.git"
folderName = foldernamefinder(githuburl)

#subprocess.run("git", "clone", str(githuburl))

#lsoutput = os.popen("ls").read().split("\n")
#for i in range(len(lsoutput)):
#    if lsoutput == 

#while True:
#    os.chdir()
