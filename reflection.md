# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  The game ran fine on the streamlit but it ran into some logical errors. For instance the secret was 40 and when I entered 50 output was go higher. Then when I entered 39 it said to go lower. So the hint system does not work. Then I entered the correct secret 40 the score in the developer system was -10 but the final score I got was 20.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
| ----- | ----------------- | --------------- | ---------------------- |
| 39          Go higher         Go lower              N/A
| 123123oweingoierngoserg Not a number Used an attempt N/A
| New Game Button New game starts no new game N/A

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

- I used claude for this specific project. 
- The AI determined that the output for the higher/lower was backwards and should be inverted. I asked the AI to apply the simplest change to fix it and it did so. 
- In this specific case I didn't have to reject anything that the AI did because the answers were simple and it worked in testing.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- I tested out the specific bug in the streamlit to make sure it was fixed. 
- One test I ran was the lower test to make sure the message really said lower and it showed that it properly outputted lower when needed.
- AI helped design tests for new bugs it was fixing. I told it to make new test cases and document any changes in the codebase it made.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

- Anytime you interact with a button or an object in streamlit it reruns your entire python script from line 1 to the end 
- Session states are new sessions for any new person interacting with your streamlit app. So if 5 different people open your streamlit app they all have different sessions to make sure they don't interfere with each other.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

- One habit is using test cases for my code. Oftentimes I just think my code works for the basic cases and think it works all the time.
- One thing I will do differently using AI on a coding task is asking what they think the problem is and give different solutions from which I can choose so it implements the best possible solution.
- I always thought AI generated code was messy and buggy but with proper prompting and testing it is possible to build larger scale apps with AI now.