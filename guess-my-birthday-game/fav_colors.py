#With renamed parameter and variables
def get_color(fav_number):
    num = str(fav_number +1)
    prompt = "What is your #" + num + "fav color? "
    answer = input(prompt)
    return answer

#With renamed variables
def get_num_colors():
    response = input("How many fav colors do you have? ")
    response_num = int(response)
    return response_num

print("Hi, I'd like to ask you about your fav colors.")
num_colors = get_num_colors()
print("Thanks! I will now ask you for each of those. ")
favorite_colors = []

for color_number in range(num_colors):
    color = get_color(color_number)
    favorite_colors.append(color)

sorted_colors = sorted(favorite_colors)
print("Thank you! I have your fav colors as:")
for color in sorted_colors:
    print("  ", color)
