import java.util.Date;
import java.security.MessageDigest;

public class Bloco {
    public String hash;
    public String hashAnterior; 
    //private String dados; // Transações, por exemplo.
    private String aluno;
    private String curso;
    private String universidade;
    private long timestamp;
    private int nonce; // Utilizado no processo de mineração.

    // Construtor do Bloco
    public Bloco(String aluno, String curso, String universidade, String hashAnterior) {
        //this.dados = dados;
        this.aluno = aluno;
        this.curso = curso;
        this.universidade = universidade; 
        this.hashAnterior = hashAnterior;
        this.timestamp = new Date().getTime();
        this.hash = calcularHash(); // Calcula o hash ao criar o bloco
    }

    // Calcula o hash do bloco
    public String calcularHash() {
        String conteudoParaHash = hashAnterior + Long.toString(timestamp) + Integer.toString(nonce) + aluno + curso + universidade;
        return aplicarSHA256(conteudoParaHash);
    }

    // Aplica a função SHA-256 para criar um hash
    public static String aplicarSHA256(String input) {
        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] hashBytes = digest.digest(input.getBytes("UTF-8"));
            StringBuilder hexString = new StringBuilder(); 
            for (byte b : hashBytes) {
                String hex = Integer.toHexString(0xff & b);
                if(hex.length() == 1) hexString.append('0');
                hexString.append(hex);
            }
            return hexString.toString();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    // Processo de mineração (Prova de Trabalho)
    public void minerarBloco(int dificuldade) {
        String alvo = new String(new char[dificuldade]).replace('\0', '0');
        while (!hash.substring(0, dificuldade).equals(alvo)) {
            nonce++;
            hash = calcularHash();
        }
        System.out.println("Bloco minerado com sucesso: " + hash);
    }
}
