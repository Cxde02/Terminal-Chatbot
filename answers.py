import datetime

#Q and A for hellos
helloWords = ['hi', 'hey', 'hello', 'sup', 'bonjour', 'salut', 'greetings', 'up', 'howdy', 'yo!', 'hi there', 'what\'s up', 'hiya',]
helloWordsAnswers = [
    'Sup! Ask me anything',
    'Hello! How can I assist you?',
    'Hey there! Feel free to chat with me',
    'Greetings! How can I help you today?',
    'Up and ready! What can I do for you?',
    'Howdy! What\'s on your mind?',
    'Yo! What\'s going on?',
    'Hi there! How can I assist you?',
    'What\'s up? Ready to chat!',
    'Hiya! How are you doing?',
    'Good day! How may I help you?',
    'Hello there! How can I assist you today?',
    'Aloha! What brings you here?',
]

# Q and A for inquiring about the time
timeQuestions = ['What time is it?', 'Can you tell me the time?', 'Do you know what time it is?', 'What\'s the current time?', 'time']
current_time = datetime.datetime.now().strftime('%H:%M')  # Get current time in HH:MM format
timeAnswers = [
    f'It is currently {current_time}.',
    f'The time is {current_time}.',
    f'As of now, it\'s {current_time}.',
    f'The current time is {current_time}.',
]

# Q and A for inquiring about the date
dateQuestions = ['What is today\'s date?', 'Can you tell me the date?', 'Do you know what date it is today?', 'What\'s the current date?', 'date']
current_date = datetime.datetime.now().strftime('%d %B %Y')  # Get current date in DD Month YYYY format
dateAnswers = [
    f'Today\'s date is {current_date}.',
    f'The date is {current_date}.',
    f'As of now, it\'s {current_date}.',
    f'The current date is {current_date}.',
    f'It\'s {current_date}.',
]

# Q and A related to technology
techQuestions = [
    'What is artificial intelligence?',
    'Explain the concept of AI.',
    'How does artificial intelligence work?',
    'What are the capabilities of artificial intelligence?',
    'Give me an overview of AI.',
    'In simple terms, what is AI?',
    'What tasks can artificial intelligence perform?',
    'Describe the function of artificial intelligence.',
    'What does artificial intelligence enable computers to do?',
    'Can you provide a definition of AI?',
    'ai',
    'artificial intelligence',
]

techAnswers = [
    'Artificial intelligence is the development of algorithms that enable machines to perform tasks that typically require human intelligence.',
    'AI refers to the creation of computer programs that can think and learn like humans, allowing them to perform tasks intelligently.',
    'The functionality of artificial intelligence is based on algorithms and computational models that simulate human cognitive processes, such as learning, problem-solving, and decision-making.',
    'Artificial intelligence can analyze data, recognize patterns, make predictions, solve complex problems, and even interact with users in a natural language.',
    'In essence, AI is about creating systems that can mimic and replicate human-like intelligence for various applications.',
    'AI involves the development of algorithms that empower machines to imitate human cognitive functions, such as learning, reasoning, and problem-solving.',
    'Artificial intelligence is capable of performing tasks like data analysis, pattern recognition, decision-making, and language understanding.',
    'The function of artificial intelligence is to enable computers to simulate human intelligence, performing tasks that typically require human reasoning and learning.',
    'Artificial intelligence allows computers to perform tasks such as understanding natural language, recognizing images, and making decisions based on data.',
    'In simple terms, artificial intelligence involves creating computer systems that can perform tasks intelligently, mimicking human-like cognitive abilities.'
]


programmingQuestions = [
'What is programming?',
'Explain the concept of coding.',
'How does programming work?',
'What are the capabilities of programming?',
'Give me an overview of programming.',
'In simple terms, what is coding?',
'What tasks can programming perform?',
'Describe the function of programming.',
'What does programming enable computers to do?',
'Can you provide a definition of programming?',
'coding',
'programming',
]

programmingAnswers = [
'Programming is the process of designing and building executable computer code to accomplish a specific task or set of tasks.',
'Coding refers to the act of writing and organizing code that instructs a computer on how to perform a particular task or set of tasks.',
'Programming involves writing instructions in a programming language that a computer can understand and execute to perform desired functions.',
'The capabilities of programming include automation of tasks, data manipulation, creating software applications, and controlling hardware devices.',
'In essence, programming is about creating a set of instructions that computers can follow to perform specific operations or solve problems.',
'Coding, in simple terms, is the act of creating a set of instructions (code) that a computer can understand and execute to perform a desired task.',
'Programming can perform tasks such as data manipulation, creating software applications, automating repetitive processes, and controlling hardware.',
'The function of programming is to enable computers to execute specific tasks by providing them with a set of instructions written in a programming language.',
'Programming enables computers to perform a wide range of tasks, from simple calculations to complex operations, by providing them with a set of instructions to follow.',
'In simple terms, programming involves creating a sequence of instructions that a computer can understand and execute to achieve a desired outcome.'
]

# Jokes Q and A
jokesQuestions = [
    'Tell me a joke.',
    'Give me a funny joke.',
    'Can you make me laugh?',
    'Share a humorous story.',
    'Tell a joke about technology.',
    'joke',
    'humor',
    'laugh',
    'funny',
]

jokesAnswers = [
    'Sure, here\'s a joke for you: Why don\'t scientists trust atoms? Because they make up everything!',
    'Why did the computer go to therapy? It had too many bytes of emotional baggage!',
    'I told my computer I needed a break, and now it won\'t stop sending me vacation ads.',
    'Why did the robot go on a diet? It had too many bytes!',
    'Why was the math book sad? Because it had too many problems.',
    'Why don\'t programmers like nature? It has too many bugs!',
    'What do you call fake spaghetti? An impasta!',
    'Why did the scarecrow win an award? Because he was outstanding in his field!',
    'Why couldn\'t the bicycle stand up by itself? Because it was two-tired!',
    'What did one hat say to the other? Stay here, I\'m going on ahead!',
    'How does a penguin build its house? Igloos it together!',
    'Why don\'t skeletons fight each other? They don\'t have the guts!',
    'What do you get when you cross a snowman and a vampire? Frostbite!',
    'Why don\'t scientists trust genetics? Because it\'s all in the genes!',
    'I only know 25 letters of the alphabet. I don\'t know y!',
    'Why did the tomato turn red? Because it saw the salad dressing!',
    'How do you organize a space party? You planet!',
    'Why did the coffee file a police report? It got mugged!',
    'What do you call a fish wearing a crown? A kingfish!',
    'Why don\'t skeletons fight each other? They don\'t have the guts!'
]

# Origin Q and A
originQuestions = [
    'Who made you?',
    'What is your origin?',
    'Who is your creator?',
    'Tell me about the person who developed you.',
    'Who programmed you?',
    'origin',
    'creator',
    'developed',
    'master',
    'created',
    'made',
]

originAnswers = [
    'Ahmad Raza Ruhomaun is the person behind my creation.',
    'I was developed by Ahmad Raza Ruhomaun.',
    'My creator is Ahmad Raza Ruhomaun.',
    'Ahmad Raza Ruhomaun is the one who programmed me.',
    'I am a creation of Ahmad Raza Ruhomaun.',
    'Ahmad Raza Ruhomaun is the individual responsible for bringing me into existence.'
]

# Fun Fact Q and A
funFactQuestions = [
    'Tell me a fun fact.',
    'Give me an interesting fact.',
    'Share a random piece of information.',
    'Tell me something cool.',
    'fun fact',
    'interesting fact',
]

funFactAnswers = [
    'Sure, here\'s a fun fact: Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!',
    'Did you know that a group of flamingos is called a "flamboyance"?',
    'Here\'s an interesting fact: The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes!',
    'Did you know that honeybees can recognize human faces?',
    'Here\'s a cool fact: Bananas are berries, but strawberries aren\'t!',
    'Fun fact: The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion of the iron!',
    'Did you know that a day on Venus (one full rotation on its axis) is longer than a year on Venus (one orbit around the sun)?',
    'Here\'s an interesting fact: The world\'s largest desert is not the Sahara; it\'s Antarctica!',
    'Fun fact: Cows have best friends and can become stressed when they are separated from them.',
    'Did you know that the Great Wall of China is not visible from the moon with the naked eye?',
    'Here\'s a cool fact: A group of owls is called a parliament!',
    'Fun fact: Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!'
]

#Q and A for movies/shows
movieQuestions = [
    'Can you recommend a movie?',
    'What should I watch tonight?',
    'Suggest a good movie',
    'I need a movie recommendation',
    'What movie should I watch?',
    'movie',
    'show',
]

movieAnswers = [
    'Sure, how about watching "The Shawshank Redemption"? It\'s a classic!',
    'For a great movie night, I recommend "Inception." The mind-bending plot is a must-watch!',
    'If you enjoy animated films, "Toy Story" is a fantastic choice with humor and heart.',
    'If you enjoy animated films, "Cars 1/2/3" is a fantastic choice with race and humor',
    'How about a thrilling experience with "The Dark Knight"? It\'s a masterpiece by Christopher Nolan.',
    'If you\'re in the mood for a feel-good movie, "Forrest Gump" is a timeless classic.',
    'For a mind-twisting series, check out "Stranger Things" on Netflix.',
    'If you love horror, "The Last Of Us" is an epic TV show with intricate plots and characters.',
    'Consider watching "The Godfather" for a cinematic masterpiece with a gripping storyline.',
    'Looking for a comedy? "The Grand Budapest Hotel" is a delightful and quirky choice.',
    'If you\'re into science fiction, "Blade Runner 2049" offers stunning visuals and a compelling story.',
    'For a mix of action and humor, "The Avengers" is a great superhero ensemble film.',
    'For a mix of action and humor, "The Amazing Spider-man" is a great superhero ensemble film.',
    'Explore the world of magic and adventure with the "Harry Potter" series.',
    'For a captivating documentary, "Planet Earth II" showcases stunning visuals of the natural world.',
    'Get ready for a rollercoaster of emotions with "The Pursuit of Happyness."',
    'If you\'re a fan of drama, "Breaking Bad" is a gripping TV series with intense character development.',
    'For a classic romantic comedy, "When Harry Met Sally" is a delightful choice.',
    'Experience the magic of animation with "Spirited Away" from Studio Ghibli.',
    'Unleash your inner detective with the mystery series "Sherlock."',
    'If you\'re into mind-bending plots, "Black Mirror" is a thought-provoking anthology series.',
    'For a heartwarming animated film, "Up" is a beautiful adventure filled with emotions.'
]






