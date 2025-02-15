import java.util.Scanner;

public class UI{
	public static void main(String[] args){
		Scanner myObj = new Scanner(System.in); 		//creating a scanner object
		System.out.println("Enter Username");

		String userName = myObj.nextLine();		//reads the users inputs 
		System.out.println("Username is: " + userName);	// Output user input
		}
}	
