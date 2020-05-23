
courses = ['English', 'Hindi', 'Marathi', 'Math']

print(courses)

courses.append('Science')

print(courses)

courses.insert(3, 'Social Science')

print(courses)

courses_2 = ['Art', 'commerce']

print(courses + courses_2)

courses.extend(courses_2)

print(courses)

popped = courses.pop()

print(popped)

print(courses)

courses.remove('Hindi')

print(courses)


courses.reverse()

print(courses)


courses.sort()

print(courses)


nums = [1, 3, 4, 5, 6, 12, 2]

# nums.sort(reverse=True)

num_sorted = sorted(nums)

print(nums)
print(num_sorted)

print(min(nums))
print(max(nums))

print(courses.index('Math'))
print('Hindi' in courses)


for index, item in enumerate(courses, start=1):
    print(index, item)


course_str = ', '.join(courses)
print(course_str)

print(course_str.split(', '))

# TUPLES (IMMUATABLE)

# SETS
