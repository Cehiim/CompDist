Explicação das classes e ações:
1. Classe Bloco: Representa um bloco individual na cadeia. Cada bloco contém o seu próprio hash, o hash do bloco anterior, dados (que poderiam ser transações) e um timestamp. A função calcularHash() garante que qualquer alteração nos dados ou no bloco afete o hash.
2. Classe Blockchain: É uma lista de blocos. A função ehBlockchainValida() verifica se a cadeia é válida, comparando os hashes dos blocos e assegurando que cada bloco foi minerado corretamente.
3. Estratégia de Mineração: O método minerarBloco() realiza uma "Prova de Trabalho" (PoW) simples, fazendo ajustes até que o hash do bloco comece com uma quantidade especificada de zeros.

Esse é um exemplo básico para ilustrar o funcionamento de uma blockchain. Em uma implementação real, você teria que lidar com muitos outros aspectos, como rede peer-to-peer, mecanismos de consenso mais complexos, validação de transações, entre outros

Tarefa: Altere o código de modo a que o bloco represente um diploma emitido por alguma universidade (contendo dados de aluno e curso, além da Universidade) e que seja transmitido (via Sockets ou gRPC/RMI), via blockchain, garantindo sua validade.
