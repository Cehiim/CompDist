// NOME: Pedro Henrique Araujo Farias
// RA: 10265432

import java.rmi.Remote;
import java.rmi.RemoteException;

// Interface com numerosos metodos
public interface Calc extends Remote {
    public boolean saoPrimosGemeos(int n1, int n2) throws RemoteException;
}
