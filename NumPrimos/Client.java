// NOME: Pedro Henrique Araujo Farias
// RA: 10265432

import java.util.Scanner;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {
    public static void main(String[] args) {
        try {
            Scanner scan = new Scanner(System.in);

            System.out.println("NUMEROS PRIMOS GEMEOS");
            System.out.println("Obs.: Aguarde alguns segundos para conexao...\n");

            Registry registry = LocateRegistry.getRegistry("localhost");
            Calc stub = (Calc) registry.lookup("Calc");

            System.out.print("Insira o primeiro numero: ");
            int numero1 = scan.nextInt();
            
            System.out.print("Insira o segundo numero: ");
            int numero2 = scan.nextInt();

            System.out.print(numero1 + " e " + numero2 + " sao primos gemeos? ");

            // Chamando metodo remoto para verificar se os numeros sao primos gemeos
            if(stub.saoPrimosGemeos(numero1, numero2)) {
                System.out.println("SIM!");
            } else {
                System.out.println("NAO!");
            }

            scan.close();
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}