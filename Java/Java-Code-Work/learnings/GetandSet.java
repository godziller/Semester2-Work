import java.util.ArrayList;
public class GetandSet{
	public static void main(String[] args) {
		ArrayList<String> cars = new ArrayList<String>();
		cars.add("Volvo");
		cars.add("BMW");
		cars.add("Ford");
		cars.add("Mazda");
		System.out.println(cars.get(0));	// this is how we get items
		
		cars.set(0, "Opel");		//this is how we set ArrayList Object values

		cars.remove(cars.get(0)); 	// removing items
						
		System.out.println(cars.size());	// gettings the Length of the array
	
		//to remove ALL elements we use
		//cars.clear();                              --> but im not gonna put that in for now
	}
}
