import requests

BASE_URL = "http://localhost:5000/number/"

#отправка GET запроса
def send_get_request():
    response = requests.get(BASE_URL, params={'param': 2.0})
    response.raise_for_status()
    return response.json()

#отправка POST запроса
def send_post_request():
    data = {'jsonParam': 3.0}
    response = requests.post(BASE_URL, json=data)
    response.raise_for_status()
    return response.json()

#отправка DELETE запроса
def send_delete_request():
    response = requests.delete(BASE_URL)
    response.raise_for_status()
    return response.json()


def calculate(operand1, operation, operand2):
    if operation == "+":
        return operand1 + operand2
    elif operation == "-":
        return operand1 - operand2
    elif operation == "*":
        return operand1 * operand2
    elif operation == "/":
        if operand2 == 0:
            raise ValueError("Деление на ноль!")
        return operand1 / operand2
    else:
        raise ValueError(f"Неизвестная операция: {operation}")


try:
    #отправка запросов
    get_data = send_get_request()
    post_data = send_post_request()
    delete_data = send_delete_request()

    print(f"GET response: {get_data}")
    print(f"POST response: {post_data}")
    print(f"DELETE response: {delete_data}")

    #инициализирация результата с результатом GET запроса
    cumulative_result = get_data['result']
    print(f"Начальный результат: {cumulative_result}")

    #POST запрос
    post_operation = post_data['operation']
    post_random_number = post_data['random_number'] 
    cumulative_result = calculate(cumulative_result, post_operation, post_random_number)
    print(f"После POST ({post_operation} {post_random_number}): {cumulative_result}")

    #DELETE запрос
    delete_operation = delete_data['operation']
    delete_random_number = delete_data['random_number'] 
    cumulative_result = calculate(cumulative_result, delete_operation, delete_random_number)
    print(f"После DELETE ({delete_operation} {delete_random_number}): {cumulative_result}")

    
    final_result = int(cumulative_result)
    print(f"Окончательный результат (int): {final_result}")

except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")
except KeyError as e:
    print(f"Ошибка ключа: {e}")
except ValueError as e:
    print(f"Ошибка значения: {e}")
except Exception as e:
    print(f"Общая ошибка: {e}")