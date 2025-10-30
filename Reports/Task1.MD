>In this file i will explain my approach for the task 1 of the home assignment

## 1. Challenge chosen
    For the assignment i tested the challenge #1 because im used to test login inputs in my current job

## 2. Checks found
    -First I wanted to try a regular input "aaa" and found check AVERAGE VALUE

    -I tried then an empty input and found check EMPTY

    -Then I tested the limits of the input with "a", a 30 character input and a +30 character input and found MINIMUM VALUE, MAXIMUM VALUE, MORE THAN MAXIMUM VALUE and OTHER CHARS THAN ALPHABETIC because i used numbers in the inputs

    -I submited "two words" to test for multiple words inputs and found SPACE IN THE MIDDLE, that made me check " ", " word" and "word " for spaces and found SPACE, SPACE VALUES AT THE BEGGINING, SPACE VALUES AT THE END

    -Then I submited "ç" to test special values and found check NON ASCII

    -Then I inspected the elements of the web and found the comment about missing resources and clicking of them i found "detailsoverviewnow.css" is missing so i used as the input to get MISSING CSS, also found the comment asking to input "dfjwGGe82H43g3uRiy53h" to check YOU LOOK AT THE PAGE SOURCE. Also the value user_rights_as_admin=0 and changed to 1 to check YOU MADE THE USER ADMIN

    -Then i looked at the HTTTP requests in network and found a 404 with the hidden input "oi32jnxd42390slk345" in the cookie and found YOU LOOKED AT THE COOKIE

    I was out of ideas so I clicked on "learn how to solve the challenges" and the video for challenge #1 was free, so I watched and found the missing checks YOU USED HTML TAGS,BASIC SQL INJECTION and BASIC XSS with the inputs <html>, 'sql injection' and <script></script>

## 3. Reflections
    Half of the checks were intuitive and the usual inputs you want to check. Then the ones hidden in the source code and the HTTP requests are not really the test cases a login input testplan but its always useful to check all the info and I think they are added to check the skills for frontend testing in general. The last 3 checks i couldn't find without the video I usually don't check for a input testing because they will be treated as regular strings most of the times. 
    
    I attached the screeshot with the completion in this folder.

