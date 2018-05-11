PRE-CLASS

Amazon  add to cart feature
PAGE OBJECT MODEL

1: HOMEPAGE class => 2: RESULTPAGE class =>3: ITEMS DETAILS PAGE class =>4: SHOPPING CART PAGE class =>5: LOG IN PAGE class =>6: CHECK OUT PAGE class

+++++++++ HOMEPAGE CLASS " PAGE OBJECT "++++++++++
1: HOMEPAGE class : INSIDE HOME PAGE WE HAVE 
				- searchBox
				- searchButton

	public class HOMEPAGE{

		private WebElement driver;

		public HOMEPAGE(WebDriver driver){
		this.driver = driver;
		pageFactory.iniElements(driver.this);
	}

		@FindBy(id="twotabsearchtextbox")
		public WebElement searchBox;

		@FindBy(xpath="[@value='Go']")
		public WebElement searchButton
		
	}







@Test
public void search(){
	WebDriver driver = new ChromeDriver();

	driver.get("https://www.amazon.com/");
}