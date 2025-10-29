
Feature: Tic Tac Toe Full Game State
  As a player
  I want to check the final state of the board
  So that I know if the game is won, drawn, or ongoing

  @ResultCheck
  Scenario Outline: Check Game Result based on Move Sequence
    Given a clean Tic-Tac-Toe board
    And the following moves have been made: "<moves>"
    When the game state check is executed
    Then the final game result should be "<expected_result>" with winner "<expected_winner>"

    Examples:
      | moves                  | expected_result | expected_winner | Moves Count |
      | 1,2,5,4,9              | Win             | Player 1        | 5           | 
      | 4,1,5,2,9,3            | Win             | Player 2        | 5           | 
      | 1,4,2,5,6,7,3          | Win             | Player 1        | 7           | 
      | 5,3,9,1,2,8,6,4,7      | Draw            | None            | 9           | 
      | 1,4,2,5,8,7            | No Win/Draw     | None            | 6           | 


@inputCheck
Scenario Outline: Rejecting System-Level Invalid Inputs
  Given a clean Tic-Tac-Toe board
  And the sequence of user inputs is set to "<inputs>"
  When the player completes the turn with the given inputs
  Then the board should contain the valid move at position <final_position>
  
  Examples:
    | inputs                | final_position |                                           
    | hello, 10, 7          | 7              | #Rejects non-int ('hello') & out-of-range (10), marks 7 
    | 10, 0, 4              | 4              | #Rejects out-of-range (10, 0), marks 4            

@duplicationCheck
Scenario Outline: Rejecting Duplicate Moves
  Given a clean Tic-Tac-Toe board
  # The sequence starts with a valid move, followed by a duplicate failure, then the final success.
  And the sequence of user inputs is set to "<inputs>"
  When the player completes the turn with the given inputs
  # We check two things: the duplicate spot is unchanged, and the new spot is marked by 'O' (Player 2)
  Then the duplicate position <duplicate_pos> remains unchanged and <new_pos> is marked

  Examples:
    # Sequence: V-X, D-Fail, V-O
    | inputs                | duplicate_pos | new_pos | Description                               |
    | 4, 4, 3               | 4             | 3       | X marks 4, O attempts 4 (duplicate), O marks 3 |
    | 1, 1, 2               | 1             | 2       | X marks 1, O marks 2, X attempts 1 (duplicate), X marks 5 |      