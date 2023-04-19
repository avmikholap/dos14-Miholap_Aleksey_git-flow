# использовал библиотеку для работы с ОС
import os

# сразу на экран вывел текущее значение переменной SHELL
print("The value of SHELL is: ", os.environ["SHELL"])
# переменной shell присвоил функцию os.getenv, через которую получаю текущее значение переменной среды SHELL
shell = os.getenv("SHELL")
# если значение совпадает, то  выведет соответсвующее сообщение.
if shell == "/bin/bash":
    print("Greeting bash")
# если значение не совпало, то выведет приветствие  с полученным значением переменной среды SHELL
else:
    print(f"HELLO {shell}")
