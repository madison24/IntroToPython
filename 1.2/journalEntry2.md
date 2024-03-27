## Exercise 1.2: Data Types in Python

### Learning Goals

- Explain variables and data types in Python
- Summarize the use of objects in Python
- Create a data structure for your Recipe app

### Reflection Questions

1. Imagine you’re having a conversation with a future colleague about whether to use the iPython Shell instead of Python’s default shell. What reasons would you give to explain the benefits of using the iPython Shell over the default one?

- I would say that iPython is just a better version of the default shell. It runs your python code like the default but includes a lot of built in toolkit options to enhance the experience.

2. Python has a host of different data types that allow you to store and organize information. List 4 examples of data types that Python recognizes, briefly define them, and indicate whether they are scalar or non-scalar.

- Bool: is a data type that stores two different values TRUE or FALSE, and is scalar.
- Int: is a data type that represents integers either negative or non-negative (-1,1,0,1990000, and so on), and is scalar.
- Tuples: are linear arrays that can store multiple values of any type(1,"frog",76.7, and so on), and are non-scalar.
- Lists: are like tuples but they differ in that they are "mutable" which means any of the internal elements can be modified or deleted, and are non-scalar.

3. A frequent question at job interviews for Python developers is: what is the difference between lists and tuples in Python? Write down how you would respond.

- As mentioned above, lists are mutable while tuples are not. Meaning, where elements in lists can be modified or deleted, this is not the case for tuples.

4. In the task for this Exercise, you decided what you thought was the most suitable data structure for storing all the information for a recipe. Now, imagine you’re creating a language-learning app that helps users memorize vocabulary through flashcards. Users can input vocabulary words, definitions, and their category (noun, verb, etc.) into the flashcards. They can then quiz themselves by flipping through the flashcards. Think about the necessary data types and what would be the most suitable data structure for this language-learning app. Between tuples, lists, and dictionaries, which would you choose? Think about their respective advantages and limitations, and where flexibility might be useful if you were to continue developing the language-learning app beyond vocabulary memorization.

- I would choose a dictionary for each individual flash card so I could utilize the key-value pairs with the vocab word, definition, and category. I would also use a list for the library of ALL the vocab words because of its flexibility compared to tuples in the modification of data.
