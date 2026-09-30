from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_too_high_message_says_lower():
    # Bug fix: guess of 60 vs secret 50 was telling the player to go HIGHER
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_message_says_higher():
    # Bug fix: guess of 40 vs secret 50 was telling the player to go LOWER
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_normal_range_is_not_full_range():
    # Bug fix: New Game used to use a hardcoded 1-100 range instead of the
    # difficulty's own range (e.g. Normal should be 1-50, not the full 1-100)
    assert get_range_for_difficulty("Normal") == (1, 50)

def test_difficulty_ranges_widen_with_difficulty():
    # Bug fix: Hard's range (1-50) used to be narrower than Normal's
    # (1-100), making Normal harder to guess than Hard. Ranges should
    # widen as difficulty increases: Easy < Normal < Hard.
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")
    assert (easy_high - easy_low) < (normal_high - normal_low) < (hard_high - hard_low)
