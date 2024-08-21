# Use your knowledge of Python lists to create a master list of each painting, its date, and its audio tour ID.
# Create lists
names = ["The Two Fridas", "My Dress Hangs Here", "Tree of Hope", "Self Portrait With Monkeys"]
dates = [1939, 1933, 1946, 1940]

# Zip together both lists & resave
paintings = list(zip(names, dates))
print(paintings)

# Last minute painting additions
names2 = ["The Broken Column", "The Wounded Deer", "Me and My Doll"]
dates2 = [1944, 1946, 1937]
paintings2 = list(zip(names2, dates2))

# For loop to append
for element in paintings2:
  paintings.append(element)
print(paintings)

print("There are now " + str(len(paintings)) + " paintings.")

# Using range to create a list
audio_tour_number = list(range(1, 8))

master_list = list(zip(paintings, audio_tour_number))
print(master_list)
