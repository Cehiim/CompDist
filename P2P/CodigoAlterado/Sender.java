import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class Sender {
    private static final int PORT = 5001;
    private static final int BUFFER_SIZE = 4096;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean end = false;

        try (ServerSocket serverSocket = new ServerSocket(PORT)) {

            while (!end) {
                System.out.println("\n\n0) Enviar um arquivo\n1) Encerrar programa");
                String option = scanner.nextLine();

                if (option.equals("0")) {
                    System.out.println("Sender aguardando a conexão...");

                    try (Socket socket = serverSocket.accept();
                         DataInputStream dis = new DataInputStream(socket.getInputStream());
                         DataOutputStream dos = new DataOutputStream(socket.getOutputStream())) {

                        // Recebe o nome do arquivo solicitado
                        String fileName = dis.readUTF();
                        System.out.println("Arquivo solicitado: " + fileName);

                        File file = new File(fileName);
                        if (file.exists() && !file.isDirectory()) {
                            dos.writeUTF("FOUND");
                            dos.flush();

                            // Envia o conteúdo do arquivo
                            try (FileInputStream fis = new FileInputStream(file)) {
                                byte[] buffer = new byte[BUFFER_SIZE];
                                int bytesRead;
                                while ((bytesRead = fis.read(buffer)) != -1) {
                                    dos.write(buffer, 0, bytesRead);
                                }
                            }
                            System.out.println("Arquivo enviado.");
                        } else {
                            dos.writeUTF("NOT_FOUND");
                            System.out.println("Arquivo não encontrado.");
                        }
                    } catch (IOException e) {
                        System.err.println("Erro ao enviar o arquivo: " + e.getMessage());
                    }
                } else if (option.equals("1")) {
                    end = true;
                    System.out.println("Programa encerrado.");
                } else {
                    System.out.println("Opção inválida.");
                }
            }
        } catch (IOException e) {
            System.err.println("Erro ao iniciar o servidor: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}
