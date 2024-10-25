import java.io.*;
import java.net.Socket;
import java.util.Scanner;

public class Receiver {
    private static final String[] HOSTS = {"172.16.18.103", "172.24.128.1"};
    private static final int PORT = 5001;
    private static final int BUFFER_SIZE = 4096;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);/*
        end = false;
        while(!end){
            String option = scanner.nextLine();
            if(option == "0"){
                
            }
        }*/
        System.out.print("Digite o nome do arquivo a ser recebido: ");
        String fileName = scanner.nextLine();

        for (String HOST : HOSTS) {
            try (Socket socket = new Socket(HOST, PORT)) {
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
                    System.out.println("Endereço " + HOST + " conectado com sucesso: Arquivo recebido.");
                } else {
                    System.out.println("Arquivo não encontrado.");
                }

                dos.close();
                dis.close();
            } 
            catch (IOException e) {
                System.out.println("Erro ao conectar-se ao endereço " + HOST + ": " + e.getMessage());
            } 
            finally {
                scanner.close();
            }
        }
    }
}
