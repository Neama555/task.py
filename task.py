temperature=40
if temperature >= 30:
    print("It's a hot day. Stay hydrated!")
elif 20 <= temperature <= 29:
    print("It's a warm day. Enjoy the weather!")
elif 10 <= temperature <= 19:
    print("It's a cool day. Wear a jacket!")
else:
    print("It's a cold day. Stay warm!")
numbers=list(range(1,21))
print(list, numbers)
divisible_by_3= []
for num in numbers:
    if num % 3 == 0:
        divisible_by_3.append(num)
print("numbers divisible by 3:",divisible_by_3)