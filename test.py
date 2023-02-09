str = input("Enter the word: ")
result = ""
for i in range(len(str)):
			
			result += str[len(str)-i-1]

print(result)