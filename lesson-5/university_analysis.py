universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(list_data):
    enrollments = [u[1] for u in list_data]
    tuitions = [u[2] for u in list_data]
    return enrollments, tuitions

def mean(values):
    return sum(values) / len(values)

def median(values):
    values.sort()
    n = len(values)
    mid = n // 2
    
    if n % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2
    else:
        return values[mid]

enrollments, tuitions = enrollment_stats(universities)

total_students = sum(enrollments)
total_tuition = sum(tuitions)

print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}\n")
print(f"Student mean: {mean(enrollments):,.2f}")
print(f"Student median: {median(enrollments):,}\n")
print(f"Tuition mean: $ {mean(tuitions):,.2f}")
print(f"Tuition median: $ {median(tuitions):,}")

#Task Details
# Define a function, _enrollment_stats()_, that takes, as an input, a list of lists where each individual list contains three elements: 
# (a) the name of a university, (b) the total number of enrolled students, and (c) the annual tuition fees.
# _enrollment_stats()_ should return two lists: the first containing all of the student enrollment values and 
# the second containing all of the tuition fees.
# Next, define a _mean()_ and a _median()_ function. Both functions should take a single list as an argument and
# return the mean and median of the values in each list.
# Using universities, _enrollment_stats()_, _mean()_, and _median()_, calculate the total number of students, the total tuition, the mean and
# median of the number of students, and the mean and median tuition values.
# Finally, output all values, and format the output so that it looks like this:

# Total students: 77,285
# Total tuition: $ 271,905

# Student mean: 11,040.71
# Student median: 10,566

# Tuition mean: $ 38,843.57
# Tuition median: $ 39,849
