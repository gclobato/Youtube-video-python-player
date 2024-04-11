import pywhatkit

    # Usando tratamento de exceções para evitar erros sem precedentes

try:

    # Peça ao usuário para inserir o nome da música

    song = input("Enter Song Name: ")

   # Reproduza um vídeo do YouTube correspondente ao termo de pesquisa inserido pelo usuário
    pywhatkit.playonyt(song)    

    # Imprima uma mensagem de sucesso se o vídeo for reproduzido com sucesso

    print("Successfully Played!") 

except:

    # Trata exceções e imprime uma mensagem de erro se ocorrer algum erro inesperado
    print("An Unexpected Error!")