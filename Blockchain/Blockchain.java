import java.util.ArrayList;

public class Blockchain {
    public static ArrayList<Bloco> blockchain = new ArrayList<>();
    public static int dificuldade = 5;

    public static void main(String[] args) {
        // Adiciona o bloco gênesis
        blockchain.add(new Bloco("João Silva", "Engenharia de Software", "Universidade de São Paulo", "0"));
        System.out.println("Minerando bloco 1...");
        blockchain.get(0).minerarBloco(dificuldade);

        // Adiciona mais blocos à cadeia
        blockchain.add(new Bloco("Maria Oliveira", "Ciência da Computação", "Universidade Estadual de Campinas", blockchain.get(blockchain.size()-1).hash));
        System.out.println("Minerando bloco 2...");
        blockchain.get(1).minerarBloco(dificuldade);

        blockchain.add(new Bloco("Carlos Souza", "Engenharia Elétrica", "Universidade Federal de Minas Gerais", blockchain.get(blockchain.size()-1).hash));
        System.out.println("Minerando bloco 3...");
        blockchain.get(2).minerarBloco(dificuldade);

        System.out.println("\nA Blockchain é válida: " + ehBlockchainValida());
    }

    // Verifica se a blockchain é válida
    public static boolean ehBlockchainValida() {
        Bloco blocoAtual;
        Bloco blocoAnterior;
        String hashAlvo = new String(new char[dificuldade]).replace('\0', '0');

        for (int i = 1; i < blockchain.size(); i++) {
            blocoAtual = blockchain.get(i);
            blocoAnterior = blockchain.get(i-1);

            // Compara o hash registrado com o hash calculado
            if (!blocoAtual.hash.equals(blocoAtual.calcularHash())) {
                System.out.println("Hashes do bloco atual não são iguais.");
                return false;
            }

            // Compara o hash anterior registrado com o hash do bloco anterior
            if (!blocoAnterior.hash.equals(blocoAtual.hashAnterior)) {
                System.out.println("Hashes do bloco anterior não são iguais.");
                return false;
            }

            // Verifica se o bloco foi minerado
            if (!blocoAtual.hash.substring(0, dificuldade).equals(hashAlvo)) {
                System.out.println("Este bloco não foi minerado.");
                return false;
            }
        }
        return true;
    }
}
