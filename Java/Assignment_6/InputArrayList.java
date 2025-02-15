import java.util.*;

public class InputArrayList{ public static void main(String[] args){ 

	//set up scanner
	Scanner myObject = new Scanner(System.in);
	System.out.println("How many Strings would you like to enter? ");
	int listLength = myObject.nextInt();
	//create arrayList 
	ArrayList<String> subjectsArrayList = new ArrayList<String>();


	//consuming the enter from above
	myObject.nextLine();

	for (int i=0; i<listLength; i++){
		System.out.println("Enter String: ");
		subjectsArrayList.add(myObject.nextLine());
	}

	//print line divider for cleanliness
	System.out.println("\r");

	//Sorting the list into reverse Alphabetical order
	Collections.sort(subjectsArrayList, Collections.reverseOrder());

	System.out.println("Your Classes are as follows: ");
	for (String str: subjectsArrayList){
		System.out.println(str);
	}
}
}
	//set up array list 
	//add to array list -> try nesting for .ad()
	//for loop over elements and print	
