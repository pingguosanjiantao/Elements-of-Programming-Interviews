/*
 * 20.3
 */
public class OddEvenMonitor {
    public static final boolean ODD_TURN = true;
    public static final boolean EVEN_TRUN = false;
    private boolean turn = ODD_TURN;

    public synchronized void waitTurn(boolean oldTurn) {
        while (turn != oldTurn) {
            try {
                wait();
            } catch (InterruptedException e) {
                System.out.println("InterruptedException in wait():" + e);
            }
        }
    }

    public synchronized void toggleTurn() {
        turn ^= true;
        notify();
    }

    public static void main(String[] args) throws InterruptedException {
        OddEvenMonitor monitor = new OddEvenMonitor();
        Thread t1 = new OddThread(monitor);
        Thread t2 = new EvenThread(monitor);
        t1.start();
        t2.start();
        t1.join();
        t2.join();
    }

}

class OddThread extends Thread {
    private final OddEvenMonitor monitor;

    public OddThread(OddEvenMonitor monitor) {
        this.monitor = monitor;
    }

    public void run() {
        for (int i = 1; i <= 100; i += 2) {
            monitor.waitTurn(OddEvenMonitor.ODD_TURN);
            System.out.println("OddThread: i = " + i);
            monitor.toggleTurn();
        }
    }
}

class EvenThread extends Thread {
    private final OddEvenMonitor monitor;

    public EvenThread(OddEvenMonitor monitor) {
        this.monitor = monitor;
    }

    public void run() {
        for (int i = 2; i <= 100; i += 2) {
            monitor.waitTurn(OddEvenMonitor.EVEN_TRUN);
            System.out.println("EvenThread: i = " + i);
            monitor.toggleTurn();
        }
    }
}
