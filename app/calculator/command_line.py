import processing

columns = "{0:30}{1:5}{2:30}"

def evaluate_from_file(filename):
    try:
        with open(filename, "r") as f:
            print columns.format("Expression", " | ", "Answer")
            print "------------------------------------------------------------------------------"
            for expression in f:
                expression = expression.replace("\n", "")
                result = processing.evaluate_expression(expression, None)
                try:
                    float(result)
                    print columns.format(expression, " = " , result)
                except ValueError:
                    print columns.format(expression, " = " , result)
                except TypeError:
                    print columns.format(expression, " = " , "Cannot graph expressions from file")
            print "------------------------------------------------------------------------------"
    except IOError:
        print "Could not find file"
