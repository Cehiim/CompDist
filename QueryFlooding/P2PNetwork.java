import java.util.*;

// Classe que representa um nó na rede P2P
class Node {
    private String nodeName;
    private Set<String> files; // Arquivos que o nó possui
    private List<Node> neighbors; // Vizinhos do nó

    public Node(String nodeName) {
        this.nodeName = nodeName;
        this.files = new HashSet<>();
        this.neighbors = new ArrayList<>();
    }

    // Adiciona um arquivo ao nó
    public void addFile(String fileName) {
        files.add(fileName);
    }

    // Adiciona um vizinho à lista de vizinhos do nó
    public void addNeighbor(Node neighbor) {
        neighbors.add(neighbor);
    }

    // Inicia uma consulta para um arquivo
    public void queryFile(String fileName, Set<Node> visitedNodes) {
        if (visitedNodes.contains(this)) {
            return; // Evita voltar para o nó que já visitou
        }

        System.out.println(nodeName + " está procurando por '" + fileName + "'...");

        if (files.contains(fileName)) {
            System.out.println(nodeName + " encontrou o arquivo '" + fileName + "'!");
            return;
        }

        // Marca o nó como visitado
        visitedNodes.add(this);

        // Repete a consulta para todos os vizinhos
        for (Node neighbor : neighbors) {
            neighbor.queryFile(fileName, visitedNodes);
        }
    }

    // Método para iniciar a busca de um arquivo
    public void searchFile(String fileName) {
        Set<Node> visitedNodes = new HashSet<>();
        queryFile(fileName, visitedNodes);
    }

    // Retorna o nome do nó
    public String getNodeName() {
        return nodeName;
    }
}

public class P2PNetwork {
    public static void main(String[] args) {
        // Criação dos nós
        Node node1 = new Node("Nó 1");
        Node node2 = new Node("Nó 2");
        Node node3 = new Node("Nó 3");
        Node node4 = new Node("Nó 4");
        Node node5 = new Node("Nó 5");

        // Adiciona arquivos aos nós
        node1.addFile("arquivo1.txt");
        node3.addFile("arquivo2.txt");
        node5.addFile("arquivo3.txt");

        // Criação das conexões entre os nós (topologia da rede)
        node1.addNeighbor(node2);
        node2.addNeighbor(node1);
        node2.addNeighbor(node3);
        node3.addNeighbor(node2);
        node3.addNeighbor(node4);
        node4.addNeighbor(node3);
        node4.addNeighbor(node5);
        node5.addNeighbor(node4);

        // Executa uma busca por um arquivo em um nó específico
        System.out.println("Iniciando busca a partir do Nó 1:");
        node1.searchFile("arquivo3.txt");
    }
}
