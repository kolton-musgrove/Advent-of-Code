# Most of the logic for the problems in day 3 can be contained in one function.
# The only logic in the actual function calls is which paths are follwed be each problem

def puzzle1():
    print("\n Puzzle 1: \n")
    print(pathSolve(3, 1))

def puzzle2():
    print("\n Puzzle 1: \n")

    answer = (pathSolve(1, 1) * pathSolve(3, 1) * pathSolve(5, 1) * pathSolve(7, 1) * pathSolve(1, 2))
    print(answer)


def pathSolve(right, down):
    with open("day 3/input.txt") as terrain:

        answer = 0
        # variable to hold the current position on the horizontal axis
        rightIncrement = 0
        # variable to hold the current position on the vertical axis
        downIncrment = 0

        for line in terrain:
            # we only want to check the lines that match the 'down' input given to the function
            if downIncrment % down == 0:
                # now we have to find if the horizontal position matches the 'right' input given to the function
                # also, since we only have 31 characters of horizontal space, we need to use the modulus operator to find our location relative to the first 31 characters
                if line[(rightIncrement * right) % 31] == "#":
                    answer += 1
                rightIncrement += 1
            downIncrment += 1
        
        return answer

puzzle1()
puzzle2()