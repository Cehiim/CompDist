import java.io.*;
import java.net.Socket;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Receiver {
    private static final String[] HOSTS = {"192.168.0.8","172.16.18.103", "172.24.128.1"};
    private static final int NUM_HOSTS = 3;
    private static final int PORT = 5001;
    private static final int BUFFER_SIZE = 4096;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean end = false;
        while(!end){
            System.out.println("\n\n0) Requisitar um arquivo\n1) Encerrar programa");

            String option = scanner.nextLine();
            if(option.equals("0")){
                System.out.println("Endereços disponíveis");
                for(int i=0; i<NUM_HOSTS; i++){
                    System.out.printf("%d) %s %n", i, HOSTS[i]);
                }

                System.out.print("Escolha o índice de um endereço: ");
                try{
                    int indice = scanner.nextInt();
                    scanner.nextLine();
                    String endereco = HOSTS[indice];

                    System.out.print("Digite o nome do arquivo a ser recebido: ");
                    String fileName = scanner.nextLine();
    
                    try (Socket socket = new Socket(endereco, PORT)) {
                        DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
                        DataInputStream dis = new DataInputStream(socket.getInputStream());
    
                        // Envia o nome do arquivo solicitado
                        dos.writeUTF(fileName);
    
                        // Recebe a resposta do Sender
                        String response = dis.readUTF();
                        if ("FOUND".equals(response)) {
                            // Cria o arquivo para salvar o conteúdo recebido
                            String prefixedFileName = "recebido_" + fileName;
                            FileOutputStream fos = new FileOutputStream(prefixedFileName);
    
                            // Recebe o conteúdo do arquivo
                            byte[] buffer = new byte[BUFFER_SIZE];
                            int bytesRead;
                            while ((bytesRead = dis.read(buffer)) != -1) {
                                fos.write(buffer, 0, bytesRead);
                            }
                            
                            fos.close();
                            System.out.println("Endereço " + endereco + " conectado com sucesso: Arquivo recebido.");
                        } else {
                            System.out.println("Arquivo não encontrado.");
                        }
    
                        dos.close();
                        dis.close();
                    } 
                    catch (IOException e) {
                        System.out.println("Erro ao conectar-se ao endereço " + endereco + ": " + e.getMessage());
                    }
                }
                catch (InputMismatchException e) {
                    System.out.println("Erro: Você deve digitar um número inteiro.");
                }
            }
            else if(option.equals("1")){
                end = true;
            }
            else{
                System.out.println("Opção inválida");
            }
        }
        scanner.close();
    }
}
