import tkinter as tk # Importa o módulo tkinter e o atribui à variável tk
from tkinter import filedialog, messagebox # Importa os submódulos filedialog e messagebox do tkinter
import subprocess # Importa o módulo subprocess para executar comandos externos
import os # Importa o módulo os para realizar operações relacionadas ao sistema operacional


def selecionar_arquivo():
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos Python", "*.py")]) # Exibe um diálogo de seleção de arquivo para arquivos Python (.py)
    if file_path: # Verifica se um arquivo foi selecionado
        arquivo_selecionado.set(file_path) # Define o caminho do arquivo selecionado na variável arquivo_selecionado


def selecionar_local_salvamento():
    salvar_localição = filedialog.askdirectory()  # Exibe uma caixa de diálogo para selecionar um diretório e armazena o caminho selecionado na variável 'salvar_localição'
    if salvar_localição:
        local_salvamento_selecionado.set(salvar_localição)# Atualiza o valor da variável 'local_salvamento_selecionado' com o caminho do diretório selecionado


def converter_para_executavel():
    file_path = arquivo_selecionado.get() # Obtém o caminho do arquivo selecionado
    salvar_localição = local_salvamento_selecionado.get()  # Obtém o local de salvamento selecionado
    if file_path and salvar_localição:   # Verifica se tanto o caminho do arquivo quanto o local de salvamento estão definidos
        file_name = os.path.basename(file_path) # Obtém o nome do arquivo a partir do caminho completo
        file_name_sem_ext = os.path.splitext(file_name)[0]    # Remove a extensão do nome do arquivo
        executable_path = os.path.join(salvar_localição, file_name_sem_ext + ".exe")   # Concatena o local de salvamento com o nome do arquivo e a extensão ".exe" para obter o caminho do executável

        comando = f'pyinstaller --onefile --noconsole --distpath="{salvar_localição}" "{file_path}"'
        subprocess.call(comando, shell=True)


        if os.path.exists(executable_path):# Verifica se o executável foi gerado com sucesso
            messagebox.showinfo("Conversão Concluída", "O arquivo foi convertido em um executável!") # Exibe uma mensagem de informação se a conversão foi concluída com sucesso
        else:
            messagebox.showwarning("Erro de Conversão", "Ocorreu um erro ao converter o arquivo.") # Exibe uma mensagem de aviso se ocorreu um erro na conversão
    elif not file_path:  # Verifica se o caminho do arquivo não está definido
        messagebox.showwarning("Nenhum arquivo selecionado", "Por favor, selecione um arquivo Python.")  # Exibe uma mensagem de aviso se nenhum arquivo foi selecionado
    else:
        messagebox.showwarning("Nenhum local de salvamento selecionado", "Por favor, selecione um local de salvamento.") # Exibe uma mensagem de aviso se nenhum local de salvamento foi selecionado

# Criação da janela principal
janela = tk.Tk()  # Cria uma instância da classe Tk para representar a janela principal
janela.title("Py to Exe")  # Define o título da janela
janela.geometry("300x250")  # Configura a geometria da janela com largura 300 e altura 250 pixels

arquivo_selecionado = tk.StringVar() # Cria uma variável do tipo StringVar para armazenar o caminho do arquivo selecionado
local_salvamento_selecionado = tk.StringVar() # Cria uma variável do tipo StringVar para armazenar o local de salvamento selecionado

# Botão para selecionar arquivo
botão_selecionar_arquivo = tk.Button(janela, text="Selecionar Arquivo", command=selecionar_arquivo)  # Cria um botão com o texto "Selecionar Arquivo" e associa a função selecionar_arquivo() ao comando do botão
botão_selecionar_arquivo.pack(pady=10)  # Empacota o botão na janela e define um espaçamento vertical de 10 pixels

# Rótulo para exibir o arquivo selecionado
arquivo_label = tk.Label(janela, textvariable=arquivo_selecionado)  # Cria um rótulo para exibir o caminho do arquivo selecionado e associa à variável arquivo_selecionado
arquivo_label.pack()  # Empacota o rótulo na janela

# Botão para selecionar local de salvamento
botão_selecionar_local_salvamento = tk.Button(janela, text="Selecionar Local de Salvamento", command=selecionar_local_salvamento)  # Cria um botão com o texto "Selecionar Local de Salvamento" e associa a função selecionar_local_salvamento() ao comando do botão
botão_selecionar_local_salvamento.pack(pady=10) # Empacota o botão na janela e define um espaçamento vertical de 10 pixels

# Rótulo para exibir o local de salvamento selecionado
rótulo_local_salvamento = tk.Label(janela, textvariable=local_salvamento_selecionado) # Cria um rótulo para exibir o local de salvamento selecionado e associa à variável local_salvamento_selecionado
rótulo_local_salvamento.pack() # Empacota o rótulo na janela

# Botão para converter o arquivo selecionado
botão_converter = tk.Button(janela, text="Converter", command=converter_para_executavel) # Cria um botão com o texto "Converter" e associa a função converter_para_executavel() ao comando do botão
botão_converter.pack(pady=10)  # Empacota o botão na janela e define um espaçamento vertical de 10 pixels

# Inicia o loop de eventos da janela
janela.mainloop() # Inicia o loop principal da interface gráfica