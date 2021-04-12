"""


input: the test score
indicate a iterator and accumlator and set it to zero
loop through the list test scores
add all the test scores
increment the counter by 1
once the loop ends, there are no ore scores to add
output: print the average of the class scores
divide the accumulated (sum) by counter
display the output to the user
output: print the average of the class scores
"""


"""
scores
iterator, accumulator = 0 
loop through scores
    accumulator = accumulator + scores
    iterator = iteratior + 1
output = accumulator / total score
print output
"""
"""
scores = [100, 80, 90, 70, 50, 95] #Input
iterator = 0
accumulator = 0
student_count = len(scores)

print("Length is:", len(scores))


#while there are more scores: 
while iterator < len(scores):
    #print("within while loop iterator: ", iterator)
    print(f"item at index {iterator} is: ", scores[iterator])
    accumulator = accumulator + scores[iterator]
    iterator = iterator + 1

print("sum is:", accumulator)
average = accumulator / student_count
print("The Average of total scoresin the class is", average)
return average
"""


def calculate_average(scores):
        iterator = 0
        accumulator = 0
        student_count = len(scores)
        while iterator < len(scores):
            accumulator = accumulator + scores[iterator]
            iterator = iterator + 1
        average = accumulator / student_count
        return average

output = calculate_average([
    50, 0 , 100, 80, 90, 70, 50, 95, 60, 90, 50, 100, 70, 90])
print("The average of total scores in the class is ", output)