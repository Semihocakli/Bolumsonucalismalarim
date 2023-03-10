# Input ile first_name bilgisini al
first_name = input("Please enter your first name: ")
# input ile last_name bilgisini al
last_name = input("Please enter your last name: ")
# input ile year_of_birth bilgisini al
year_of_birth = input("Please enter your year of birth: ")
# first_name ve last_name bilgilerinin karakter sayini yaz
print("The length of your first name is:", len(first_name))
print("The length of your last name is:", len(last_name))
# fString ile kullanicinin adinin ilk harfi ve buyuk olacak sekilde full_name yazdir
full_name = f"{first_name.capitalize()} {last_name}"
print("Your full name is:", full_name)
# yasini ve gelecek seneki yasini fString ile yazdir
age = 2023 - int(year_of_birth)
print(f"You are currently {age} years old and you will be {age+1} years old next year.")
# 18 yasindan buyukse True olacak sekilde bilgisini don
is_18_or_older = age >= 18
print("Is your age greater than 18?", is_18_or_older)
