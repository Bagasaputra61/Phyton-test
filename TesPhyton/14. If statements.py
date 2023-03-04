#if statements
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("you are a short male")
elif not is_male and (is_tall):
    print("you are not a male but are tall")   
else:
    print("You not a male and not tall")