import java.util.*;

public class burner{
	public static void main(String[] args){
		Scanner myObj = new Scanner(System.in);
		System.out.println("How many bands do you know?");
		
		ArrayList<String> theList = new ArrayList<String>(myObj.nextInt());
		myObj.nextLine();		// eat enter
		
		for (int i=0; i<theList.size(); i++){
			System.out.println("Name?");
			theList.add(myObj.nextLine());
		}

		for (String name: theList) {
			System.out.println(name);
		}
	}

}
