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

restaurant_tables2 = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'x'],
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
#--------------------------------------------------------------------------------------
#Level 2
def party_size(tables, time, party):
    for i in range(1, len(tables[0])):
        table_name = tables[0][i]
        #empty string for adding
        seating_amount = ''
        #gets the number
        for character in table_name:
            if character == '(':
                seating_amount = ''
            elif character == ')':
                break
            #checks number
            elif character.isdigit():
                #adds number
                seating_amount += character
        #add the number to the empty string
        seating_capacity = int(seating_amount)
        #checks if is open
        if tables[time][i] == 'o' and seating_capacity >= party:
            return table_name
    return None
#--------------------------------------------------------------------------------------
#Level 3
def tables_for_party(tables, party):
    able_tables = []
    
    for i in range(1, len(tables[0])):
        table_name = tables[0][i]
        
        seating_amount = ''
        
        for character in table_name:
            if character == '(':
                seating_amount = ''
            elif character == ')':
                break
            elif character.isdigit():
                seating_amount += character
                
        seating_capacity = int(seating_amount)
        #checks availability of timeslots
        for time in range(1, len(tables)):
            #checks if the party size matches up
            if tables[time][i] == 'o' and seating_capacity >= party:
                #checks if the name is not already added
                if table_name not in able_tables:
                    #adds name if no dupes
                    able_tables.append(table_name)
                break
    #returns if exists
    return able_tables or None
#----------------------------------------------------------------------------------------
#Level 4
def combine_party(tables, party):
    able_tables = []
    #same as previous
    for i in range(1, len(tables[0])):
        table_name = tables[0][i]
        
        seating_amount = ''
        
        #extract seating capacity from the table name
        for character in table_name:
            if character == '(':
                seating_amount = ''
            elif character == ')':
                break
            elif character.isdigit():
                seating_amount += character
        seating_capacity = int(seating_amount)
        #check availability for the current table alone
        for time in range(1, len(tables)):
            if tables[time][i] == 'o' and seating_capacity >= party:
                able_tables.append([table_name])
                break 
        #check availability for adjacent table pairs
        if i < len(tables[0]) - 1:
            next_table_name = tables[0][i + 1]
            
            #checking next items
            
            #extract seating capacity of the next table
            next_seating_capacity = ''
            for character in next_table_name:
                if character == '(':
                    next_seating_capacity = ''
                elif character == ')':
                    break
                elif character.isdigit():
                    next_seating_capacity += character
            next_seating_capacity = int(next_seating_capacity)
            
            #check if table1 + table2 = amount of party
            for time in range(1, len(tables)):
                if tables[time][i] == 'o' and tables[time][i + 1] == 'o' and (seating_capacity + next_seating_capacity) >= party:
                    able_tables.append([table_name, next_table_name]) 
                    break 
    
    return able_tables or None
#-----------------------------------------------------------------------------------------
#Testing

#print(table_check(restaurant_tables2, 2))
#print(party_size(restaurant_tables2, 2, 2))
#print(tables_for_party(restaurant_tables2, 2))
#print(combine_party(restaurant_tables2, 5))
