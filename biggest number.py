biggest= None
first = True

while True:
    number = input("Please enter your number(enter end to end):")
    
    if number.lower() == 'end':
        break
    
    adad = float(number)
    
    if first:
        biggest = adad
        first = False
    elif adad > biggest:
        biggest = adad

if biggest is not None:
    print("Biggest number:" , biggest)
else:
    print("ERROR")