import expression_validator

#Iterates through the expression list and evaluates each expression
def calculate(expressions):
    for i in range(0,len(expressions)):
        answer  = expression_validator.gui_function_validator(expressions[i], None)
        print expressions[i] + " = " + answer

#Loads expressions into a list
def loadFile(fileName):
    fpt=open(fileName, 'r')
    dataFile=fpt.read()
    expressions = dataFile.split('\n')
    expressions = expressions[0:-1]
    return expressions

#Checks to see if commandLine argument is a file
def fileCheck(fileName):
    try:
        with open(fileName, 'r') as fl:
            return True
    except IOError as ex:
        return False

def main(system, fileName):
    if not fileCheck(fileName):
        system.exit("Error. File name does not exist.")
    else:
       expressions = loadFile(fileName)
       calculate(expressions)
