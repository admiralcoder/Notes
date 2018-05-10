POM.xml

project in eclipse /TestNG-Maven-Automation

=========== POM CONFIGURATION PLUG IN

	<build>
		<plugins>
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-surefire-plugin</artifactId>
				<version>2.21.0</version>
				<configuration>
					<suiteXmlFiles>
						<suiteXmlFile></suiteXmlFile>
					</suiteXmlFiles>
				</configuration>
			</plugin>
		</plugins>
	</build>



mvn test -Drunner=testng_runner.xml

======= testng_runner execution on Terminal =====

<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >
<suite name="Presta shop smoke tests" verbose="2">
	<test name="Automated tests">
		<classes>
			<class name="com.app.tests.GitHub"></class>
		</classes>
	</test>
</suite>

alexs-MacBook-Pro:TestNG-Maven-Automation arod$ mvn test -Drunner=testng_runner.xml



======= Smoke_test execution on Terminal =====

<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >
<suite name="Presta shop smoke tests" verbose="2">
	<test name="Smoke tests">
		<classes>
			<class name="com.app.tests.GitHub"></class>
		</classes>
	</test>
</suite>

alexs-MacBook-Pro:TestNG-Maven-Automation arod$ mvn test -Drunner=smoke_test.xml




















