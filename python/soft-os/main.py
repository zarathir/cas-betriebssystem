NOP = 0x00
ADD = 0x01
SUB = 0x02
JMP = 0x03
HLT = 0xFF

PROGRAM = [
    ADD, 0x00, 0x01,
    JMP, 0x06,
    
    HLT,

    ADD, 0x01, 0x01,
    JMP, 0x00,
    
    HLT
]

if __name__ == "__main__":
    register = [0] * 8

    instruction_pointer = 0

    while True:
        operation = PROGRAM[instruction_pointer]

        if operation == NOP:
            instruction_pointer += 1
            pass

        elif operation == ADD:
            register[PROGRAM[instruction_pointer + 1]] += register[PROGRAM[instruction_pointer + 2]]
            instruction_pointer += 3
                
        elif operation == SUB:
            register[PROGRAM[instruction_pointer + 1]] -= register[PROGRAM[instruction_pointer + 2]]
            instruction_pointer += 3
        
        elif operation == JMP:
            instruction_pointer = PROGRAM[instruction_pointer + 1]

        elif operation == HLT:
            instruction_pointer += 1
            exit