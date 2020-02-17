def run_sql(value, value2, value3):
    if value < value2:
        print('inclusive')
        print(value2, 'value2 is larger')
    elif value2 < value: 
        print('exclusive')
        print(value, 'value is larger')
    else:
        print(value3)


run_sql(24, 63, 34)
    
