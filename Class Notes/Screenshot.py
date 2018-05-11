03/21/2018 

Practice 

RECAP

hooks class : @Before, @After
cucumber annotations

we can create our own tags:
		tags --> We can put tags on a feauture file or on specific Scenarios


Taking screenshots using selenium WebDriver.

	getScreenshoAs


Sample:

	WebDriver driver = new ChromeDriver();

	public class ChromeDriver implements WebDriver,TakesScreenShot{


	}

-- How to take screen shot as file ---

File screenshotFile = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
String screenshotBase64 = ((TakesScreenshot) driver).getScreenshotAs(OutputType.BASE64);
 
-- Casting to Takes Screen shot interfacetype to get screen shot --

	if(scenario.isFailed()) {
				// taking a screenshot
		final byte[] screenshot = ((TakesScreenshot) Driver.getDriver()).getScreenshotAs(OutputType.BYTES);
		// adding the screenshot to the report 
		scenario.embed(screenshot, "image/png");
		}
		

		
















