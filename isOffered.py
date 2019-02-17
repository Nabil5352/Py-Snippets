# Dictionaries of Dictionaries (of Dictionaries)

# The next several questions concern the data structure below for keeping
# track of Udacity's courses (where all of the values are strings):

#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

#For example,

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': 
                {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': 
                {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                 'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res

def is_offered(courses, course, hexamester):
  offered = courses_offered(courses, hexamester)

  for c in offered:
    if c == course:
      return True
      break
  
  return False


# print is_offered(courses, 'cs101', 'apr2012')
# >>> True

# print is_offered(courses, 'cs003', 'apr2012')
# >>> False

# print is_offered(courses, 'cs101', 'apr2012')
# >>> True

# print is_offered(courses, 'cs003', 'apr2012')
# >>> False

# print is_offered(courses, 'cs001', 'jan2044')
# >>> True

# print is_offered(courses, 'cs253', 'feb2012')
# >>> False


def when_offered(courses,course):
  res = []
  for c in courses:
    if is_offered(courses, course, c):
      res.append(c)

  return res

# print when_offered (courses, 'cs101')
#>>> ['apr2012', 'feb2012']

# print when_offered(courses, 'bio893')
#>>> []


# [Double Gold Star] Define a procedure, involved(courses, person), that takes 
# as input a courses structure and a person and returns a Dictionary that 
# describes all the courses the person is involved in.  A person is involved 
# in a course if they are a value for any property for the course.  The output 
# Dictionary should have hexamesters as its keys, and each value should be a 
# list of courses that are offered that hexamester (the courses in the list 
# can be in any order).

def involved(courses, person):
  involved = {}
  for hexamester in courses:
    arr = []
    for course in courses[hexamester]:
      exists = False
      if 'teacher' in courses[hexamester][course]:
        if courses[hexamester][course]['teacher'] == person:
          exists = True
      
      if 'assistant' in courses[hexamester][course]:
        if courses[hexamester][course]['assistant'] == person:
          exists = True

      if exists:
        arr.append(course)

    if len(arr) > 0:
      involved[hexamester] = arr

  return involved

# For example:

# print involved(courses, 'Dave')
#>>> {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}

# print involved(courses, 'Peter C.')
#>>> {'apr2012': ['cs262'], 'feb2012': ['cs101']}

# print involved(courses, 'Dorina')
#>>> {'jan2044': ['cs001']}

# print involved(courses,'Peter')
#>>> {}

# print involved(courses,'Robotic')
#>>> {}

# print involved(courses, '')
#>>> {}
