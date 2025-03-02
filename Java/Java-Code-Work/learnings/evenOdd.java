import java.util.*;
public class evenOdd{
	public static void main(String[] args){
		Scanner myObj = new Scanner(System.in);

		for (int i=0; i<10; i++){
			System.out.println("Please enter number: ");
			int number = myObj.nextInt();
			myObj.nextLine();
			if ( number % 2 == 0){
				System.out.println("Even!");
			}
			else {
				System.out.println("Odd");
			}
		}
	}
}
			
