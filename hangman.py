import random

# English translations
translations_en = {
    'welcome': "Welcome to Hangman!",
    'menu': "\nMenu:",
    'start_game': "1) Start Game",
    'instructions': "2) Instructions",
    'switch_language': "3) Switch Language",
    'random_category': "4) Random Category",
    'exit': "5) Exit",
    'select_option': "Select an option (1/2/3/4/5): ",
    'enter_word': "Player 1, enter a word (letters only, or 'done' to finish): ",
    'invalid_input': "Invalid input. Please enter a word using only letters.",
    'play_hangman': "Let's play Hangman!",
    'already_guessed_letter': "You already guessed the letter {}.",
    'not_in_word': "{} is not in any of the words.",
    'good_job_letter': "Good job, {} is in at least one word!",
    'congrats_word': "Good job, you guessed the phrase '{}' correctly!",
    'invalid_guess': "Invalid guess. Please guess a single letter or the entire phrase.",
    'congrats_win': "Congrats, you guessed all the words! You win!",
    'sorry_lose': "Sorry, you ran out of tries. The correct phrase was '{}'. Maybe next time!",
    'exit_message': "Exiting Hangman. Goodbye!",
    'instructions_en': """
    Instructions:
    1. Player 1 enters multiple words.
    2. Player 2 guesses letters or the entire phrase.
    3. Player 2 has 10 lives represented by the hangman stages.
    4. Player 2 wins if they guess the entire phrase correctly within 10 lives.
    5. Player 1 wins if Player 2 runs out of lives without guessing the entire phrase.

    Note:
    - You can guess a single letter or the entire phrase.
    - If the phrase has multiple words, submit them together without spaces.
    - Example: If the phrase is "shaun davies", you should guess "shaundavies".
    - Type 'exit' at any time to return to the dashboard.
    """
}

# Welsh translations
translations_cy = {
    'welcome': "Croeso i Hangman!",
    'menu': "\nDewislen:",
    'start_game': "1) Dechrau'r Gem",
    'instructions': "2) Cyfarwyddiadau",
    'switch_language': "3) Newid Iaith",
    'random_category': "4) Categori Arall",
    'exit': "5) Gadael",
    'select_option': "Dewiswch opsiwn (1/2/3/4/5): ",
    'enter_word': "Chwaraewr 1, rhowch air (llythrennau'n unig, neu 'gorffen' i orffen): ",
    'invalid_input': "Mewnbwn annilys. Rhowch air gan ddefnyddio llythrennau'n unig.",
    'play_hangman': "Chwarae Hangman!",
    'already_guessed_letter': "Rydych chi eisoes wedi dyfalu'r llythyren {}.",
    'not_in_word': "Nid yw {} yn unrhyw air.",
    'good_job_letter': "Da iawn, mae {} mewn o leiaf un gair!",
    'congrats_word': "Da iawn, gwnaethoch chi ddyfalu'r ymadrodd '{}' yn gywir!",
    'invalid_guess': "Dygwch mewn dyfalu annilys. Rhowch lythyren sengl neu'r holl ymadrodd.",
    'congrats_win': "Llongyfarchiadau, gwnaethoch chi ddyfalu pob gair! Rydych chi'n ennill!",
    'sorry_lose': "Mae'n ddrwg gennym, wnaethoch chi ddod i ben o dreuliau. Yr ymadrodd cywir oedd '{}'. Efallai'r tro nesaf!",
    'exit_message': "Yn gadael Hangman. Hwyl fawr!",
    'instructions_cy': """
    Cyfarwyddiadau:
    1. Mae Chwaraewr 1 yn nodi nifer o eiriau.
    2. Mae Chwaraewr 2 yn dyfalu llythrennau neu'r holl ymadrodd.
    3. Mae Chwaraewr 2 yn 10 bywydau wedi'u cynrychioli gan gamau Hangman.
    4. Chwaraewr 2 yn ennill os ydynt yn dyfalu'r ymadrodd cyfan yn gywir o fewn 10 bywyd.
    5. Mae chwaraewr 1 yn ennill os ydy chwaraewr 2 yn rhedeg allan o fywydau heb ddyfalu'r holl ymadrodd.

    Nodyn:
    - Gallwch ddyfalu llythyren sengl neu'r ymadrodd cyfan.
    - Os yw'r ymadrodd yn cynnwys sawl gair, nodwch hwy gyda'i gilydd heb fannau.
    - Enghraifft: Os yw'r ymadrodd yn "shaun davies", dylech ddyfalu "shaundavies".
    - Teipiwch 'gadael' ar unrhyw adeg i ddychwelyd i'r fwrdd syniadau.
    """
}

# Hangman stages (10 stages)
hangman_stages = [
    '''
       -----
       |   |
           |
           |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
           |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
      /|\  |
           |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
      /|\  |
       |   |
           |
    =========
    ''',
    '''
       -----
       |   |
       O   |
      /|\  |
       |   |
      /    |
    =========
    ''',
    '''
       -----
       |   |
       O   |
      /|\  |
       |   |
      / \  |
    =========
    ''',
    '''
       -----
       |   |
      [O   |
      /|\  |
       |   |
      / \  |
    =========
    ''',
    '''
       -----
       |   |
      [O]  |
      /|\  |
       |   |
      / \  |
    =========
    '''
]

current_language = translations_en  # Default language is English

# Word categories with predefined words
word_categories = {
    'Animals': ['cat', 'dog', 'elephant', 'tiger', 'lion'],
    'Fruits': ['apple', 'banana', 'orange', 'grape', 'pear'],
    'Countries': ['india', 'canada', 'japan', 'brazil', 'france']
}

def get_translation(key):
    """Retrieve translation based on current language."""
    global current_language
    return current_language.get(key, f'Missing translation for key: {key}')

def display_hangman(tries):
    """Display the current hangman stage based on the number of tries left."""
    return hangman_stages[10 - tries]

def get_words():
    """Prompt Player 1 to enter words, validate inputs, and return a list of words."""
    words = []
    while True:
        word = input(get_translation('enter_word')).lower()
        if word == 'done':
            break
        elif word.isalpha():
            words.append(word)
        else:
            print(get_translation('invalid_input'))
    return words

def choose_random_category():
    """Choose a random category and return a word from that category."""
    category = random.choice(list(word_categories.keys()))
    word = random.choice(word_categories[category])
    return word

def display_words(words, guessed_letters):
    """Display the current status of words to be guessed."""
    display = []
    for word in words:
        display.append(" ".join(letter if letter in guessed_letters else "_" for letter in word))
    return " / ".join(display)

def display_guessed_letters(guessed_letters):
    """Display the letters that have been guessed so far."""
    return "Guessed letters: " + ", ".join(guessed_letters)

def play_hangman(words):
    """Start and play the Hangman game."""
    guessed_letters = []
    tries = 10

    print(get_translation('play_hangman'))
    while tries > 0:
        print(display_hangman(tries))
        print(display_words(words, guessed_letters))
        print(display_guessed_letters(guessed_letters))

        guess = input("\nPlayer 2, please guess a letter or the whole phrase: ").lower()

        if guess == 'exit':
            break

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(get_translation('already_guessed_letter').format(guess))
            elif any(guess in word for word in words):
                print(get_translation('good_job_letter').format(guess))
                guessed_letters.append(guess)
            else:
                print(get_translation('not_in_word').format(guess))
                guessed_letters.append(guess)
                tries -= 1
        elif len(guess) == len("".join(words)) and guess.isalpha():
            if guess == "".join(words):
                print(get_translation('congrats_word').format(" ".join(words)))
                guessed_letters.extend(list(set("".join(words)) - set(guessed_letters)))
                break
            else:
                print(get_translation('invalid_guess'))
                tries -= 1
        else:
            print(get_translation('invalid_guess'))
            tries -= 1

        print("\n")

    if tries == 0:
        print(get_translation('sorry_lose').format(" ".join(words)))

# Main dashboard function
def dashboard():
    """Display the main menu dashboard and handle user input."""
    global current_language
    while True:
        print(get_translation('welcome'))
        print(get_translation('menu'))
        print(get_translation('start_game'))
        print(get_translation('instructions'))
        print(get_translation('switch_language'))
        print(get_translation('random_category'))
        print(get_translation('exit'))
        choice = input(get_translation('select_option'))

        if choice == '1':
            words = get_words()
            if words:
                play_hangman(words)
        elif choice == '2':
            print(get_translation('instructions_en') if current_language == translations_en else get_translation('instructions_cy'))
        elif choice == '3':
            current_language = translations_cy if current_language == translations_en else translations_en
        elif choice == '4':
            word = choose_random_category()
            play_hangman([word])
        elif choice == '5':
            print(get_translation('exit_message'))
            break
        else:
            print(get_translation('invalid_input'))

# Start the dashboard
dashboard()
