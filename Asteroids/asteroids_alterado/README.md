Os princípios SOLID são um conjunto de cinco diretrizes para a programação orientada a objetos, que ajudam a criar software mais robusto, fácil de manter e expandir. Aqui estão os cinco princípios:

1. Single Responsibility Principle (SRP): Uma classe deve ter apenas uma responsabilidade ou motivo para mudar. Isso significa que cada classe deve ter uma única função ou responsabilidade.
2. Open/Closed Principle (OCP): As entidades de software (classes, módulos, funções, etc.) devem estar abertas para extensão, mas fechadas para modificação. Ou seja, você deve ser capaz de adicionar novas funcionalidades sem alterar o código existente.
3. Liskov Substitution Principle (LSP): Os objetos de uma classe derivada devem poder substituir objetos da classe base sem alterar o comportamento desejado do programa. Isso garante que a herança seja usada corretamente.
4. Interface Segregation Principle (ISP): Muitas interfaces específicas são melhores do que uma interface geral. Isso significa que os clientes não devem ser forçados a depender de interfaces que não utilizam.
5. Dependency Inversion Principle (DIP): Os módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações. Além disso, as abstrações não devem depender de detalhes. Os detalhes devem depender de abstrações.

O código original não segue os princípios SOLID. Porque a responsabilidade do sistema não foi dividida entre classes e portanto não há como adicionar novas funcionalidades sem alterar o código existente, ou seja, os princípios 1 e 2 foram violados.

Após a alteração, o sistema foi dividido entre classes de forma que cada classe represente uma responsabilidade específica do sistema e que cada método represente um único comportamento de uma classe.