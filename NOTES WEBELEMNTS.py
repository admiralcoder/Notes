Web Element 

Dynamic IDs => they change depending onthe tools they use to generate those tools The Xpath will not work next time the web page is refreshed it will generate a new number

	<input name = "dsfds" id="u_0_b">

================= E[starts-with(@A, 't')] ===============

--------  STARTS-WITH ---------

E[starts-with(@A, 't')]

* E[starts-with(@A, 't')] formula for x path that locates elements with given input and attribute with begining test of its value 

--------- ENDS-WITH -------------

//E[ends-with(@A, 't')]

*E[ends-with(@A, 't')] formula for xpath that locates elements with given input and attribute with ending test of its value

------------- CONTAINS ----------------

//E[contains-with(@A, 't')]  formula for xpath that locates elements with given input and attribute with containing text of its value

	tag is input 
	and always starts with  u_0_

	//E[starts-with(@A, 't')]
	//input [starts-with(@id,'u_0_')]   <-- this is a xpath


	//....Relatice xpath
	/ ....Absolute xpath

====================== <LABEL starts with for,"j_id..." ================

	<label for="j_idt117:basic:0">Xbox One</label>

	//label[starts-with(@for,'j_idt117')]




========================= CSS E[^='t'] =========================

E[*='t'] --- CONTAINS
		input [id*= 'u_']

E[^='t'] --- STARTS WITH
		input [id^= 'u_']

E[$='t'] --- ENDS WITH
		input [id$= 'u_']



How to test Xpath On Firefox

	open developers tools firefox
	select option console
	put the xpath in this text $x(""), between the double qoutes
	type the xpath in the console

	....go to console and type >> allow pasting
	$x("//input[starts-with(@A, 't')]"). ---> firefox Xpath 


==================== SOME THINGS WORK ON XPATH / CSS, SOME DONT ============

CSS --> we cant use anything that is related to text
		also css does not do indexing
		can not jump to parent from top to bottom 



How DO YOU HANDLE DYNAMIC IDS ???
1. Find the static part of the ID and write locator based on that 
2. Find a fixed element who is related to that element 
	a. locate the fixed
	b. point to target from that fixed element


====================== Locating Based on PARENT ELEMENT ==================

find the second Help link on amazon home page(the one in the bottom of the page)

<a href='asda'>Help</a>   <----this is a  link from a website inspector


1. find the element that ocntain only the second help link

	//div[@id='navFooter']
	//a[.='Help']

2. find the actual element with xpath that does not have to find it uniquely

	//div[@id='navFooter']//a[.='Help']

3. Add those xpaths

	//div[@id='navFooter']//a[.='Help']


************

// input [@id='a'][@name='b'] => can be done for xpath or CSS conbine
// input [@name='b']

************

FIND USING COUNT for same same

1. write an xpath that matches all the elements

	//a[.='Help']

2. pass index of the element you want to identify
	
	()[i] => 1 based count
	(//a[.='Help'])[1] ----> will find first Help link on Amazon.com
	(//a[.='Help'])[2] ----> will find second Help link on Amazon.com



========================= THREAD SLEEP VS IMPLICIT WAIT=================

Thread.sleep()  --- put the program to sleep

		Thread.sleep(2000);

implicit wait ----- only kicks in when we findELement method is called it is set only once, ony wait during the execution if findElement method
		
		driver.manage().timeouts().implicitlyWait(3, TimeUnit.SECONDS);




=========

AssertFalse -->expected false condition to be passed opposite of assert true

elementnotclickable -->selenium found the element but its is hidden behind another one thats why it cannot click

elementNotFound
				a. when the locator: id, name xpath is wrong
				b. locator is good but we did not wait long enough
				

findelements 
				a.	returns a list of web elementsall the elements that match the locator will be returned
				b.  if locators does not match anything it just return an empty list it will throw the NoSuchElementException


--------------------   dropdown list ----------------------
dropdown are represented by tag called select most of the ime selenium usese theleemen with the select tage to work with dropdown
operations we can do on dropdown:

see whats selected
see what are the options
make selection

in order to work with dropdowns we need to create a new object of tpe select we can create select object by passing an element with select tag as constructor in order to be able to create a select object we must pass element with select tag

list.getFirstSelectedOption();   => Allows you to select the first option

list.getAllSelectedOptions();    => returns all options which are selected some drops down allow multiple selections 

link.selectByVisibleText("Option 1"); => will return the specific name of the drop down menu based on the text display


list.getOptions();   => get all options

list.selectByIndex(); => select by Index

list.selectByValue(); => selects option based on the value of the value attribute of the option

fore +commandspace will fill out the for each loop 


what if THERE IS NO SELECT TAG

1. you have to lael for the dropdown separately as a webelement the label shows whats selcted is also shows the options when we click on it if we want to select we have to find a label and click on it to be able to open the list
2. locate the option you want to select separately perform select operation by doing the click() method on the option you want to select. so just click.



