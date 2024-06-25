def factorial(n: int) -> int:
  
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def list_factorial(numbers: list[int]) -> list[int]:
 
    return [factorial(n) for n in numbers]

