import java.util.Scanner;

public class LoadBalancing {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter no of servers: ");
        int numServers = sc.nextInt();
        System.out.print("Enter no of processes: ");
        int numProcesses = sc.nextInt();

        while (true) {
            printServerLoad(numServers, numProcesses);
            displayMenu();
            System.out.print("> ");
            int choice = sc.nextInt();
            int temp;

            switch (choice) {
                case 1:
                    System.out.println("Enter number of servers to be added: ");
                    temp = sc.nextInt();
                    numServers += temp;
                    break;
                case 2:
                    System.out.println("Enter number of servers to be removed: ");
                    temp = sc.nextInt();
                    numServers -= temp;
                    break;
                case 3:
                    System.out.println("Enter number of processes to be added: ");
                    temp = sc.nextInt();
                    numProcesses += temp;
                    break;
                case 4:
                    System.out.println("Enter number of processes to be removed: ");
                    temp = sc.nextInt();
                    numProcesses -= temp;
                    break;
                case 5:
                    sc.close();
                    return;
                default:
                    break;
            }
        }
    }

    static void printServerLoad(int numServers, int numProcesses) {
        int processesPerServer = numProcesses / numServers;
        int extraProcesses = numProcesses % numServers;

        int i = 0;

        // loop for extra process i.e adding 1 to each server
        for (i = 0; i < extraProcesses; i++)
            System.out.println("Server " + (i + 1) + " has " + (processesPerServer + 1) + " processes");

        // loop for remaining processes
        for (; i < numServers; i++)
            System.out.println("Server " + (i + 1) + " has " + processesPerServer + " processes");
    }

    static void displayMenu() {
        System.out.println("1. Add Server");
        System.out.println("2. Remove Server");
        System.out.println("3. Add Processes");
        System.out.println("4. Remove Processes");
        System.out.println("5. Exit");
    }
}