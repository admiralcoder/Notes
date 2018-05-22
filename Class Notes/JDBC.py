JDBC

JAVA DATABASE CONNECTIVITY (JDBC) API IS the industry standard
for database independent connectivity between the java programming language
and a wide range of databases. 

SQL database and other tabular data sources such as spreadsheets or flat files

the JDBC API provides a call level API for SQL based database access.

Example:

    you have your code: 3343 then you ask JDBC to connect to the database

    JDBC is like a waiter. when you order food in a restaurant. 

-- JDBC is a JAR file

How does it work. 
    we have our "CODE" -> which connects to "JDBC" -> then we have our "ORACLE DRIVER"
    -> it will connect to "ORACLE DATABASE" that is running on our cloud machine.

example 2: 
    we have "code" -> which connects to selenium -> selenium connects to Chromedriver
    -> and then it opens Chrome browser

Create a class: 

String oracledburl="jdbc:oracle:thin:@ec2-52-87-176-139.compute-1.amazonaws.com:1521:xe";

thin : is a basic jdbc driver to connect to the oracle database


JDBC 3 important classes: 
    - Connection -> Helps Connect to database 
    - Statement -> Helps write SQL queries and get data and execute
    - ResultSet -> Data that comes from database will be stored in ResultSet format

Connection connection = DriverManager.getConnection();

Connection is interface: interview questions how are you using it on your current
                        project. in JDBC 


ResultSet methods: 
next() -> moves to next row 
getObject(colname/index) -> read data from column

last() ->
getRow() ->

ResultSet.TYPE_SCROLL_INSENSITIVE = turn off the feature that is 
restricting us to go back and forth. 

ResultSet.CONCUR_UPDATABLE = means if someone adds new row it will not
affect my resut. it will be in sinc mode 


last() = goes to last row
first() = goes to first row
getRow() = current row number

beforeFirst() = goes to row 0
afterlast() = goes to "second table"
absolute(rowNum) = jumps to specified row. 

	@Test
	public void oracle2() throws SQLException {
			Connection connection = DriverManager.getConnection(oracledburl,oraclePassword,oracleDbusername);
		//	Statement statement = connection.createStatement();
			Statement statement = connection.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE,ResultSet.CONCUR_READ_ONLY);
			ResultSet resultset = statement.executeQuery("select * from countries");
			
			// find out how many records in resultSet
			resultset.last();
			int rowsCount = resultset.getRow();
			assertEquals(rowsCount, 25);
			System.out.println(rowsCount);
			
			resultset.beforeFirst();
			while(resultset.next()) {
				System.out.println(resultset.getString(1)+" "
			+resultset.getString("country_name")+" "+resultset.getString("region_id"));
			}

		}



=== METADATA ===

its data about data

- Meta data programming is useful to know the capbilities limitations 
and facilities of underlying database software and its resources
- when you 

JDBC metadata programming supports
    - database metadata
    - resultSet metadata
    - parameter metadata

metadata we need it for our result set. 

	@Test
	public void metadata() throws SQLException {
		Connection connection = DriverManager.getConnection(oracledburl,oraclePassword,oracleDbusername);
	//	Statement statement = connection.createStatement();
		Statement statement = connection.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE,ResultSet.CONCUR_READ_ONLY);
		String sql = "select employee_id, last_name,job_id,salary from employees";
		ResultSet resultset = statement.executeQuery(sql);
		//database metadata
		DatabaseMetaData dbMetaData = connection.getMetaData();
		System.out.println("user : "+ dbMetaData.getUserName());
		System.out.println("Database type: "+ dbMetaData.getDatabaseProductName());
		
		//results metadata
		ResultSetMetaData rsMeta= resultset.getMetaData();
		System.out.println(rsMeta.getColumnCount());
		System.out.println(rsMeta.getColumnName(1));
		
		//print all column names using a loop 
		for (int i = 1; i <= rsMeta.getColumnCount(); i++) {
			System.out.println(i+" "+ rsMeta.getColumnName(i));
		}
		
		resultset.close();
		statement.close();
		connection.close();
	}

what do we mean with data STructures?
    - we mean coleections of data. 

What type of data structure we should use so we dont use
Resultset anymore?

if we have multiple rows what do you think we should use?

    - List<Map<String, Object>> queryData =  new Array












WHAT IS DATA STRUCTURES?
 LIST map String 
 tables
 