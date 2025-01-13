from tkinter import ttk
from tkinter import *
from gtts import gTTS
from playsound import playsound
import os
from os import remove
import speech_recognition as sr

class inicio:
    def __init__(self,ventana):
        self.ven = ventana
        self.ven.iconbitmap('icon.ico')
        self.ven.geometry("1280x720+350+150")
        self.ven.resizable(False, False)
        self.ven.title("Texto a Audio")

        #Entry de texto a audio
        self.txt = Entry(self.ven, width=40, font=("Console", 30), background="#FF4D00")
        self.txt.place(x=200, y=50)
        self.lbl = Label(self.ven, text="No hay ningun archivo que borrar", font=("Console", 30))

        #Button de texto a audio
        self.btnreproducir = Button(self.ven, text="Reproducir", font=("Console", 30), background="#FF4D00", command=self.textoavoz)
        self.btnreproducir.place(x=855, y=250)
        self.btnborrar = Button(self.ven, text="Borrar", font=("Console", 30), background="#FF4D00", command=self.borrar)
        self.btnborrar.place(x=210, y=250)
        self.btnpegar = Button(self.ven, text="Salir", font=("Console", 30), background="#FF4D00", command=self.salir)
        self.btnpegar.place(x=225, y=400)
        self.btnsegunda = Button(self.ven, text="Voz a Texto", font=("Console", 30), background="#FF4D00", command=self.segunda)
        self.btnsegunda.place(x=855,y=400)
    
    def textoavoz(self):
        
        self.lbl.place_forget()
        gta = gTTS(self.txt.get(), lang="es-us")
        if os.path.isfile("text.mp3")==False:
            gta.save("text.mp3")
            playsound("text.mp3")
            remove("text.mp3")
    
    def borrar(self):
        
        if os.path.isfile("prueba.mp3"):
            
            remove("prueba.mp3")
        else:
            self.lbl.place(x=350, y=600)

    def salir(self):
        self.ven.destroy()
    
    #Segunda Ventana

    def segunda(self):
        self.ven2 = Frame(self.ven, width=1280, height=720)
        self.ven2.place(x=0, y=0)

        self.recognizer = sr.Recognizer()
        self.detener_grabacion = False
        self.resultado_texto = StringVar()

        #Entry de texto a audio
        self.txt2 = Label(ventana, textvariable=self.resultado_texto, wraplength=350, font=("Arial", 12))#Entry(self.ven2, width=40, font=("Console", 30), background="#FF4D00")
        self.txt2.place(x=200, y=50)

        #Button de voz a texto
        self.btngrabar = Button(self.ven2, text="Grabar", font=("Console", 30), background="#FF4D00", command=self.grabar)
        self.btngrabar.place(x=850, y=250)
        self.btnrepro = Button(self.ven2, text="Detener", font=("Console", 30), background="#FF4D00",command=self.detener)
        self.btnrepro.place(x=210, y=250)
        self.btncopiar = Button(self.ven2, text="Salir", font=("Console", 30), background="#FF4D00",command=self.salir)
        self.btncopiar.place(x=260, y=400)
        self.btnatras = Button(self.ven2,text="Atras", font=("Console", 30), background="#FF4D00", command=self.atras)
        self.btnatras.place(x=910, y=400)
    
    def grabar(self):
        
        self.detener_grabacion = False
        self.resultado_texto.set("Grabando... Por favor, hable.")
        
        try:
            with sr.Microphone() as source:
                # Ajustar el ruido ambiental
                self.recognizer.adjust_for_ambient_noise(source)
                while not self.detener_grabacion:
                    print("Escuchando...")
                    audio = self.recognizer.listen(source, timeout=2, phrase_time_limit=5)
                    print("Procesando el audio...")
                    
                    # Convertir audio a texto
                    texto = self.recognizer.recognize_google(audio, language="es-ES")
                    self.resultado_texto.set(f"Texto reconocido: {texto}")
                    break  # Salir después de la primera grabación válida
                
        except sr.UnknownValueError:
            self.resultado_texto.set("No se pudo entender el audio.")
        except sr.RequestError as e:
            self.resultado_texto.set(f"Error con el servicio: {e}")
        except Exception as e:
            self.resultado_texto.set(f"Error: {e}")

    def atras(self):
        self.ven2.place_forget()
    
    def detener(self):
        self.detener_grabacion = True
        self.resultado_texto.set("Grabación detenida.")
        



if __name__=='__main__':
    ventana = Tk()
    application = inicio(ventana)
    ventana.mainloop()
