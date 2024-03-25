## Exercise 1.1: Getting Started with Python

### Learning Goals

- Summarize the uses and benefits of Python for web development
- Prepare your developer environment for programming with Python

### Reflection Questions

1. In your own words, what is the difference between frontend and backend web development? If you were hired to work on backend programming for a web application, what kinds of operations would you be working on?

- Basically frontend is what users see and possibily interact with (buttons, forms, etc) and backend is what is stored in the background (servers, API's, etc).
  As a backend developer you could be making an API that has any kind information you want to store, databases, authentication, and more.

2. Imagine you’re working as a full-stack developer in the near future. Your team is asking for your advice on whether to use JavaScript or Python for a project, and you think Python would be the better choice. How would you explain the similarities and differences between the two languages to your team? Drawing from what you learned in this Exercise, what reasons would you give to convince your team that Python is the better option?

- I would start by telling my team how Python is a language thats known to be easy to learn and understand which is a major perk. A big feature of Python is its readability, so anyone with some kind of basic coding experience can glance at a piece of code and understand whats actually happening.
  Like JavaScript, Python uses easy to understand keywords like import, return, etc. They also both share a dynamic typing approach.
  Another feature Python has is the number of open-source and proprietary packages available for whatever project you're working on that can be easily imported.

3. Now that you’ve had an introduction to Python, write down 3 goals you have for yourself and your learning during this Achievement. You can reflect on the following questions if it helps you. What do you want to learn about Python? What do you want to get out of this Achievement? Where or what do you see yourself working on after you complete this Achievement?

- I would like to learn about more packages I can import and use on Python projects and how to utilize them to my advantage.
- I want to be able to add Python to my developer toolkit and become a stronger backend developer.
- In the future I could see myself working on a new database or API for a project of my own, or even something to help a friend/colleague.

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
