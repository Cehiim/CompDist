// NOME: Pedro Henrique Araujo Farias
// RA: 10265432

public class Numero implements java.io.Serializable {
    private static final long serialVersionUID = 1L;
    private int num;

    public Numero(int num) {
        this.num = num;
    }

    public boolean ePrimo() {
        if (this.num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(this.num); i++) {
            if (this.num % i == 0) {
                return false;
            }
        }

        return true;
    }

    public boolean saoPrimosGemeos(Numero other) {
        if(this.ePrimo() && other.ePrimo()) {
            if(this.num - other.num == 2 || // Aceita tanto 5 - 3 = 2 quanto 3 - 5 = -2
            this.num - other.num == -2) return true;
        }

        return false;
    }

    public int getNum() {
        return this.num;
    }
}
