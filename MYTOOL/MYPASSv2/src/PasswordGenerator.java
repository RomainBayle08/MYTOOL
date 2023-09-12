public class PasswordGenerator {
    outputGenerator outputGen = new outputGenerator();



    public String yourPassword(int strength , int length) throws Exception {   String output = "";
        for(int n = 0;n<length;n++){
            output += outputGen.getRandomOutputByStrength(strength);
        }
        return output;
    }

    public String randomPassword() throws Exception {
        int length = 17;
        int strength = 3;
        String output = "";
        for(int n = 0;n<length;n++){
            if(n == 5 || n ==11){
               output +='-';
            }
            else{
                output += outputGen.getRandomOutputByStrength(strength);
            }
        }
        return output;
    }
































}
