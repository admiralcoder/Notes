



Assertion vs Verification

Assertion -> of any validation fails, the whole tests will fail, the execution
will stop

Verification -> if any validation fails we can still continue with the test

@Test
        public void test() {
                SoftAssert softAssert= new SoftAssert()
        }


SoftAssert = is a class provided by testNG, provides assertion methods
Which will not stop the execution if any of them fail

when softAssert class is used assertion method do not run immediatly

@Test
        public void test() {
                SoftAssert softAssert = new SoftAssert();
                
                softAssert.assertEquals(1, 1);
                softAssert.assertAll();
                
        }

Without softAssert.AssertAll() it will not show what has failed so its 
important 

AssertAll() --> this method will actually run the assertions and report
this method has to be caleld when soft assertions are user

End to End testing = testing a certain flow of te functionality form begi
ning to the end.single application will have multiple end to end flowsi

all assertion methods are overloaded methods and they can take extra
string paramether

Assert.fail() when this line is called the test will fail. This method


