import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class Sender {
    private static final int PORT = 5001;
    private static final int BUFFER_SIZE = 4096;

    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Sender aguardando a conexão...");

            Socket socket = serverSocket.accept();
            DataInputStream dis = new DataInputStream(socket.getInputStream());
            DataOutputStream dos = new DataOutputStream(socket.getOutputStream());

            // Recebe o nome do arquivo solicitado
            String fileName = dis.readUTF();
            System.out.println("Arquivo solicitado: " + fileName);

            File file = new File(fileName);
            if (file.exists() && !file.isDirectory()) {
                dos.writeUTF("FOUND");
                dos.flush();
                
                // Envia o conteúdo do arquivo
                FileInputStream fis = new FileInputStream(file);
                byte[] buffer = new byte[BUFFER_SIZE];
                int bytesRead;
                while ((bytesRead = fis.read(buffer)) != -1) {
                    dos.write(buffer, 0, bytesRead);
                }
                fis.close();
                System.out.println("Arquivo enviado.");
            } else {
                dos.writeUTF("NOT_FOUND");
                System.out.println("Arquivo não encontrado.");
            }

            dos.close();
            dis.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
