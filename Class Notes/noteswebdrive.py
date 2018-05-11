GETTING MULTIPLE PRICES 



WebDriver driver;

	@BeforeClass
	public void setup() {
		System.setProperty(Configure.getProperty("webdriver"), Configure.getProperty("driverpath"));
		driver = new ChromeDriver();
		driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
		driver.get(Configure.getProperty("url2"));
	}



@Test
	public void priceTest() {
		HomePageVerification homepageverification = new HomePageVerification(driver);
		List<WebElement> prices = homepageverification.allPrices;
		System.out.println(prices.size());
		
		for (int i = 0; i < prices.size(); i++) {
			String priceTxt= prices.get(i).getText();
			
			if(priceTxt.length()!= 0)
			System.out.println(priceTxt);
		}
		
	}