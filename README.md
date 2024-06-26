This Flask application serves as an API that provides endpoints to retrieve various types of numbers and calculate their average within a sliding window. Here's a breakdown of the code:

Imports: The code imports necessary modules from Flask (Flask for creating the application and jsonify for JSON responses) and collections for using deque to implement a fixed-size window for storing numbers.
Constants: Constants like WINDOW_SIZE, TEST_SERVER_BASE_URL, and TIMEOUT are defined. WINDOW_SIZE determines the size of the sliding window for storing numbers. TEST_SERVER_BASE_URL holds the base URL of the test server where additional numbers can be fetched. TIMEOUT specifies the timeout duration for requests made to the test server.
Data Storage: A deque named number_window is initialized to store numbers within the sliding window.
Helper Functions:
is_prime(n): This function checks if a given number is prime.
fibonacci(n): This function generates the first n Fibonacci numbers.
calculate_average(numbers): This function calculates the average of a list of numbers.
Endpoint Definitions:
/e: This endpoint returns a list of even numbers within the range [2, 2 + WINDOW_SIZE * 2) where WINDOW_SIZE determines the count of numbers.
/p: This endpoint returns a list of prime numbers within the range [2, 2 + WINDOW_SIZE * 10) where WINDOW_SIZE determines the count of numbers.
/fibo/<int:n>: This endpoint returns the first n Fibonacci numbers.
/numbers: This endpoint returns the numbers stored in the sliding window along with the average, current state of the window, and previous state (empty in this case).
Main Execution Block: The Flask application is started if the script is executed directly.

![op1](https://github.com/kowshikpeddireddy/VTU19226/assets/127022987/51640830-36ca-456f-a25f-b7f52b59ac76)
![op2](https://github.com/kowshikpeddireddy/VTU19226/assets/127022987/76fd905f-2617-4ff5-b80e-b21fbe399f81)
![op3](https://github.com/kowshikpeddireddy/VTU19226/assets/127022987/b4c695c3-5bb8-4ffb-880b-6e2cf2faf10f)
![op4](https://github.com/kowshikpeddireddy/VTU19226/assets/127022987/abbb778b-9160-49a8-9b14-16f01f12865c)

