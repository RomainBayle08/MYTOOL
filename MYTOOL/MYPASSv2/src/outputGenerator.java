import java.util.Random;

public class outputGenerator {// strength 1-4 1 = juste chiffre , 2 = 1+ lettre minuscule , 3 = 2 + lettre majuscule , 5 = 3 + symboles

    private final Random random = new Random();



    private char outputStrength1(){
        return (char) randomBetweenTwoBounds(48 , 58);
    }
    private char outputStrength2(){

        if(test()){
            return outputStrength1();
        }
        else {
            return (char) randomBetweenTwoBounds(97 , 123);
        }

    }

    private  char outputStrength3(){
        if(test()){
            return outputStrength2();
        }
        else {
            return  (char) randomBetweenTwoBounds(65 , 91);
        }
    }

    private char outputStrength4(){
        if(test()){
            return outputStrength3();
        }
        else {
            return getRandomSymbol();
        }
    }



    public  char getRandomOutputByStrength(int strength) throws Exception {
        switch (strength){
            case 1:
                return outputStrength1();
            case 2:
                return outputStrength2();
            case 3:
                return outputStrength3();
            case 4 :
                return outputStrength4();
            default:
                throw new Exception("strength out of bounds");
        }
    }









    private boolean test(){
        return random.nextBoolean();
    }
    private int randomBetweenTwoBounds(int lowerBound , int upperBound){ // lowerbounds <= x < upperbounds
        return random.nextInt(upperBound-lowerBound)+lowerBound;
    }

    private char getRandomSymbol (){ //comment les symbole de sont pas tous a la suite en ASCII
        boolean test = random.nextBoolean();
        if(test){
            return (char) randomBetweenTwoBounds(33 , 48);}
        else {
            return (char) randomBetweenTwoBounds(91, 97);
        }
    }
}
