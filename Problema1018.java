/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package problema1018;
import java.util.Scanner;
/**
 *
 * @author User
 */
public class Problema1018 {

    /**
     * @param args the command line argumentss
     */
    public static void main(String[] args) {
        int a,b,t;
        Scanner sc=new Scanner(System.in);
        t=sc.nextInt();
        for(int i=1;i<=t;i++)
        {
            a=sc.nextInt();
            b=sc.nextInt();
            if(a<b)
            {
                System.out.println("<");
            }
            if(a>b)
            {
                System.out.println(">");
            }
            if(a==b)
            {
                System.out.println("=");
            }
        }
        
    }
    
}
