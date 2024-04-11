# Youtube-video-python-player
 Reproduzindo um vídeo do YouTube usando Python.

Explicação:
Importando o Módulo: import pywhatkit importa o módulo pywhatkit, que oferece diversas funcionalidades, incluindo a reprodução de vídeos do YouTube.



Tratamento de exceções (try-except): O código é encapsulado em um bloco try, que permite ao Python tentar o código dentro dele. Se ocorrer um erro durante a execução do código dentro do bloco try, o Python irá parar de executar esse bloco e pular para o bloco except.



Entrada do usuário: dentro do bloco try, a função input() solicita que o usuário insira o nome da música que deseja reproduzir no YouTube. O nome da música inserida é armazenado na variável song.



Reproduzindo vídeo do YouTube: A função pywhatkit.playonyt() é chamada com a variável song como argumento. Esta função abre um navegador da web e reproduz o vídeo do YouTube correspondente ao termo de pesquisa inserido pelo usuário.



Mensagem de sucesso: Se o vídeo for reproduzido com sucesso e sem erros, o código dentro do bloco try será executado completamente e a mensagem de sucesso "Reproduzido com sucesso!" será impresso.



Tratamento de exceções (exceto): Se ocorrer algum erro inesperado durante a execução do código dentro do bloco try, o Python irá pular para o bloco except e executar o código dentro dele. Neste caso, simplesmente imprime a mensagem de erro "An Unexpected Error!". Isso garante que o programa não trave abruptamente se ocorrer um erro durante a reprodução do vídeo.



No geral, esse código permite que os usuários insiram o nome de uma música e reproduzam o vídeo do YouTube correspondente enquanto lidam com quaisquer erros inesperados que possam ocorrer durante a execução.
