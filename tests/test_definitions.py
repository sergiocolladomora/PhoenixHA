import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from tictactoe import win_check, full_board_check, mark_position

scenarios('game.feature') 

# --- GIVEN DEFINITIONS ---

@given("a clean Tic-Tac-Toe board")
def clean_board(board):
    """Provides a clean Tic-Tac-Toe board."""
    assert all(cell == ' ' for cell in board[1:])
    print("\n Game started with a clean board.")
    return board

@given(parsers.parse("the following moves have been made: {moves}"))
def make_multiple_moves(board, moves):
    """Marks the positions given by the input list alternatively for each player."""
    moves = moves.strip('"')
    move_list = [int(m.strip()) for m in moves.split(',')]
    
    for index, position in enumerate(move_list):
        # Player 1 ('X') always takes even index (0, 2, 4...)
        player_mark = 'X' if index % 2 == 0 else 'O'
        
        # Check for invalid moves
        if board[position] != ' ':
             raise ValueError(f"Position {position} is already taken in the sequence: {moves}")
             
        board[position] = player_mark

        #Check who made the last move 
        if player_mark == 'X':
            pytest.test_session_data['last_player_mark'] = "Player 1"
        else:
            pytest.test_session_data['last_player_mark'] = "Player 2"

        print(f"Player {'1' if player_mark == 'X' else '2'} placed '{player_mark}' at position {position}.")
    
    return board

@given(parsers.parse("the sequence of user inputs is set to \"{inputs}\""))
def setup_mock_inputs(mock_inputs_list: list, inputs: str):
    """Loads the sequence of inputs from the feature table into the mock fixture's list."""
    # Strip quotes and split by comma to get the clean list of inputs
    inputs_list = [i.strip() for i in inputs.strip('"').split(',')]
    
    # Load the inputs into the list that the mock will read from
    mock_inputs_list.extend(inputs_list) 
    print(f"Mock Input Queue set: {inputs_list}")

# --- WHEN DEFINITION ---

@when("the game state check is executed")
def check_game_state(board, request):
    """Check both victory and full board conditions."""

    #Check the game state and saves it in the session
    win_result = win_check(board)
    full_result = full_board_check(board)

    request.session.win_result = win_result
    request.session.full_result = full_result

    #Saves who made the last move to check the winner in case of victory
    request.session.last_player_mark = pytest.test_session_data['last_player_mark']

@when("the player completes the turn with the given inputs")
def call_mark_position_repeatedly(board, mock_inputs_list: list):
    """
    Executes mark_position for each valid move in the sequence,
    switching the turn after each successful move.
    """
    current_player = 'Player 1'
    

    # A maximum number of turns to avoid infinite loops in case of errors
    MAX_TURNS = 20 # Sufficient for any sequence of 9 moves with intermittent errors
    
    for _ in range(MAX_TURNS):
        try:
            # Call the actual game function. It consumes mock inputs until successful or the mock is empty.
            board = mark_position(board, current_player)
            
            # If mark_position returns WITHOUT ERROR: The move was successful.
            # 1. Switch the turn for the next iteration
            current_player = 'Player 2' if current_player == 'Player 1' else 'Player 1'
            
        except StopIteration:
            # This means the mock ran out of inputs. The scenario is finished.
            break 
        except Exception as e:
            # Captures a Python exception (e.g., ValueError from 'hello'). The test should fail here.
            raise AssertionError(f"Test Interrupted: Unexpected Python exception during turn: {e}") from e

# --- THEN DEFINITION ---

@then(parsers.parse("the final game result should be \"{expected_result}\" with winner \"{expected_winner}\""))
def assertion_game_result(expected_result, expected_winner, request):
    """ Check the game result based on expected outcome: Win, Draw, or No Win/Draw."""
    win = request.session.win_result
    full = request.session.full_result
    last_player = request.session.last_player_mark
    
    # 1. Check the actual result
    if win is True:
        actual_result = "Win"
    elif full is True:
        actual_result = "Draw"
    else:
        actual_result = "No Win/Draw"

    # 2. Check the Winner
    if actual_result == "Win":
        # If it's a win, the last player MUST be the winner.
        actual_winner = last_player
    else:
        actual_winner = "None" # For Draw or No Win/Draw
    
    print(f"\n --- RESULT ---")
    print(f"Final state: Victory={win}, Full board={full}")
    print(f"Actual result: {actual_result}")
    print(f"Expected result: {expected_result}")
    
    # 3. Makes the assertions based on expected result and actual game state
    if expected_result == "Win":
        assert win is True, "Expected a Win, but no winning condition was met."
        assert actual_winner == expected_winner, f"Expected winner '{expected_winner}', but actual winner was '{actual_winner}' (Last move)."
        print(f"PASS: Game ended in victory by {actual_winner} as expected. \n")
    
    elif expected_result == "Draw":
        assert win is False, "Expected a Draw, but a player actually won."
        assert full is True, "Expected a Draw, but the board is not full."
        print(f"PASS: Game ended in draw as expected. \n")
            
    elif expected_result == "No Win/Draw":
        assert win is False, "Expected game to be ongoing, but a player won."
        assert full is False, "Expected game to be ongoing, but the board is full (Draw)."
        print(f"PASS: Game is still going as expected.")

@then(parsers.parse("the board should contain the valid move at position {final_position:d}"))
def assert_valid_move_marked(board, final_position: int):
    """
    Asserts that the final position marked is the one expected, 
    assuming the successful mark belongs to 'X' (Player 1) 
    as this step usually verifies the first successful move after errors.
    """
    
    # 1. Ensure the final position is not empty (the valid move did pass).
    assert board[final_position] != ' ', (
        f"Assertion Failed: Position {final_position} was expected to be marked, but it is empty."
    )
    
    # 2. Ensure the marker is 'X' (Player 1, assuming the scenario tests the first successful turn).
    assert board[final_position] == 'X', (
        f"Assertion Failed: Position {final_position} was marked with '{board[final_position]}' instead of 'X'."
    )
    
    print(f"PASS: Position {final_position} was correctly marked after rejecting invalid inputs.")

@then(parsers.parse("the duplicate position {duplicate_pos:d} remains unchanged and {new_pos:d} is marked"))
def assert_duplicate_logic(board, duplicate_pos: int, new_pos: int):
    """
    Verifies that the first move remains on the board and the subsequent valid move
    (after rejection) is correctly marked.
    """
    
    # 1. Verify that the original position (the duplicate attempt) was NOT overwritten.
    # We assume the first move was 'X', so it must remain 'X'.
    assert board[duplicate_pos] == 'X', (
        f"Assertion Failed: The original position {duplicate_pos} was overwritten or cleared."
    )
    
    # 2. Verify that the new (valid) position WAS marked (by 'O' in the second turn).
    # This movement must be 'O' (Player 2) if the sequence is [X, X, O].
    assert board[new_pos] == 'O', (
        f"Assertion Failed: Position {new_pos} was expected to be marked with 'O', but found '{board[new_pos]}'."
    )
    
    print(f"PASS: Duplicate at {duplicate_pos} was successfully ignored and {new_pos} was marked by 'O'.")