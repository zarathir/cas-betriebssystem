
RAM = []

instruction_pointer = 0

while True:
    op = RAM[instruction_pointer]

    if op == 'NOP':
        instruction_pointer += 1