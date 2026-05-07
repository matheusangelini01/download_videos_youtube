import customtkinter as ctk
from pytubefix import YouTube

# configurações visuais 

# função baixar vídeo
def baixar():
    link_youtube = link.get()
    yt = YouTube (link_youtube)
    # Baixar resolução padrão
    yt.streams.first().download()
    status.configure(text='Download concluído')


# criação da janela
janela = ctk.CTk()
janela.geometry('600x400')
janela.title('Download de vídeos do Youtube')

# elementos da tela 
# label título
titulo = ctk.CTkLabel(janela, text='Download de vídeos do Youtube',
                      font=('Arial', 22),
                      text_color='#016FFC')
titulo.pack(pady=20)

# icone da janela 
janela.iconbitmap('ico_youtube.ico')

link = ctk.CTkEntry(janela, placeholder_text='Digite o link desejado')
link.pack(pady=20)

download = ctk.CTkButton(janela, text='Download', command=baixar)
download.pack(pady=20)

# status -> texto dizendo que o Download foi concluido!!
status = ctk.CTkLabel(janela, text='')
status.pack(pady=20)

# loop para a geração da janela 
janela.mainloop()