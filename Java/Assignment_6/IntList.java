import java.util.*;
public class IntList{public static void main(String[] args) {
	//create ArrayList for <ints>
	int[] numberList = new int[5]; 
	//add ints
	numberList[0] = 11;
	numberList[1] = 22;
	numberList[2] = 6;
	numberList[3] = 89;
	numberList[4] = 99;
	
	
	//do the rest
	numberList.length = numberList.length + 1;
	numberList[2] = 50;
	System.out.println(numberList);

	numberList.remove(1);
	System.out.println(numberList);

	numberList.remove(0);
	System.out.println(numberList);


