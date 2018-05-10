ACTIONS in JAVA

-------------- HOVER OVER MOUSE ----------------


Actions is a class that provides metods for advanced user interactions
such as hovering the mouse, double click, right click, scroll, drag and drop

- hovering = perform() actually will perform the actions
movesToElement method that takes an element as a parameter and moves the mouse over that element

moveToElement(el).perform();
Example 1: hover over the mouse on the hello sign in in amazon.com

@Test
	public void HoverTest(){
		driver.get("https://www.amazon.com/");
		˜


-------------- DRAG AND DROP ----------------

build() --> required when multiple actions are called at the same time it must be called 
before the perform


("source") = WHAT YOU WANT TO DROP
("target") = WHERE YOU WANT TO DROP IT

++++ OPTION 1 ++++++

@Test
	public void dragAndDrop() throws InterruptedException {
		driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index");
		Actions actions= new Actions(driver);
		WebElement source = driver.findElement(By.id("draggable"));
		WebElement target = driver.findElement(By.id("droptarget"));
		actions.dragAndDrop(source, target).perform();
		
		Thread.sleep(3000);
		driver.quit();
	}


++++ OPTION 2 ++++++

@Test
	public void dragAndDrop2() throws InterruptedException {
		driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index");
		Actions actions = new Actions(driver);
		//what you want to drop
		WebElement source = driver.findElement(By.id("draggable"));
		// where you want to drop it
		WebElement target = driver.findElement(By.id("droptarget"));
		//move mouse to element
		//click and hold
		//move to second element
		//release 
		actions.moveToElement(source).clickAndHold().moveToElement(target).release().build().perform();
		Thread.sleep(3000);
		driver.quit();

	}



-------------- DOUBLE CLICK ----------------

 @Test
	public void doubleClick() throws InterruptedException {
		Actions actions = new Actions(driver);
		driver.get("https://www.primefaces.org/showcase/ui/misc/effect.xhtml");
		WebElement fold = driver.findElement(By.id("fold"));
		WebElement puff = driver.findElement(By.id("puff"));
		WebElement slide = driver.findElement(By.id("slide"));
		WebElement scale = driver.findElement(By.id("scale"));

		actions.doubleClick(slide).perform();

		Thread.sleep(3000);
		driver.quit();
	}

-------------- PAGE DOWN A BOX INSIDE A WEB SITE (box)----------------


@Test
	public void scroll() throws InterruptedException {
		Actions actions = new Actions(driver);
		driver.get("http://jscroll.com/");
		//find the element
		//click
		//click page down
		WebElement element = driver.findElement(By.xpath("//h3[.='Page 1 of jScroll Example - jQuery Infinite Scrolling Plugin']"));
		actions.moveToElement(element).click().sendKeys(Keys.PAGE_DOWN).perform();

		Thread.sleep(3000);
		driver.quit();
	}

--------- SCROLL MAIN PAGE DOWN EVERY 2 SECONDS SO PAGE LOADS ---------

@Test
	public void generalScroll() throws InterruptedException {
		Actions actions = new Actions(driver);
		driver.get("http://jscroll.com/");
		WebElement element = driver
				.findElement(By.xpath("//h2[.='About jScroll']"));
		actions.moveToElement(element).click().sendKeys(Keys.PAGE_DOWN).perform();
		Thread.sleep(3000);
		actions.moveToElement(element).click().sendKeys(Keys.PAGE_DOWN).perform();
		Thread.sleep(3000);
		actions.moveToElement(element).click().sendKeys(Keys.PAGE_DOWN).perform();
		Thread.sleep(3000);
	}




	









































