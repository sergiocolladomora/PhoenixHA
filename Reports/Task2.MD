## 1. Application created
    With the reference of the rock, paper,scissors i created a tic tac toe game console app in python. The app works as a regular tic tac toe game where each player takes turns to mark with 'X' or 'O' a 3x3 board by console input choosing the positions from 1 to 9 as shown in the intro of the game to try to make 3 mark in a row, column or diagonal. 
    
    The code for the game is in the file tictactoe.py. Instructions on how to run the game are in README.MD

## 2. Tests created
    For the testing i created a Playwright project in python for automation testing. I created 3 different scenarios with multiple executions by using scenario outline with examples. The scenarios use gherkin logic and are coded in game.feature, inside tests folder. 
    
    The steps for the scenarios are coded in test_definitions.py in the tests folder too.

    The conftest.py file has the fixtures to help set up the tests.

    The file pytest.ini is used to help pytest find the features and steps defined, i put all the steps and scenarios in the same files and the same folder because pytest was having a lot of trouble to find the files while running and this was the only structure it was able to run. Instructions on how to run the tests in README.MD

## 3. Test execution
    The tests execution all passed for the examples shown. New examples can be added if it follows the logic of the tests, incorrect data in the examples will make the tests fail. The execution are really fast because it only calls for local functions on the project, there is no need to use multiple workers even if adding a lot of examples

## 4. Reflections
    After running the tests it can be said that the tictactoe app is working correctly and it would pass the QA testing (even though the tests can be improved, for example including a new scenario for testing the replay option of the game as i was planning but unfortunally i had no more time).

    Something I noticed (as is my first python playwright project) is that playwright works better as a typescript/javascript project particullary with finding the features to test, it is much easier with npm rather than pytest and gives you more freedom to organize features and steps.

    At last, i wanted to mention that testing the mark_position() function was more challenging than expected with the user inputs and infinite loops. Using Gemini code assistant was really heplful here to create the fixtures and steps necessary to mock the inputs, and i learnt a lot with it.