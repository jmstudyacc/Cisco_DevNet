There are 5 prevailing principles of Test-Driven Development (aka Test-First Development)
The basic pattern of this process is the concept of repeating steps

1 - Create a new test, existing it to other tests if they exist:
    This will help you capture requirements for your code ahead of writing

2 - Runs tests to see if any fail for unexpected reasons:
    If this happens, correct the tests. Expected failures are permitted here, for instance, a test failing as a function is not yet created

3 - Write application code that passes the new test:
    The rule here is to add nothing more to the application beyond what is required to pass the test

4 - Run tests to see if any fail
    If there are failures you need to correct the application code and try again

5 - Refactor and improve application code
    Each time this step is taken, re-run the tests and correct application if you encounter any failures


By taking this approach the test evolves organically with the application code. This gives you very high test coverage on the code and provides
testing and application code that are correct together at any given stopping-point. This process necessitates a number of things:

- Obliges devs to consistently think about the requirements and how to capture them in tests
- Helps clarify and constrain what the code needs to do, as it just needs to pass the tests, with speeds development and encourages simplicity + good use of design patterns
- Mandates the creation of highly testable code - this will, as an example, produce code that can be tested in isolation and in any order!