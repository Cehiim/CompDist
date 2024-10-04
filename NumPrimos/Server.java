// NOME: Pedro Henrique Araujo Farias
// RA: 10265432

import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class Server implements Calc {
    public boolean saoPrimosGemeos(int n1, int n2) throws RemoteException {
        Numero a = new Numero(n1);
        Numero b = new Numero(n2);
        return a.saoPrimosGemeos(b);
    }

    public static void main(String[] args) {
        try {
            System.out.println("Obs.: Aguarde alguns segundos para conexao...\n");

            Server server = new Server();
            Calc stub = (Calc) UnicastRemoteObject.exportObject(server, 0);
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.bind("Calc", stub);
            System.out.println("Calc ouvindo na porta 1099...");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}