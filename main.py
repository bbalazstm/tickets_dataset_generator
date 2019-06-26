import csv
import random
### Cols
# ID        - 1,2,3,4..
# Prio      - 1,2,3,4,5
# Type      - Incident, Task, Problem, Issue
# Category  - Hardware, Software, Networking, Firewall
# Title
# Group     - ABC_Infra, ABC_Hardware, ABC_Networking, ABC_Firewall
# Person    - None, AA, BB, CC, DD, etc
# TtC       - 5, 10, 20, 30, etc
### ID, Prio, Type, Category, Title, Group, Person, TtC
_NUM_TICKETS_TRAINING   = 700   # CSV for training data
_NUM_TICKETS_TESTING    = 300   # CSV for testing data
_NUM_TICKETS_VALIDATION = 300   # CSV for validation data
_NUM_EMPLOYEES          = 4     # Number of employees that work with tickets
_NUM_CATEGORIES         = 4     # Number of possible categories for the tickets
_NUM_GROUPS             = 2     # Number of groups where tickets can be assigned 
_NUM_TYPES              = 4     # Number of types
_MISTAKES               = False # Allow random.randint mistakes: category routing to wrong group/person, etc - TO DO

_TRAINING_CSV_HEAD = [
        'ID',
        'Priority',
        'Type',
        'Category',
        'Title',
        'Group',
        'Asignee'
]

_VALIDATION_CSV_HEAD = [
        'ID',
        'Priority',
        'Type',
        'Category',
        'Title',
        'Group',
        'Assignee'
]

_NAME_TYPES = [
        'Incidents',
        'Task',
        'Problem',
        'Issue'
]

_NAME_CATEGORIES = [
    'Hardware', 
    'Software', 
    'Networking', 
    'Firewall', 
    'User management', 
    'Infrastructure',
    'Purchasing',
    'Helpdesk'
]

_NAME_EMPLOYEES = [
    1,
    2,
    3,
    4
]

_NAME_GROUPS = [
    'CLIENT_L1',
    'CLIENT_L2'
]

_GROUP_TO_EMPLOYEE = [
        [1, 'CLIENT_L1'],
        [2, 'CLIENT_L2'],
        [3, 'CLIENT_L1'],
        [4, 'CLIENT_L2']
]

# Use this list to ensure that the same people
# work on a specific category or give them weights
_CATEGORY_TO_PERSON = [
        ['Hardware', [1] * 50 + [2] * 25 + [3] * 20 + [4] * 5],
        ['Software', [1] * 25 + [2] * 50 + [3] * 5 + [4] * 20],
        ['Networking', [1] * 5 + [2] * 20 + [3] * 50 + [4] * 25],
        ['Firewall', [1] * 20 + [2] * 5 + [3]* 25 + [4] * 50]
]

_PRIO_TO_TTC = [
        [1, 15],
        [2, 30],
        [3, 60],
        [4, 90],
        [5, 100]
]

# Config of writer
csv.register_dialect('myDialect',
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True)

def findTitle(param):
        _NAME_TITLE = [
                ['Hardware', f'HDD failure {random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}'],
                ['Hardware', f'Cooler failure {random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}'],
                ['Hardware', f'Motherboard failure {random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}'],
                ['Hardware', f'Graphic card failure {random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}'],
                ['Hardware', f'New PC Tower'],
                ['Hardware', f'New laptop unit'],
                ['Hardware', f'New Bullion X server'],
                ['Hardware', f'New BullSequana server'],
                ['Software', f'Office License for {random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}'],
                ['Software', f'PowerBI License for {random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}'],
                ['Software', f'Skype not working for {random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}'],
                ['Software', f'Visual Studio license'],
                ['Software', f'Windows license'],
                ['Networking', f'Cannot access webserver {random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}'],
                ['Networking', f'New LAN'],
                ['Networking', f'Assign static IP'],
                ['Networking', f'Cannot access host {random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}'],
                ['Networking', f'New switch/router installation'],
                ['Firewall', f'Unblock HTTPS for {random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}'],
                ['Firewall', f'Unblock SSH to {random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}'],
                ['Firewall', f'New network'],
                ['Firewall', f'New IP for host {random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)} needs cleareance']
        ]        
        possible_titles = []
        total_possible_titles = 0

        for elem in _NAME_TITLE:
                if elem[0] == param:
                        possible_titles.append(elem[1])
                        total_possible_titles += 1

        if not possible_titles:             # If category has no titles 
                return 'N/A'
        else:
                return possible_titles[random.randint(0,total_possible_titles-1)]

def findSuitablePerson(category):
        for elem in _CATEGORY_TO_PERSON:
                if elem[0] == category:
                        val = random.choice(elem[1])

        return val

def weightedPrios():
        possible_values = [1] * 5 + [2] * 15 + [3] * 20 + [4] * 30 + [5] * 30
        return random.choice(possible_values)

def findTTC(prio):
        for elem in _PRIO_TO_TTC:
                if elem[0] == prio:
                        return elem[1]

def findGroup(employee):
        for elem in _GROUP_TO_EMPLOYEE:
                if elem[0] == employee:
                        return elem[1]

def generateLine():
        line=[]
        line.append(i+1)                                                        # Ticket ID
        line.append(weightedPrios())                                            # Ticket Prio
        line.append(_NAME_TYPES[random.randint(0,_NUM_TYPES-1)])                # Ticket Type
        line.append(_NAME_CATEGORIES[random.randint(0,_NUM_CATEGORIES-1)])      # Ticket Category
        line.append(findTitle(line[3]))                                         # Ticket Title
        line.append(findTTC(line[1]))                                           # Time to close
        line.append(findSuitablePerson(line[3]))                                # Employee Name
        line.append(findGroup(line[6]))                                         # Ticket Group

        a, b = 6, 7
        line[7], line[6] = line[6], line[7]

        return line

# Writing data for training
with open('training.csv', 'w', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')

        writer.writerow(_TRAINING_CSV_HEAD)                                     # CSV Titles

        finalList = []
        for i in range(_NUM_TICKETS_TRAINING):
                line=generateLine()
                writer.writerow(line)

        f.close()

with open('testing.csv', 'w', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')

        writer.writerow(_TRAINING_CSV_HEAD)                                      # CSV Titles

        finalList = []
        for i in range(_NUM_TICKETS_TESTING):
                line=generateLine()
                writer.writerow(line)

        f.close()

with open('validation.csv', 'w', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')

        writer.writerow(_VALIDATION_CSV_HEAD)                                      # CSV Titles

        finalList = []
        for i in range(_NUM_TICKETS_VALIDATION):
                line=generateLine()
                writer.writerow(line)

        f.close()        