import java.util.Date;

/*
 * 20.6
 */
public class RW {
    private static Object LR;
    private static Object LW;
    private static int readCounter = 0;
    private static String data;

    public static class Reader extends Thread {
        public void run() {
            while (true) {
                synchronized(RW.LR) {
                    RW.readCounter++;
                }
                System.out.println(RW.data);
                synchronized(RW.LR) {
                    RW.readCounter--;
                    RW.LR.notify();
                }
                // to do something
            }
        }
    }

    public static class Writer extends Thread {
        public void run() {
            while (true) {
                synchronized(RW.LW) {
                    boolean done = false;
                    while (!done) {
                        synchronized(RW.LR) {
                            if (RW.readCounter == 0) {
                                RW.data = new Date().toString();
                                done = true;
                            } else {
                                try {
                                    while (RW.readCounter != 0) {
                                        RW.LR.wait();
                                    }
                                } catch (InterruptedException e) {
                                    System.out.println("InterruptedException in Writer wait");
                                }
                            }
                        }
                    }
                }
                // to do something
            }
        }
    }
}
