LOCAL Date and Time and LAMBDA

=================== LOCAL DATE ============================

LocalDate birthday = LocalDate.of(1986, 5, 5);
		System.out.println("Alex BDAY is: "+birthday);
		
LocalDate birthday2 = LocalDate.of(1987, Month.FEBRUARY, 14);
		System.out.println("Melisa BDAY is: "+birthday2);

=================== LOCAL TIME ============================

LocalTime f2 = LocalTime.of(5, 01);
		System.out.println("Sunday Class ends Hours and Minutes: "+f2);
		
LocalTime f3 = LocalTime.of(5, 00, 33);
		System.out.println("Sunday Class ends Hours, minutes, seconds: "+f3);
		
LocalTime f = LocalTime.of(5, 00, 00, 00);
		System.out.println("Sunday Class ends hours,minute,seconds,nanoseconds: "+f);

=================== LOCAL DATE & TIME =====================

LocalDateTime time = LocalDateTime.of(birthday, f);
		System.out.println(time);
		
LocalDateTime time2 = LocalDateTime.of(2018, 02, 10, 4, 44);
		System.out.println(time2);





=================== LAMBDA =====================


Abstract type like Abstractclass and interfaces can not be instanciated directly it should be assigned to sub classes or eimplementing 
classes of the interfaces










