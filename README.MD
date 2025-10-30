## 1. Setup
    # 1. Download and install Python (3.8+) on your system from python.org

    # 2. Create the virtual environment:
        python -m venv venv

    # 3. Activate the environment:
        .\venv\Scripts\Activate.ps1

    # 4. Install playwright and pytest-BDD
        pip install pytest pytest-bdd playwright
        playwright install

## 2. How to run the game
    # 1. Execute the command in the terminal with the env activated
        python tictactoe.py
    
## 3. How to run the tests
    # 1. Activate the environment:
        .\venv\Scripts\Activate.ps1

    # 2. To run all the test, execute
        pytest -s -v

    # 3. To run a specific scenario, execute 
        pytest -m scenarioname -s -v
            
    -m: select scenario(replace scenarioname with resultCheck, inputCheck or duplicationCheck)
    -s: Shows print() output and debug statements
    -v: Increases verbosity (shows names of passing tests)
