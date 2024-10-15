// Color Sandwich
// Sam is a cook and he has colored breads and stuffing with which he had made some sandwiches. A sandwich can be made by keeping multiple or no stuffing between two same-colored breads like,
// gabcq (where abc represents stuffing and q represents coloured bread). The sandwiches are placed one over the other represented by a string 5 where each character depicts either bread or 
// the stuffing. Your task is to find and retur a string value representing the colour of the breads used in all sandwiches.
// Input Specification:
// inputl: A string 5 representing the sandwiches,
// Output Specification:
// Retum a string value representing the colour of the breads used in all sandwiches
// Example 1: input1: qezcquu
// Output : qu

import java.util.*;

public class ColorSandwich {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        sc.close();
        System.out.println(findColoredBreads(s));
    }

    public static String findColoredBreads(String str) {
        int count=1;
        HashSet<Character> set= new HashSet<>();
        

        for (int i = 0; i < str.length(); i++) {
          
           
                for (int j = i+1; j < str.length(); j++) {
                    if(str.charAt(i)==str.charAt(j))
                    count++;
                }
                if(count==2){
                    set.add(str.charAt(i));
                    count=1;

                }
               
            
           
            }  
            StringBuilder sb = new StringBuilder();
        for (Character ch : set) {
            sb.append(ch);
        }

        return sb.toString();       
            
        }
       
       
    

    }

    

