# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Game's purpose:** This is a classic number-guessing game built with Streamlit. The app picks a random secret number in a range that depends on the chosen difficulty (Easy, Normal, or Hard), and the player repeatedly enters guesses. After each guess, the game reports whether the guess was correct, too high, or too low, optionally shows a "Go Higher/Lower" hint, and tracks a score and a limited number of attempts. The player wins by guessing the secret number before running out of attempts, and can start a new round at any time with the "New Game" button.

**Bugs found and fixes applied:**

1. **Inverted hint messages.** `check_guess` in `logic_utils.py` labeled the outcome correctly (`"Too High"` / `"Too Low"`) but showed the opposite hint text (e.g. a guess that was too high told the player to "Go HIGHER!"). Fixed by swapping the two hint strings so they match their outcome.
2. **Core logic scattered in `app.py`.** `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` were defined directly in the Streamlit script instead of the intended `logic_utils.py` module. Moved all four functions into `logic_utils.py` and had `app.py` import them, so the game logic is unit-testable and separate from the UI.
3. **"New Game" button didn't actually restart the game.** It reset `attempts` and generated a new secret, but never reset `status`, so after a win/loss the game immediately re-displayed "Game over" / "You already won" and stopped. It also regenerated the secret with a hardcoded `random.randint(1, 100)` instead of the selected difficulty's range, and never cleared the guess history. Fixed by resetting `status` to `"playing"`, using the difficulty's `(low, high)` range, and clearing `history`.
4. **Attempts counter appeared to lag by one click.** The "Attempts left" info box and the debug panel were rendered *before* the Submit button's logic (which increments `attempts`) ran later in the script, so a submitted guess looked like it hadn't used an attempt until the *next* click. Fixed by rendering that panel through `st.empty()` placeholders that get filled in *after* the attempt/score updates for that click.
5. **Changing difficulty mid-game didn't reset anything.** Switching from, say, Hard to Easy updated the sidebar's displayed range and attempt limit, but the secret number (and attempts/history) from the old difficulty stuck around. Fixed by tracking the previously selected difficulty in session state and restarting the round (new secret, attempts, status, history) whenever it changes.
6. **Difficulty ranges were backwards.** Hard's guessing range (1–50) was narrower than Normal's (1–100), which made Normal objectively harder to guess correctly than Hard. Fixed by widening the range as difficulty increases: Easy 1–20, Normal 1–50, Hard 1–100.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Run `streamlit run app.py`. The sidebar shows the current difficulty (default "Normal"), its guessing range (1 to 50), and how many attempts are allowed (8).
2. Open "Developer Debug Info" to reveal the secret number so you can guess it correctly.
3. Enter a guess lower than the secret and click "Submit Guess 🚀". The game correctly shows "📈 Go HIGHER!" and immediately decrements "Attempts left" by one.
4. Enter a guess higher than the secret and submit again. The game shows "📉 Go LOWER!" and the attempts counter drops again right away.
5. Switch the difficulty in the sidebar (e.g. to "Hard"). The range updates to 1–100, a brand-new secret is drawn from that range, and attempts/history reset to a fresh round.
6. Enter the exact secret number and submit. The game shows a win message with balloons, your final score, and reveals the secret.
7. Click "New Game 🔁" to confirm the round fully resets — a new secret, attempts back to 0, and the win/loss screen clears so you can play again immediately.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ pytest tests/ -v
============================= test session starts ==============================
collected 7 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 14%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 28%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 42%]
tests/test_game_logic.py::test_too_high_message_says_lower PASSED        [ 57%]
tests/test_game_logic.py::test_too_low_message_says_higher PASSED        [ 71%]
tests/test_game_logic.py::test_normal_range_is_not_full_range PASSED     [ 85%]
tests/test_game_logic.py::test_difficulty_ranges_widen_with_difficulty PASSED [100%]

============================== 7 passed in 0.01s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
