class IncrementThread implements Runnable {

    @Override
    public void run() {
        for (int i = 0; i < TwoThreadIncrementDriver.N; i++) {
            TwoThreadIncrementDriver.counter++;
        }
    }
}

public class TwoThreadIncrementDriver {
    public static int counter;
    public static int N;

    public static void main(String[] args) throws InterruptedException {
        N = 10000;

        Thread t1 = new Thread(new IncrementThread());
        Thread t2 = new Thread(new IncrementThread());
        Thread t3 = new Thread(new IncrementThread());

        t1.start();
        t2.start();
        t3.start();
        t1.join();
        t2.join();
        t3.join();

        // the result may be less than 30000
        System.out.println(counter);

    }
}
