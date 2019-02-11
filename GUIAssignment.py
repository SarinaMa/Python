#Assignment7-GUI about dictionary

#inport modules
import tkinter
import os
import sys
import requests
import json
import pygame
import urllib

#function declaration
def check(a):
    i=0
    for var in range(0,len(a)):
        if a[var]["lexicalCategory"]=="Adjective" or a[var]["lexicalCategory"]=="Adverb" or a[var]["lexicalCategory"]=="Verb":
            i=i+1
    if i!=0:
        return True
    else:
        return False
def SearchFunc():
    #print (keyword.get())
    printout.set(keyword.get())
    app_id = '0a4aedf4'
    app_key = 'b4379c0d5e1270781bf4450799782a09'

    language = 'en'
    word_id =keyword.get()

    url1 = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
    r1 = requests.get(url1, headers = {'app_id': app_id, 'app_key': app_key})
    dic1=r1.json()
    #print("text \n" + r1.text)
    

    if check(dic1["results"][0]["lexicalEntries"])==True:
        url2 = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower() + '/synonyms;antonyms'
        r2 = requests.get(url2, headers = {'app_id': app_id, 'app_key': app_key})
        dic2=r2.json()
        #print("text \n" + r2.text)
        url3 = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower() + '/synonyms;antonyms'
        r3 = requests.get(url3, headers = {'app_id': app_id, 'app_key': app_key})
        dic3=r3.json()
#synonyms:
        an="Antonyms are: \n"
        for var in range(0,len(dic2['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['antonyms'])):
            an=an+str(dic2['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['antonyms'][var]['text'])+'\n'       
#antonyms:
        sy="Synonyms are: \n"
        for var in range(0,len(dic2['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms'])):
            sy=sy+str(dic2['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms'][var]['text'])+'\n'
        #antonyms.set(an)
        #synonyms.set(sy)
#rhyme with the word:
    
#sentence:
        st="Sentence are: \n"
        for var in range(0,len(dic3['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'])):
            st=st+str(dic3['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][var]['text'])+'\n'
        #sentence.set(st)
    else:
        an=''
        sy=''
        st=''
        print('it is a N')
    antonyms.set(an)
    synonyms.set(sy)
    sentence.set(st)
    
    #print("text \n" + r3.text)
    #print("code {}\n".format(r.status_code))
    #print("text \n" + r.text)
    #print("json \n" + json.dumps(r.json()))
    #print(dic["results"][0]["lexicalEntries"][0]["entries"][0]["senses"])
    
#definitions:
    temp=""
    for var in range(0,len(dic1["results"][0]["lexicalEntries"])):
        #print (dic["results"][0]["lexicalEntries"][var]["lexicalCategory"])
        temp=temp+(str(dic1["results"][0]["lexicalEntries"][var]["lexicalCategory"])+": \n")
        for i in range(0,len(dic1["results"][0]["lexicalEntries"][var]["entries"][0]["senses"])):
            #print ("definition",(i+1),"is: "+str(dic["results"][0]["lexicalEntries"][var]["entries"][0]["senses"][i]["definitions"][0]))
            temp=temp+("Definition "+str(i+1)+" is: \n"+str(dic1["results"][0]["lexicalEntries"][var]["entries"][0]["senses"][i]["definitions"][0])+"\n")
    definitions.set(temp)
#etymologies:
    #print("etymologies is: "+str(dic["results"][0]["lexicalEntries"][0]["entries"][0]["etymologies"][0]))
    if dic1["results"][0]["lexicalEntries"][0]["entries"][0].get('etymologies')!=None:
        etymologies.set("Etymologies is: \n"+str(dic1["results"][0]["lexicalEntries"][0]["entries"][0]["etymologies"][0]))
#phonetic spelling:
    #print("phonetic spelling is: "+str(dic["results"][0]["lexicalEntries"][0]["pronunciations"][0]["phoneticSpelling"]))
    phonetic.set("Phonetic spelling is: \n"+str(dic1["results"][0]["lexicalEntries"][0]["pronunciations"][0]["phoneticSpelling"]))
#audio pronunciation:
    



def playp():
    printout.set(keyword.get())
    app_id = '0a4aedf4'
    app_key = 'b4379c0d5e1270781bf4450799782a09'
    language = 'en'
    word_id =keyword.get()
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    dic=r.json()
    #print("text \n" + r.text)
    #a=urllib.urlretrieve()
    a=urllib.request.urlretrieve(dic['results'][0]['lexicalEntries'][0]['pronunciations'][0]['audioFile'])
    #print(a)
    pygame.mixer.music.load(str(a[0]))
    #pygame.mixer.music.load(r'C:\Users\anthonyliu\Downloads\huge_gb_1.mp3')
    pygame.mixer.music.play()
        
    



#announce:


    
#main funciton
root=tkinter.Tk()
root.title("Shuangjie's Dictionary")
root.configure(bg="white")
root.lift()
root.minsize(600, 600)
#pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
pygame.init()

WelcomeWords=tkinter.Label(root,text="Welcome guys!",bg="light blue")
WelcomeWords.grid(row=0,column=0,columnspan=3,sticky="nsew")

Enterword=tkinter.Label(root,text="Enter Word:>>>",bg="white")
Enterword.grid(row=1,column=0,sticky="nsew")
############
playpath=""
keyword=tkinter.StringVar()
phonetic=tkinter.StringVar()
etymologies=tkinter.StringVar()
definitions=tkinter.StringVar()
antonyms=tkinter.StringVar()
synonyms=tkinter.StringVar()
sentence=tkinter.StringVar()
###########                                     
inbox=tkinter.Entry(root,textvariable=keyword,bg="pink",fg="dark green")
inbox.grid(row=1,column=1,sticky="nsew")

click=tkinter.Button(root,text="Search",command=SearchFunc)
click.grid(row=1,column=2,sticky="nsew")

play=tkinter.Button(root,text="Pronunciation",command=playp)
play.grid(row=2,column=2,sticky="nsew")

printout=tkinter.StringVar()
#printout.set(keyword.get())                                    
                 
outbox_keyword=tkinter.Message(root,textvariable=printout,fg="black")
outbox_keyword.grid(row=2,column=0,sticky="nsew")

outbox_definitions=tkinter.Message(root,textvariable=definitions,fg="black")
outbox_definitions.grid(row=3,column=0,sticky="nsew")

outbox_phonetic=tkinter.Message(root,textvariable=phonetic,fg="black")
outbox_phonetic.grid(row=4,column=0,sticky="nsew")

outbox_etymologies=tkinter.Message(root,textvariable=etymologies,fg="black")
outbox_etymologies.grid(row=5,column=0,sticky="nsew")

copyrignt=tkinter.Label(root,text="Copyright Hongchi",bg="light blue")
copyrignt.grid(row=6,column=0,columnspan=3,sticky="nsew")

outbox_antonyms=tkinter.Message(root,textvariable=antonyms,fg="black")
outbox_antonyms.grid(row=3,column=1,columnspan=2,sticky="nsew")

outbox_synonyms=tkinter.Message(root,textvariable=synonyms,fg="black")
outbox_synonyms.grid(row=4,column=1,columnspan=2,sticky="nsew")
                 
outbox_sentence=tkinter.Message(root,textvariable=sentence,fg="black")
outbox_sentence.grid(row=5,column=1,columnspan=2,sticky="nsew")


root.rowconfigure(4,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.rowconfigure(3,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.mainloop()
