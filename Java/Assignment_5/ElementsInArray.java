import java.util.Scanner;
public class ElementsInArray { 
	public static void main(String[] args) {
		Scanner myObject = new Scanner(System.in);

		//ask for desired amount of elements
		System.out.println("How many elements in the list?: ");
		
		//saving the length of our list.
		int listLength = myObject.nextInt();

		//instantiating list 
		int[] intArray = new int[listLength];


		//consume enter
		myObject.nextLine();
	        System.out.println("The Array is of size: " + listLength);
		System.out.println("\r");

		for (int i=0; i<listLength; i++){
			System.out.println("Enter First int: ");
			intArray[i] = myObject.nextInt();		//setting element at index i.
			myObject.nextLine();				//eat the enter.
		}

		System.out.println("\r");

		for (int number : intArray){
			System.out.println(number);
		}


	}
}	
