from flask import Flask

app = Flask(__name__)

def fibonacci(n):
    a, b = 0, 1
    series = []
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_palindrome(text):
    return text == text[::-1]

def armstrong(num):
    total = 0
    temp = num
    digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == num

@app.route('/')
def home():
    result = ""

    result += "Fibonacci Series:<br>"
    fib = fibonacci(10)
    result += str(fib) + "<br><br>"

    number = 17
    result += f"Prime Check ({number}): {is_prime(number)}<br><br>"

    text = "madam"
    result += f"Palindrome Check ({text}): {is_palindrome(text)}<br><br>"

    arm = 153
    result += f"Armstrong Check ({arm}): {armstrong(arm)}"

    return result

app.run(host='0.0.0.0', port=10000)