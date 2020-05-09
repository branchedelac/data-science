def remove_parenthesis(value):
    value = value.replace("(","")
    value = value.replace(")","")
    return value

for row in moma:
    nationality = row[2]
    row[2] = remove_parenthesis(nationality)
    
    gender = row[5]
    row[5] = remove_parenthesis(gender)