import java.util.Scanner;

public class PasswordBuilder {
    PasswordGenerator pwGen = new PasswordGenerator();

    Scanner read = new Scanner(System.in);

    PasswordBuilder() throws Exception {
        passwordType();
    }

    private void passwordType() throws Exception {
        System.out.println("choose your password type (1/2)");
        System.out.println("1 - random strong password");
        System.out.println("2 - build your own password");
        int input = read.nextInt();
        switch (input){
            case 1 :
                randomPasswordBuilder();
                break;
            case 2 :
                yourPasswordBuilder();
                break;
            default:
                throw new Exception("incorrect option");
        }
    }

    private void yourPasswordBuilder() throws Exception {
        System.out.println("choose your Password's strength (1-4)");
        System.out.println("strength rank :");
        System.out.println("1 : number , 2 : 1 + lower case letter , 3 : 2 + upper case letter , 4 : 3 + symbols");
        int strength = read.nextInt();
        System.out.println("now , choose your password length");
        int length = read.nextInt();
        System.out.println("your password is : "+ pwGen.yourPassword(strength,length));
    }

    private void randomPasswordBuilder() throws Exception {
        System.out.println("your random strong password is : "+pwGen.randomPassword());
    }

    public static void main(String[] args) throws Exception {

        PasswordBuilder test ;
        test = new PasswordBuilder();
        

    }




}
