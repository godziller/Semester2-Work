import java.util.ArrayList;
import java.util.Collections;
public class CompSciArrayList { public static void main( String[] args) {
	ArrayList<String> subjects = new ArrayList<String>();
	subjects.add("Cryptography");
	subjects.add("Databases");
	subjects.add("OS");
	subjects.add("Networking");
	System.out.println("Initial List: " + subjects);

	subjects.remove("Networking");		// removing networking
	
	Collections.sort(subjects, Collections.reverseOrder());		//Sorting our list in reverse alphabetical
	System.out.println(subjects);

	}
}
