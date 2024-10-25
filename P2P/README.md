Observe os dois códigos Java a seguir. Receiver solicitará o nome do arquivo ao usuário e o enviará para a Sender. Se o arquivo existir, a Sender enviará o conteúdo do arquivo de volta. Caso contrário, ela retornará uma mensagem informando que o arquivo não foi encontrado.

# Classe Sender
Esta classe verifica se o arquivo existe e, se sim, envia seu conteúdo. Caso contrário, ela envia uma mensagem indicando que o arquivo não foi encontrado.


# Classe Receiver
A Receiver solicita o nome do arquivo ao usuário e o envia para o Sender. Se o Sender retornar uma mensagem de que o arquivo foi encontrado, a Receiver salva o arquivo com o prefixo "recebido". Caso contrário, ela exibe uma mensagem indicando que o arquivo não foi encontrado.


# Explicação do Funcionamento
## Sender

Aguarda uma conexão do Receiver.
Recebe o nome do arquivo solicitado.
Verifica se o arquivo existe na pasta onde está sendo executado.
Se o arquivo existir, envia uma mensagem "FOUND" e o conteúdo do arquivo em chunks.
Caso contrário, envia "NOT_FOUND".
## Receiver

Solicita ao usuário o nome do arquivo.
Envia o nome do arquivo para o Sender.
Se o Sender retornar "FOUND", o Receiver salva o arquivo com o prefixo "recebido_".
Se o Sender retornar "NOT_FOUND", o Receiver exibe "Arquivo não encontrado".
# Instruções
Primeiro, execute a classe Sender para que ela fique aguardando a conexão.
Em seguida, execute a classe Receiver e insira o nome do arquivo desejado.
O Sender responderá conforme o arquivo exista ou não no diretório.
# Tarefa (em trio)

Altere o código para rodar em três máquinas, cada uma delas tendo uma versão de Sender e Receiver . A busca pode ser feita por qualquer máquina e deve ocorrer nas outras duas máquinas.
