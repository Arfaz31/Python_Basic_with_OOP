dictt_1={'rahim':10,'karim':20,'jony':30}
dictt_2={'rahim':10,'karim':2,'sardar':40}

result = dictt_1

for key, value in dictt_2.items():
    result[key] = result.get(key, 0) + value

print(result)
