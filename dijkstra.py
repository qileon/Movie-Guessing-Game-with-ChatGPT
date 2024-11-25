import openai
import heapq

def get_api_key():
    return input("Enter your ChatGPT API key: ").strip()

def get_chatgpt_hint(movie_name):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for a movie guessing game."},
                {"role": "user", "content": f"Provide a creative hint for the movie: '{movie_name}' without revealing the answer."}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error fetching hint: {e}"

def dijkstra(graph, start_node, target_node):
    queue = [(0, start_node)]
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    shortest_path = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    path = []
    while target_node:
        path.insert(0, target_node)
        target_node = shortest_path[target_node]

    return distances, path

def print_movie_name(movie_name, guessed_letters):
    display_name = ''.join([letter if letter.lower() in guessed_letters else '_' for letter in movie_name])
    print(f"Movie name: {display_name}")

# this function updates the game path based on the guessed letters and the movie name
def update_game_path(graph, guessed_letters, movie_name):
    path = []
    for node in graph:
        if any(letter.lower() in guessed_letters for letter in node.lower()):
            path.append(node)
    return path

def dijkstra_guess_game(movie_name, main_star, info):
    api_key = get_api_key()
    openai.api_key = api_key

    print("\n🎬 Welcome to the Ultimate Movie Guessing Challenge! 🎬")
    print("\nGame Rules:")
    print("1. Guess one letter at a time or try the full movie name")
    print("2. Identify the main star for bonus points")
    print("3. Each correct letter: +3 points")
    print("4. Correct movie name: +10 points")
    print("5. Identifying main star: +5 points")
    print("6. Wrong guess: -2 points")

    hint = get_chatgpt_hint(movie_name)
    print(f"\n🎯 Hint: {hint}\n")

    graph = {
        "Start": [("Hint 1", 2), ("Hint 2", 4)],
        "Hint 1": [("Hint 3", 1), ("Hint 4", 3)],
        "Hint 2": [("Hint 4", 1)],
        "Hint 3": [("End", 5)],
        "Hint 4": [("End", 2)],
        "End": []
    }

    # this section calculates the shortest path in the background for solving the movie
    # it is not necessary for the user to see this, so im commenting it out

    # print("\nFinding the shortest path to solve the movie...")
    # distances, path = dijkstra(graph, "Start", "End")
    # print(f"Initial Path: {' -> '.join(path)}")
    # print(f"Total distance: {distances['End']}")

    guessed_name = ""
    score = 0
    guessed_letters = set()
    incorrect_guesses = []

    # this section handles the scoring based on user guesses, providing feedback for correct or incorrect guesses
    while True:
        print_movie_name(movie_name, guessed_letters)

        current_path = update_game_path(graph, guessed_letters, movie_name)
        print(f"Current Path: {' -> '.join(current_path)}")

        guess = input("\nEnter your guess (or type 'quit' to exit): ").strip().lower()

        if guess == 'quit':
            print("Exiting the game. Thanks for playing!")
            break

        if guess in guessed_letters:
            print("You've already guessed this letter!")
            continue

        guessed_letters.add(guess)

        if guess == movie_name.lower():
            score += 10
            print("🎉 Brilliant! You've guessed the movie title! (+10 points)")
            break
        elif guess == main_star.lower():
            score += 4
            print("⭐ Amazing! You've identified the main star! (+4 points)")
        elif guess in info.lower():
            score += 3
            print("📚 Nice! That detail is related to the movie! (+3 points)")
        elif guess in movie_name.lower():
            score += 2
            print("✓ Correct direction! (+2 points)")
        else:
            incorrect_guesses.append(guess)
            score -= 2
            print("❌ Not quite right! (-2 points)")

        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        print(f"Current score: {score}")

    print(f"\nGame Over! Your final score is {score}.")

movie_name = "Arcane"
main_star = "Orianna"
info = "An animated series set in the League of Legends universe, exploring the origins of two iconic characters."

dijkstra_guess_game(movie_name, main_star, info)
