
if __name__ == "__main__":
    RAM = ['NOP', 'NOP', 'BLABLA']

    instruction_pointer = 0

    while True:
        op = RAM[instruction_pointer]

        if op == 'NOP':
            print("Doing nothing")
        
        instruction_pointer += 1