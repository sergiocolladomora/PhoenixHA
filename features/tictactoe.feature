
Feature: Tic Tac Toe Logic
  As a Tic-Tac-Toe player
  I want to check if a board state results in a win or a draw

  Scenario: Row Win Detection
    Given a clean Tic-Tac-Toe board
    And player 'X' has marked positions "1, 2, 3"
    When the win check function is executed
    Then a win should be detected

  Scenario: Column Win Detection
    Given a clean Tic-Tac-Toe board
    And player 'O' has marked positions "2, 5, 8"
    When the win check function is executed
    Then a win should be detected

  Scenario: Draw Detection (Full Board)
    Given a clean Tic-Tac-Toe board
    And the board is marked with non-winning moves in "1, 3, 4, 6, 7, 9" by 'X'
    And the board is marked with non-winning moves in "5, 2, 8" by 'O'
    When the full board check function is executed
    Then the board should be detected as full