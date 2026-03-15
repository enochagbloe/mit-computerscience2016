# word = input("Enter a word: ")
# times = int(input("Enter a number: "))

# count = 0
# for w in word:
#     if w == "e":
#         count += 1
#         print("Found an e!")
#     print(w)
# print(f"Total e's found: {count}")

# for i in range(times):
#     print(f"{word}!!!")



# s = "abca"
# seen = ""
# count = 0
# for char in s:
#     if char not in seen:
#         seen += char
#         count += 1
# print(f"Total characters found: {count}") 

x = int(input("Enter a number: "))
guess = 0
while guess ** 2 < x:
    guess += 1
print(f"The square root of {x} is approximately {guess}")