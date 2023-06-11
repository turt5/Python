text="Jon loves programming"

sliced_string=text.split(" ")

user=sliced_string[0]
adj=sliced_string[1]
v=sliced_string[2]

print(user)
print(adj)
print(v)


username=text[:3]
print(username)
print(text[10:])

print(user[::-1]) #reverse string

slice=slice(12,-4)
website1="https://www.google.com"
website2="https://www.facebook.com"
print(website1[slice])
print(website2[slice])