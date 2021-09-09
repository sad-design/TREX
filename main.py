import phonenumbers
from phonenumbers import carrier, geocoder, timezone


mobileNo = input("Enter the mobile number with country code : ")
mobileNo = phonenumbers.parse(mobileNo)

#time zone of the number
print(timezone.time_zones_for_number(mobileNo))

#carrier of the number
print(carrier.name_for_number(mobileNo, "en"))

#region of the number
print(geocoder.description_for_number(mobileNo, "en"))

#validationg a phone number
print("valind Moblie Number : ",phonenumbers.is_valid_number(mobileNo))

#checking possibility of a number
print("Checking possibilty of Number : ", phonenumbers.is_possible_number(mobileNo))

