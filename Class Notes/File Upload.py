FILE UPLOAD 

---------------Downloading  from a web site ---------------

File Download
by using javascript with selenium code javascript with selenium will be covered inthe future

fileDownload

selenium itself can not verify download files; it can click on the download link but it cannot go outside the browser to verify o
open the download files

Other tools need to be used on order verify open downloaded files

- FILE UPLOAD

selenium handles the file UPLOAD but it does it differently compared to actual user

1. we need to find the element with the input tag
2. we need to know the path to the file we want to UPLOAD
3. do sendkeys by sending the path of the file to the input element


Example: how to UPLOAD

	@Test
	public void fileUpload() {
		driver.get("https://the-internet.herokuapp.com/upload");
		String file = "/Users/arod/Desktop/test-folder/id.png";
		WebElement input = driver.findElement(By.id("file-upload"));
		input.sendKeys(file);
		driver.findElement(By.id("file-submit")).click();
	}













































