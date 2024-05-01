import requests
from flask import Flask, jsonify

app = Flask(__name__)

numbers = []
window_size = 10

def fetch_numbers(qualifier):
    headers = {
        "Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzE0NTQ2MjgwLCJpYXQiOjE3MTQ1NDU5ODAsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjZjZTZkN2U2LWQwZTctNDUxMy1hODI5LTJhYjMzOGU2YmFmNCIsInN1YiI6InZ0dTE5MjI2QHZlbHRlY2guZWR1LmluIn0sImNvbXBhbnlOYW1lIjoiZ29NYXJ0IiwiY2xpZW50SUQiOiI2Y2U2ZDdlNi1kMGU3LTQ1MTMtYTgyOS0yYWIzMzhlNmJhZjQiLCJjbGllbnRTZWNyZXQiOiJlYVhkR3hUQlh1THVkeVVmIiwib3duZXJOYW1lIjoicGVkZGlyZWRkeSBrb3dzaGlrIGt1bWFyIHJlZGR5Iiwib3duZXJFbWFpbCI6InZ0dTE5MjI2QHZlbHRlY2guZWR1LmluIiwicm9sbE5vIjoidnR1MTkyMjYifQ.lxE5hC09yLtwAsVs_zqlIWDG7B-lq-vM1tLlJBkEIcc"
    }
    if qualifier == 'p':
        url = "http://20.244.56.144/test/primes"
    elif qualifier == 'f':
        url = "http://20.244.56.144/test/fibo"
    elif qualifier == 'e':
        url = "http://20.244.56.144/test/even"
    elif qualifier == 'r':
        url = "http://20.244.56.144/test/random"
    else:
        return []

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["numbers"]
    else:
        return []

def calculate_average():
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

@app.route('/numbers/<qualifier>')
def process_numbers(qualifier):
    global numbers

    new_numbers = fetch_numbers(qualifier)

    numbers = list(set(numbers + new_numbers))

    if len(numbers) > window_size:
        numbers = numbers[-window_size:]

    avg = calculate_average()

    response = {
        "numbers": new_numbers,
        "windowPrevState": numbers[:-len(new_numbers)],
        "windowCurrState": numbers,
        "avg": avg
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876)
