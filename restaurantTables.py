# ------------------------------------------------------------------------------------
# The following 2D lists mimic a restaurant seating layout, similar to a grid.
# 
# - Row 0 is a "header row":
#     - The first cell (index 0) is just a row label (0).
#     - The remaining cells are table labels with capacities in parentheses,
#       e.g., 'T1(2)' means "Table 1" has capacity 2.
#
# - Rows 1 through 6 each represent a distinct "timeslot" or "seating period":
#     - The first cell in each row (e.g., [1], [2], etc.) is that row's label (the timeslot number).
#     - Each subsequent cell shows whether the table (from the header row) is
#       free ('o') or occupied ('x') during that timeslot.
#
# In other words, restaurant_tables[row][column] tells you the status of a
# particular table (column) at a particular timeslot (row).
# ------------------------------------------------------------------------------------

# Shows the structure of the restaurant layout with all tables free ("o" = open).
restaurant_tables = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'o',      'o',      'o',      'o',      'o',      'o'],
    [2,        'o',      'o',      'o',      'o',      'o',      'o'],
    [3,        'o',      'o',      'o',      'o',      'o',      'o'],
    [4,        'o',      'o',      'o',      'o',      'o',      'o'],
    [5,        'o',      'o',      'o',      'o',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'o',      'o']
]

# ------------------------------------------------------------------------------------
# This second layout serves as a test case where some tables ('x') are already occupied.
# Use this for testing your logic to:
#   - Find free tables (marked 'o')
#   - Check if those tables meet a certain capacity (from the header row, e.g. 'T1(2)')
#   - Potentially combine adjacent tables if one alone isn't enough for a larger party.
# ------------------------------------------------------------------------------------

restaurant_tables2 = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'x',      'o']
]

#--------------------------------------------------------------------------------------
#Level 1
def table_check(tables, time):
    #making list to put the data in
    free_tables = []
    #loops the the tabels
    for i in range(1, len(tables[0])):
        #checks if the tables are open
        if tables[time][i] == 'o':
            #adds all open tables to the list
            free_tables.append(tables[0][i])
    #returns tables
    return free_tables
#test call 
print(table_check(restaurant_tables2, 2))
#--------------------------------------------------------------------------------------
#Level 2
def party_size(tables, time, party):
    #loops tables
    for i in range(1, len(tables[0])):
        #gets the name of the table ex T1(2)
        table_name = tables[0][i]
        #string that shall hold the table_name
        seating_amount = ''
        #loop the the T1(2)
        for character in table_name:
            #to get the value inbetween the parentheses
            if character == '(':
                #gets value
                seating_amount = ''
            elif character == ')':
                #stops collection value
                break
            elif character.isdigit():
                #adds value
                seating_amount += character
        #to make the numbers comparable
        seating_capacity = int(seating_amount)
        #checks if table is open AND the seating is enought
        if tables[time][i] == 'o' and seating_capacity >= party:
            #returns
            return table_name
    #if nothing return nothing
    return None
#test call
print(party_size(restaurant_tables2, 2, 6))
#--------------------------------------------------------------------------------------
