Web Tables

table data arranged in a grid format
Table tag used for table


th --> tag used for columm name

tr   --> tag used to indicate a row it applies to all columns it is the whole row Horizontal

td  --> tag used to indicate a columm in a row vertical

 table

 	tr
 			th th th.  --> colum name
 	tr
 			td td td.  --> actual data

tbody --> used to indicate the data of the table does not include colum names


constant class --> class used to save string and other types of data. All variables in constants class are final for example company url can be a constant every time company url is used it must be called from the constants class if the url changes we only need it to change in constant class


Different companies have differnt naming conventions for classesthat hold constant variables

//table[@class='ProductsTable']			= identifies the table 
	//table[@class='ProductsTable']//th = identifies all the colum elements

===========================================================

IF the Slashes are in the begining 
// --> Relative Xpath search anywhere in the page
			//table[@class='ProductsTable']

/  --> Absolute Xpath search starting from the root element(html tag)
			/html/head/body/liv/....

// --> if the slashes are in the middle of a Xpath mean any child or decendant, is a direct child
			//table[@class='ProductsTable']//th
			//table[@class='ProductsTable']//th[2]

===========================================================

//tagname[contains(text(),'text')] --> Xpath for tag that contains certain text

//tagname[.='text'] --> 

id == ctl00_MainContent_orderGrid

//table[@id='ctl00_MainContent_orderGrid']//tr


======================= FINDING COLUMN ============================


1. //table[@id='ctl00_MainContent_orderGrid'] --> finds the table colum
2. //td[2] --> the second td it is family tr | it will match all the td element which is second



XPATH USING THE COUNT

//table/tr[1] --> first tr in that table
//table/tr[2] --> second tr in that table




======================= Locating by row and column ============================

http://secure.smartbearsoftware.com/samples/testcomplete12/weborders/Default.aspx

//table[@id='ctl00_MainContent_orderGrid']//tbody/tr[4]/td[5]


//4TH ROW, 5TH COLUMN
		String text = driver.findElement(By.xpath("//table[@id='ctl00_MainContent_orderGrid']//tbody/tr[4]/td[5]")).getText();
		System.out.println(text);
//6TH ROW, 10 COLUMN
		String text1 = driver.findElement(By.xpath("//table[@id='ctl00_MainContent_orderGrid']//tbody/tr[6]/td[10]")).getText();
		System.out.println(text1);


======================= locating cells in relation to cells ============================

http://secure.smartbearsoftware.com/samples/testcomplete12/weborders/Default.aspx

finding a cell in relation to another cell
1. find cell 1 
2. find a common ancestor for both elements
3. find cell 2 in relation using the common ancestor

step:
1. //td[.='Mark Smith']
2. /..  				--> goes to the parent
3. //td[.='Mark Smith']/../td[11]. --> result to find multiple for example
   //td[.='Paul Brown']/../td[11]  --> they all share same value for 11 post
   //td[.='Bob Feather']/../td[11] --> and you can reuse the xpath by just changing the name



======================= findElement vs findElements =====================

findElement()= returns a single element if the locator matches
				-> if the locator doesnt match  throws an exception
				-> return type: WebElement

findElements()= returns a List of webelements if the locator matches
				-> if the locator doesnt match still returns a empt list
				-> return type: List<WebElement>


TestNG + Selenium are user on medium and corporations

-------- Home Work ------------------------------
write a whole framework that automates a website
-------------------------------------------------










