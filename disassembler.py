def disassemble(operation_code):
    if (operation_code == '901'):
        return 'INP'
    elif (operation_code == '902'):
        return 'OUT'
    elif (operation_code[0] == '1'):
        return 'ADD ' + operation_code[1:3]
    elif (operation_code[0] == '2'):
        return 'SUB ' + operation_code[1:3]
    elif (operation_code[0] == '3'):
        return 'STA ' + operation_code[1:3]
    elif (operation_code[0] == '5'):
        return 'LDA ' + operation_code[1:3]
    elif (operation_code[0] == '6'):
        return 'BRA ' + operation_code[1:3]
    elif (operation_code[0] == '7'):
        return 'BRZ ' + operation_code[1:3]
    elif (operation_code[0] == '8'):
        return 'BRP ' + operation_code[1:3]
    elif (operation_code == '000'):
        return 'HLT'
    else:
        print('Input not understood')
    pass

def main():
    recceive_input = True
    inputs = []
    while (recceive_input):
        n = input("Enter Instructions: ")
        temp = disassemble(n)
        if (temp != None):
            inputs.append(disassemble(n))
        if (n == '000'):
            for i in inputs:
                print(i)
            recceive_input = False
    pass

if __name__ == "__main__":
    main()
