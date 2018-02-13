/*
 * 20.5
 */
public class DeadLock {
    public static class Account {
        private int balance;
        private int id;
        private static int globalId;

        Account(int balance) {
            this.balance = balance;
            this.id = ++globalId;
        }

        // have a global ordering on locks and acquire them in that order
        private boolean move(Account to, int amount) {
            Account lock1 = id < to.id ? this : to;
            Account lock2 = id < to.id ? to : this;
            synchronized(lock1) {
                synchronized(lock2) {
                    if (amount > balance) {
                        return false;
                    }
                    to.balance += amount;
                    this.balance -= amount;
                    System.out.println("returning true");
                    return true;
                }
            }
        }
    }

    public static void transfer(final Account from, final Account to, final int amount) {
        Thread transfer = new Thread(new Runnable() {
            @Override
            public void run() {
                from.move(to, amount);
            }
        });
        transfer.start();

    }
}
