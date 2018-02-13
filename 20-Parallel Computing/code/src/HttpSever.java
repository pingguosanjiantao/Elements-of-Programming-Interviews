import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;

/*
 * 20.4
 */
public class HttpSever {
    public static class SingleThreadWebServer {
        public static final int PORT = 8080;

        public static void main(String[] args) throws IOException {
            ServerSocket serverSocket = new ServerSocket(PORT);
            while (true) {
                Socket socker = serverSocket.accept();
                // process socket
            }
        }
    }

    public static class ConcurrentWebServer {
        public static final int PORT = 8080;

        public static void main(String[] args) throws IOException {
            ServerSocket serverSocket = new ServerSocket(PORT);
            while (true) {
                final Socket connection = serverSocket.accept();
                Runnable task = new Runnable() {
                    @Override
                    public void run() {
                        // process socket
                    }
                };
                new Thread(task).start();
            }
        }
    }

    public static class ThreadPoolWebServer {
        public static final int PORT = 8080;
        public static final int NTHREADS = 100;
        private static final Executor exec = Executors.newFixedThreadPool(NTHREADS);

        public static void main(String[] args) throws IOException {
            ServerSocket serverSocket = new ServerSocket(PORT);
            while (true) {
                final Socket connection = serverSocket.accept();
                Runnable task = new Runnable() {
                    @Override
                    public void run() {
                        // process socket
                    }
                };
                exec.execute(task);
            }
        }
    }

}
