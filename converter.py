print "\nThis program converts units. Simply write an amount and a unit e.g. '25 km', '30 deg C', '205 lbs'. The program will automaticaly convert it to other possible values. Don't forget the space between the number and the unit. To exit enter 'exit', for help and a list of supported units enter 'help'."


while True:
    
    print "\n"
    userInput = raw_input("What do you want to convert? ")
    success = False         # keeps track of errors
    
    units = {
        
        "km/h": {
            "kilometers per hour": "x * 0.621",
            "meters per second": "x * 1000 / 3600.0"
        },
        
        "mph": {
            "kilometers per hour": "x * 1.61",
            "meters per second": "x * 0.45"
        },
        
        "m/s": {
            "kilometers per hour": "x * 3.6",
            "miles per hour": "x * 2.237"
        },
        
        "km": {
            "miles": "x * 0.621"
        },
        
        "mi": {
            "kilometres": "x * 1.61"
        },
        
        "cm": {
            "inches": "x * 0.394",
            "feet": "x * 0.0328"
        },
        
        "m": {
            "inches": "x * 39.37",
            "feet": "x * 3.281"
        },
        
        "in": {
            "centimetres": "x * 2.54",
            "feet": "x * 1/12.0"
        },
        
        "ft": {
            "centimetres": "x * 30.48",
            "meters": "x * 0.305",
            "inches": "x * 12.0"
        },
        
        "deg C": {
            "degrees Fahrenheit": "x * (9/5.0) + 32",
            "Kelvin": "x + 273"
        },
        
        "deg F": {
            "degrees Celsius": "(x - 32) * (5/9.0)",
            "Kelvin": "(x + 459.67) * (5/9.0)"
        },
        
        "K": {
            "degrees Celsius": "x - 273",
            "degrees Fahrenheit": "x * 9/5.0 - 459.67"
        },
        
        "lbs": {
            "kilograms": "x * 0.454",
            "ounces": "x * 16",
            "stone": "x * 1/14.0"
        },
        
        "kg": {
            "pounds": "x * 2.205",
            "ounces": "x * 35.274",
            "stone": "x * 0.157"
        },
        
        "oz": {
            "grams": "x * 28.351",
            "pounds": "x * 1/16.0"
        }
        
    }


    
    if userInput.lower() == "exit":
        break
    if userInput.lower() == "help":
        print "Supported units are: \n"
        for unit in units:
            print unit
        print "\nYour input should have a space between the amount and the unit e.g. '25 km'"
        success = True

    amount = userInput.split()[0]

    
    #check if a supported unit is in user's input
    for unit in units:
        if userInput.endswith(" " + unit):
            
            #get all formulas and convert
            print userInput + " is equal to:"
            for convertTo, formula in units[unit].iteritems():
                
                print str(eval(formula.replace("x", amount))) + " " + convertTo
                success = True
                
            break
    
    if success != True:
        print "Unrecognized unit. Enter 'help' to see a list."
        






