#!/usr/bin/python3
import chunk
from pytube import YouTube
import tkinter as tk


def restart():
    button.configure(text="Téléchargement terminé !")
    root.update()
    text_fill.delete("1.0", "end-1c")

    labelAsk = tk.Label(root, text="Voulez-vous télécharger une autre vidéo ? Si oui, entrez le lien dans le champ de texte.")
    labelAsk.pack()

    buttonYes = tk.Button(root, text="Oui", command=download_url)
    buttonYes.pack()
    
    buttonNo = tk.Button(root, text="Non", command=exit)
    buttonNo.pack()

    root.update()    


def progress_function(my_video, chunk, bytes_remaining):
    text = round((1-bytes_remaining/my_video.filesize)*100, 3)
    textProgress = str(text) + ' % done...'
    labelProgress.configure(text=textProgress)
    labelProgress.pack()
    root.update()


def download_url():
    try:
        inputValue = text_fill.get("1.0","end-1c")
        my_video = YouTube(inputValue, on_progress_callback=progress_function)
        my_video = my_video.streams.get_highest_resolution()

        labelSize = tk.Label(root, text='FileSize : ' + str(round(my_video.filesize/(1024*1024))) + 'MB', justify=tk.CENTER, relief=tk.RAISED)
        labelSize.pack()
        root.update()

        my_video.download("/home/eflay/Vidéos")

        my_video.on_complete = restart()
    except Exception as e:
        print(e)


def change_button():
    button.configure(text="En téléchargement...", background="green", state="disabled")
    root.update()
    download_url()


root = tk.Tk()
root.geometry("500x250")

label = tk.Label(root, text="Entrez l'URL à télécharger : ", justify=tk.CENTER, relief=tk.RAISED)
label.pack()

text_fill= tk.Text(root, height=2, width=35)
text_fill.pack()

button = tk.Button(root, text="Télécharger", command=change_button)
button.pack()

labelProgress = tk.Label(root)

root.mainloop()
