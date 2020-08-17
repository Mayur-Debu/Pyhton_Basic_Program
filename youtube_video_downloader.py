from tkinter import *
from tkinter.filedialog import askdirectory
from PIL import Image,  ImageTk
from pip._vendor.urllib3.util import url
import pytube
from threading import *
from tkinter.messagebox import askyesno

file_size=0         #Video size container

def downThread():
    """Thread for downloading youtube video"""
    thread = Thread(target=downloader)
    thread.start()

def progress(chunk, file_handle, remaining):
    """Monitoring the process of downloading"""
    global  download_status
    file_downloaded= file_size-remaining
    per=(file_downloaded/file_size)*100
    download_status.config(text='{:00.0f}% downloaded'.format(per))

def downloader():
    """Download the video"""
    global file_size,download_status
    download_button.config(state=DISABLED)
    download_status.place(x=320,y=250)
    try:
        url1=url.get()
        path=askdirectory()
        yt=pytube.YouTube(url1, on_progress_callback=progress)
        video=yt.streams.filter(progressive=True, file_extension='mp4').first()
        file_size=video.filesize
        video.download(path)
        download_status.config(text='Download Finish....')
        res=askyesno("Youtube video downloader", "Do you want to downoad another video?")
        if res==1:
            url.delete(0,END)
            download_button.config(state=NORMAL)
            download_status.config(text='')
        else:
            root.destroy()
    except Exception as e:
        download_status.config(text='FAILED!!! THEIR IS AN  ERROR')


root=Tk()
root.geometry('600*400')
root.iconbitmap('logo.ico')


root.title("YOUTUBE VIDEO DOWNLOADER")
root['bg']='white'
root.resizable(0,0)

img=Image.open('logo.ico')
img=img.resize((80,80), Image.ANTIALIAS)


img=ImageTK.photoImage(img)
head=Label(root,image=img)
head.config(anchor=CENTER)
head.pack()

enter_url= Label(root,text='Enter URL:', bg='white')
enter_url.config(font=('Verdana',15))
enter_url.place(x=5,y=120)
url= Entry(root,width=35,border=1,relief=SUNKEN,font=('verdana',15))
url.place(x=125,y=123)
download_button_img=Image.open('download_button.png')
download_button_img=download_button_img.resize((200,150),Image.ANTIALIAS)
download_button_img=ImageTk.PhotoImage(download_button_img)

download_button=Button(root,width=160,height=45,bg='white', relief=FLAT)
activebackground=('red', downThread())
download_button.config(image=download_button_img)
download_button.place(x=220,y=170)
download_status=Label(root,text="Please Wait.....",font=('Verdana',15),bg='white')
root.mainloop()



