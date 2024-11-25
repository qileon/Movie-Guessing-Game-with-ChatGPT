# Movie Guessing Game with ChatGPT

Welcome to the **Movie Guessing Game**! This is an interactive game where players try to guess a movie title with the help of AI-generated hints, while also earning points for correct guesses and identifying the main star.

## Features

- **ChatGPT-Powered Hints**: Get creative hints about a movie without revealing the answer.
- **Point System**: Earn points for:
  - Correct letter guesses (+3 points)
  - Correct movie title guess (+10 points)
  - Identifying the main star (+5 points)
  - Movie-related information (+3 points)
  - Wrong guesses (-2 points)
- **Interactive Gameplay**: Guess letters or try the full movie name, and see your progress as you go.
- **Dynamic Pathfinding**: The game uses the Dijkstra algorithm to simulate a dynamic path with hints and correct guesses.

## How to Play

1. **Start the Game**: Once you run the script, you will receive an initial hint for the movie.
2. **Guess Letters or Full Movie Name**: You can guess one letter at a time or try to guess the full movie title.
3. **Score Points**:
   - Each correct letter gets you points.
   - Guessing the movie title correctly earns you bonus points.
   - You can also identify the main star and gain points.
4. **Incorrect Guesses**: Wrong guesses will result in a penalty to your score.
5. **End the Game**: When you've guessed the movie title or typed 'quit', the game ends and your final score is displayed.

