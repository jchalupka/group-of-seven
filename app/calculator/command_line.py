import processing


def evaluate_from_file(filename):
    try:
        with open(filename, "r") as f:
            for expression in f:
                expression = expression.replace("\n", "")
                result = processing.evaluate_expression(expression, None)
                try:
                    float(result)
                    print expression + " = " + result
                except ValueError:
                    print result
                except TypeError:
                    print "Cannot graph expressions from file"
    except IOError:
        print "Could not find file"
