03/14/2018

TestNG-Maven-Automation

============ FRAMEWORK ==============

- Companies are using simular type of framework

Java+Selenium+TestNG+Maven+Git

1: Create a new project TestNG-Maven-Automation
2: pom.xml
3: Identify JDK version, set to 1.8
4: Create framework structure ( where you wanna say what)


==== MAVEN VERSION 1.8 =============

<properties>
		<maven.compiler.source>1.8</maven.compiler.source>
		<maven.compiler.target>1.8</maven.compiler.target>
</properties>



====== DEPENDECY TESTNG =============

url: http://mvnrepository.com/artifact/org.testng/testng/6.14.2


		<dependency>
			<groupId>org.testng</groupId>
			<artifactId>testng</artifactId>
			<version>6.14.2</version>
		</dependency>

======== DEPENDECY WEBDRIVER =========
url: http://mvnrepository.com/artifact/io.github.bonigarcia/webdrivermanager/2.1.0

		<dependency>
			<groupId>io.github.bonigarcia</groupId>
			<artifactId>webdrivermanager</artifactId>
			<version>2.1.0</version>
		</dependency>


======= DEPENDECY JAVA =============
url: http://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-java/3.11.0

		<dependency>
   			 <groupId>org.seleniumhq.selenium</groupId>
   			 <artifactId>selenium-java</artifactId>
    		<version>3.11.0</version>
		</dependency> 


=========================================

Selenium delete those 2 folders 

		  src/main/Java
		  src/main/resource

========= src/test/resources =================
DELETE also:
resources only test resources go there not .java files

===============================================

What is Singleton Pattern:

Factory pattern ->  what kind of design pattern


========= 

+++ Interview question what you put on your testbase class 
we put before class 
after class 


======= 
++ Interview questions?

how do you get all the links text into array list find element by tag name a
loop and add to array 

	@Test
	public void getAllLinks() {
		driver.get("https://github.com/");
		List<WebElement> links = driver.findElements(By.tagName("a"));
		// saving it to array list
		List<String> linkTexts = new ArrayList<>();

		for (WebElement link : links) {
			if (!link.getText().isEmpty()) {
				linkTexts.add(link.getText());
			}
		}
		System.out.println(linkTexts);
	}


++ Interview questions

Create a method that accepts a locator by object 
returns arraylist containing texts for all matching findElements


store into browserUtil class 


	public static List<String> getElementsText(By locator){

		List<WebElement> elems = driver.findElements(locator);
		List<String> elemTexts = new ArrayList<>();

		for(WebElement el : elems){
			if(!el.gettext().isEmpty()){
			elemTexts.add(el.getText());
			}
		}
		return elemTexts;
	}
















































