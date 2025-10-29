import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from playwright.sync_api import Page
from tictactoe import win_check, full_board_check 

# Link the feature file
scenarios('features/tictactoe.feature')

# --- GIVEN DEFINITIONS ---

@given("a clean Tic-Tac-Toe board")
def clean_board(board):
    """The 'board' fixture already provides a clean board."""
    assert all(cell == ' ' for cell in board[1:])
    return board

@given(parsers.parse("player '{player}' has marked positions \"{positions}\""))
def mark_positions(board, player, positions):
    # Convert positions string to a list of integers
    positions_list = [int(p.strip()) for p in positions.split(',')]
    
    mark = 'X' if player == 'X' else 'O'
    
    # Mark the board
    for pos in positions_list:
        board[pos] = mark
    
    return board

@given(parsers.parse("the board is marked with non-winning moves in \"{x_positions}\" by 'X'"))
def mark_x_draw(board, x_positions):
    positions_list = [int(p.strip()) for p in x_positions.split(',')]
    for pos in positions_list:
        board[pos] = 'X'
    return board

@given(parsers.parse("the board is marked with non-winning moves in \"{o_positions}\" by 'O'"))
def mark_o_draw(board, o_positions):
    positions_list = [int(p.strip()) for p in o_positions.split(',')]
    for pos in positions_list:
        board[pos] = 'O'
    return board

# --- WHEN DEFINITIONS ---

@when("the win check function is executed")
def check_win(board, request):
    # Save the result of the check in the Pytest session context
    request.session.win_result = win_check(board)

@when("the full board check function is executed")
def check_full_board(board, request):
    # Save the result in the Pytest session context
    request.session.full_result = full_board_check(board)

# --- THEN DEFINITIONS ---

@then("a win should be detected")
def assertion_win(request):
    # Check the saved result
    assert request.session.win_result is True

@then("the board should be detected as full")
def assertion_full_board(request):
    # Check the saved result
    assert request.session.full_result is True