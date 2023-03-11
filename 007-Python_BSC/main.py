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



# Kullanıcı küpün kenar uzunluğunu (cm olarak alın) ve işlem numarasını girsin
# İşlem No 1: Küpün kenarlarının toplamı (cm olarak)
# İşlem No 2: Küpün yüzey alanının toplamı (cm^2 olarak)
# İşlem No 3: Küpün hacmi cm^3 olarak

a = int(input("Lütfen küpün bir kenar uzunluğunu cm cinsinden giriniz: "))
secim = int(input("Lütfen işlem tipini seçiniz: \n1- Küpün kenar uzunluklarının toplamı\n2- Küpün yüzey alanlarının toplamı\n3- Küpün hacmi\n"))

if secim == 1:
    sonuc = 12 * a
    print(f"Küpün kenar uzunluklarının toplamı: {sonuc} cm'dir.")
elif secim == 2:
    sonuc = 6 * a * a
    print(f"Küpün yüzey toplamı: {sonuc} cm^2'dir.")
elif secim == 3:
    sonuc = a * a * a
    print(f"Küpün hacmi: {sonuc} cm^3'dir.")
else:
    print("Lütfen 1-3 arasında seçim yapınız.")

