import java.util.*; 
public class txtInputMatrix {
	public static void main(String[] args){
		int[][] m1 = {{1,4,6}, {3,8,5}};
		int[][] m2 = {{4,3,7}, {2,5,1}};

		//creating scanner
		Scanner myObj = new Scanner(System.in);


		for (int c=0; c<3; c++){
			System.out.println("Col");
			for (int r=0; r<3; r++){
				System.out.println("Row");
				System.out.println("Enter M1 Number: ");
			       	m1[c][r] = myObj.nextInt();
				myObj.nextLine();		//eat enter 

				System.out.println("Enter M2 Number: ");
				m2[c][r] = myObj.nextInt();
				myObj.nextLine();		//eat enter 
			}
		}
	}
}

