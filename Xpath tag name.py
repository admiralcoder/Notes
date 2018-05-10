
================  TAG NAME for <input ===================

<input type="text" class="inputtext _58mg _5dba _2ph-" data-type="text" name="firstname" aria-required="1" placeholder="" aria-label="First name" id="u_0_p">

input -> TagName

Attributes -> class, name 

value -> "inputtext","firstname"


-------------- Xpath path expresion syntax -------------------

//tagName[@attribute='value']
//input[@class='inputtext']


Example1:

<input value="Log In" tabindex="4" data-testid="royal_login_button" type="submit" id="u_0_3">

Xpath

//input[@value='Log In']


Example2:

<input type="email" class="inputtext" name="email" id="email" tabindex="1" data-testid="royal_email">

Xpath

//input[@class='inputtext']


Example3:

<input type="password" class="inputtext" name="pass" id="pass" tabindex="2" data-testid="royal_pass">

//input[@type='password'][@class='inputtext'][@name='pass']





