def myName(name, age , gender):
    print(f"Hello, my name is {name}")
    print(f"I'am {age} years old")
    if(gender == 'male'):
       return print(f"I'am male")
    elif(gender == 'female'):
       return print("I'am female ")
    else:
       return None
        

myName("furkan", 23, 'male')