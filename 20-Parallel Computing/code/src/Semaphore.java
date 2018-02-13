public class Semaphore {
    private final int MAX_AVAILABLE;
    private int taken;

    public Semaphore(int maxAvaible) {
        this.MAX_AVAILABLE = maxAvaible;
        this.taken = 0;
    }

    public synchronized void acquire() throws InterruptedException {
        while (this.taken == MAX_AVAILABLE) {
            wait();
        }
        this.taken++;
    }

    public synchronized void release() throws InterruptedException {
        this.taken--;
        this.notifyAll();
    }
}
