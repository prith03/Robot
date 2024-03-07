import math

# Function to calculate the distance from the origin to the final destination
def calculate_distance_from_origin(horizontal_steps, vertical_steps):
    origin = [0, 0]
    distance = math.sqrt(((origin[0] - horizontal_steps) ** 2) + ((origin[1] - vertical_steps) ** 2))
    return distance

# Set vertical and horizontal step counts to 0
verticalStepsCount = 0
horizontalStepsCount = 0

# Enter a trace (The trace should be in this format: DIRECTION QUANTITY (ex: LEFT 3)
while True:
    user = input("Enter a trace: ")
    if not user:
        break

    # Split string so that the first string is the direction and second string is number of steps
    position = user.split(" ")
    direction = position[0]
    steps = int(position[1])

    # If direction is up, then increase the number of steps
    if(direction == "UP"):
        verticalStepsCount += steps

    # If direction is down, then decrease the number of steps
    elif(direction == "DOWN"):
        verticalStepsCount -= steps

    # If direction is right, then increase the number of steps
    elif(direction == "RIGHT"):
        horizontalStepsCount += steps

    # If direction is left, then decrease the number of steps
    elif(direction == "LEFT"):
        horizontalStepsCount -= steps

# Print out the final trace, calculate the total distance, and print out the distance
print("(" + str(horizontalStepsCount) + ", " + str(verticalStepsCount) + ")")
distance = calculate_distance_from_origin(horizontalStepsCount, verticalStepsCount)
print(distance)
