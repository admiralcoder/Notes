HOW TO FIND A NUMBER IN A WEB SITE AND VERIFY 

.isDigit(Char c)--> this will store the number from any string



============ UTIL CLASS METHOD TO GET NUMBERS FROM STRINGS =====

**** THIS WILL BE USED IF WE HAVE A WEB SITE WITH NUMBRERS AND LETTERS 
EXAMPLE : http://automationpractice.com/index.php
Sign in
Contact us
Call us now: 0123-456-789 
****


++ THIS IS A METHOD FOR THE UTIL CLASS THAT WILL ONLY GET NUMBERS ++

package com.presshop.Utils2;

public class StringUtility {
	public static void main(String[] args) {
		extractNumberFromString("cybertek003tech112ABC");
		extractNumberFromString("Call us now: 0123-456-789");
		
		
	}

	public static String extractNumberFromString(String targetString) {
		String employeeID = "cybertek003tech112ABC";
		String onlyNumber = "";

		for (int i = 0; i < employeeID.length(); i++) {

			char eachChar = employeeID.charAt(i);

			if (Character.isDigit(eachChar)) {
				// System.out.print(eachChar);
				onlyNumber = onlyNumber + eachChar;// onlyNumber+=eachChar;
			}
		}
		System.out.println(onlyNumber);
		
		
		return onlyNumber;
	}
}









































