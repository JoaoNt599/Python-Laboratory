# Recursion


## Recursion is a programming concept where a function calls itself in order to solve a problem. Instead of using iteration (loops) to repeatedly execute a set of statements, a recursive function breaks down a problem into smaller, more manageable subproblems and solves each subproblem by invoking the same function. The process continues until a base case is reached, at which point the function returns a result without making further recursive calls.

### Key components of a recursive function include:

## Base Case: 

    This is the condition that determines when the recursion should stop. It represents the simplest form of the problem that can be directly solved without further recursion.

## Recursive Case: 

    This is where the function calls itself with a modified version of the original problem. The goal is to reduce the problem toward the base case.

### A classic example of recursion is the computation of the factorial of a number. The factorial of a non-negative integer nn, denoted as n!n!, is the product of all positive integers up to nn.