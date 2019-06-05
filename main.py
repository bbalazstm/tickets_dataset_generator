import csv
from random import randint
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
_NUM_TICKETS_TRAINING   = 200   # CSV for training data
_NUM_TICKETS_TESTING    = 50    # CSV for testing data
_NUM_EMPLOYEES          = 4     # Number of employees that work with tickets
_NUM_CATEGORIES         = 4     # Number of possible categories for the tickets
_NUM_GROUPS             = 2     # Number of groups where tickets can be assigned 
_NUM_TYPES              = 4     # Number of types
_MISTAKES               = False # Allow randint mistakes: category routing to wrong group/person, etc - TO DO

_TRAINING_CSV_HEAD = [
        'ID',
        'Priority',
        'Type',
        'Category',
        'Title',
        'Group',
        'Asignee'
]

_TESTING_CSV_HEAD = [
        'ID',
        'Priority',
        'Type',
        'Category',
        'Title',
        'Group'
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

_NAME_TITLE = [
    ['Hardware', f'HDD failure {randint(1,254)}.{randint(1,254)}.{randint(1,254)}.{randint(1,254)}'],
    ['Hardware', f'Cooler failure {randint(1,254)}.{randint(1,254)}.{randint(1,254)}.{randint(1,254)}'],
    ['Hardware', f'Motherboard failure {randint(1,254)}.{randint(1,254)}.{randint(1,254)}.{randint(1,254)}'],
    ['Hardware', f'Graphic card failure {randint(1,254)}.{randint(1,254)}.{randint(1,254)}.{randint(1,254)}'],
    ['Hardware', f'New PC Tower'],
    ['Hardware', f'New laptop unit'],
    ['Hardware', f'New Bullion X server'],
    ['Hardware', f'New BullSequana server'],
    ['Software', f'Office License for {randint(1,254)}.{randint(1,254)}.{randint(1,254)}.{randint(1,254)}'],
    ['Software', f'PowerBI License for {randint(1,254)}.{randint(1,254)}.{randint(1,254)}.{randint(1,254)}'],
    ['Software', f'Skype not working for {randint(1,254)}.{randint(1,254)}.{randint(1,254)}.{randint(1,254)}'],
    ['Software', f'Visual Studio license'],
    ['Software', f'Windows license'],
    ['Networking', f'Cannot access webserver {randint(1,254)}.{randint(1,254)}.{randint(1,254)}.{randint(1,254)}'],
    ['Networking', f'New LAN'],
    ['Networking', f'Assign static IP'],
    ['Networking', f'Cannot access host {randint(1,254)}.{randint(1,254)}.{randint(1,254)}.{randint(1,254)}'],
    ['Networking', f'New switch/router installation'],
    ['Firewall', f'Unblock HTTPS for {randint(1,254)}.{randint(1,254)}.{randint(1,254)}.{randint(1,254)}'],
    ['Firewall', f'Unblock SSH to {randint(1,254)}.{randint(1,254)}.{randint(1,254)}.{randint(1,254)}'],
    ['Firewall', f'New network'],
    ['Firewall', f'New IP for host {randint(1,254)}.{randint(1,254)}.{randint(1,254)}.{randint(1,254)} needs cleareance']
]

_NAME_EMPLOYEES = [
    'AA',
    'BB',
    'CC',
    'DD',
    'EE',
    'FF',
    'GG',
    'ZZ'
]

_NAME_GROUPS = [
    'CLIENT_L1',
    'CLIENT_L2'
]

# Use this list to ensure that the same people
# work on a specific category
_PERSON_TO_CATEGORY = [
        ['AA', 'Hardware'],
        ['BB', 'Software'],
        ['CC', 'Networking'],
        ['DD', 'Firewall']
]

# Config of writer
csv.register_dialect('myDialect',
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True)

def findTitle(param):
    possible_titles = []
    total_possible_titles = 0

    for elem in _NAME_TITLE:
        if elem[0] == param:
            possible_titles.append(elem[1])
            total_possible_titles += 1

    if not possible_titles:             # If category has no titles 
        return 'test'
    else:
        return possible_titles[randint(0,total_possible_titles-1)]

def findSuitablePerson(param):
    for elem in _PERSON_TO_CATEGORY:
        if elem[1] == param:
            return elem[0]

# Writing data for training
with open('training.csv', 'w', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')

        writer.writerow(_TRAINING_CSV_HEAD)                                     # CSV Titles

        finalList = []
        for i in range(_NUM_TICKETS_TRAINING):
                line=[]
                line.append(i+1)                                                # Ticket ID
                line.append(randint(1,5))                                       # Ticket Prio
                line.append(_NAME_TYPES[randint(0,_NUM_TYPES-1)])               # Ticket Type
                line.append(_NAME_CATEGORIES[randint(0,_NUM_CATEGORIES-1)])     # Ticket Category
                line.append(findTitle(line[3]))                                 # Ticket Title
                line.append(_NAME_GROUPS[randint(0, _NUM_GROUPS-1)])            # Ticket Group
                line.append(findSuitablePerson(line[3]))                        # Employee Name
                writer.writerow(line)

        f.close()

with open('testing.csv', 'w', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')

        writer.writerow(_TESTING_CSV_HEAD)                                      # CSV Titles

        finalList = []
        for i in range(_NUM_TICKETS_TRAINING):
                line=[]
                line.append(i+1)                                                # Ticket ID
                line.append(randint(1,5))                                       # Ticket Prio
                line.append(_NAME_TYPES[randint(0,_NUM_TYPES-1)])               # Ticket Type
                line.append(_NAME_CATEGORIES[randint(0,_NUM_CATEGORIES-1)])     # Ticket Category
                line.append(findTitle(line[3]))                                 # Ticket Title
                line.append(_NAME_GROUPS[randint(0, _NUM_GROUPS-1)])            # Ticket Group
                writer.writerow(line)

        f.close()