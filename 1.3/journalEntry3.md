## Exercise 1.3: Operators & Functions in Python

### Learning Goals

- Implement conditional statements in Python to determine program flow
- Use loops to reduce time and effort in Python programming
- Write functions to organize Python code

### Reflection Questions

1. In this Exercise, you learned how to use if-elif-else statements to run different tasks based on conditions that you define. Now practice that skill by writing a script for a simple travel app using an if-elif-else statement for the following situation:

- The script should ask the user where they want to travel.
- The user’s input should be checked for 3 different travel destinations that you define.
- If the user’s input is one of those 3 destinations, the following statement should be printed: “Enjoy your stay in **\_\_**!”
- If the user’s input is something other than the defined destinations, the following statement should be printed: “Oops, that destination is not currently available.”

```
travel = input("Where would you like to travel? ")
if travel == "Tokyo":
    print("Enjoy your stay in Tokyo!")
elif travel == "Oslo":
    print("Enjoy your stay in Oslo!")
elif travel == "Monterrey":
    print("Enjoy your stay in Monterrey!")
else:
    print("Oops, that destination is not currently available.")
```

2. Imagine you’re at a job interview for a Python developer role. The interviewer says “Explain logical operators in Python”. Draft how you would respond.

- Logical operators are used to check multiple condtions at the same time, for example if you wanted to check if the length and width of a rug would fit your space. The logical operators check if each condition is true or false.

3. What are functions in Python? When and why are they useful?

- Functions are sets of instructions that process code to achieve certain things. They are useful for saving time because you can create your own function and reuse it throughout your code when necessary.

4. In the section for Exercise 1 in this Learning Journal, you were asked in question 3 to set some goals for yourself while you complete this course. In preparation for your next mentor call, make some notes on how you’ve progressed towards your goals so far.

- So far I've learned how to organize data, create loops & functions, and make more use of the iPython shell.
- I am starting to feel more comfortable with Python scripts (at least with the material I have gone over so far.)
- I am still getting used to backend vs frontend and not being able to see the work on a browser, but using the shell has been a good way to visualize it all.
