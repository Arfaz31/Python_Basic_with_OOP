dictt_1={'rahim':10,'karim':20,'jony':30}
dictt_2={'rahim':10,'karim':2,'sardar':40}

result = dictt_1

for key, value in dictt_2.items():
    result[key] = result.get(key, 0) + value

print(result)


# result.get('rahim', 0)
#  এখানে rahim নামের key result এ আছে → তাই output হবে: 10

# result.get('sardar', 0)
# sardar এই key result এ নেই → তাই output হবে: 0 (default value)