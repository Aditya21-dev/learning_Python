// Interface 1
interface Refundable {
    void refund();
}

// Interface 2
interface Verifiable {
    void verify();
}

// Abstract Class
abstract class Payment {
    protected double amount;

    Payment(double amount) {
        this.amount = amount;
    }

    abstract void pay();

    void receipt() {
        System.out.println("Receipt generated for amount: " + amount);
    }
}

// Child Class 1
class UPIPayment extends Payment implements Refundable, Verifiable {

    UPIPayment(double amount) {
        super(amount);
    }

    @Override
    public void verify() {
        System.out.println("UPI payment verified");
    }

    @Override
    void pay() {
        System.out.println("Paid " + amount + " via UPI");
    }

    @Override
    public void refund() {
        System.out.println("UPI refund successful");
    }
}

// Child Class 2
class CardPayment extends Payment implements Verifiable {

    CardPayment(double amount) {
        super(amount);
    }

    @Override
    public void verify() {
        System.out.println("Card payment verified");
    }

    @Override
    void pay() {
        System.out.println("Paid " + amount + " via Card");
    }
}

// Main Class
public class Main {
    public static void main(String[] args) {

        Payment p1 = new UPIPayment(500);
        Payment p2 = new CardPayment(1000);

        p1.pay();
        p1.receipt();

        p2.pay();
        p2.receipt();

        // Runtime Polymorphism + Interface check
        if (p1 instanceof Refundable) {
            ((Refundable) p1).refund();
        }
    }
}
