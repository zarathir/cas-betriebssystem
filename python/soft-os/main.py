import threading
import time

INTERRUPT_INTERVAL = 5  # in Sekunden
INTERRUPT_OFFSET = 10
interrupt = False

NOP = 0x00
ADD = 0x01
SUB = 0x02
JMP = 0x03
HLT = 0xFF

PROGRAM = [ADD, 0x00, 0x01, JMP, 0x06, HLT, ADD, 0x01, 0x01, JMP, 0x00, NOP, HLT]

class Cpu(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.instruction_pointer = 0
        self.register = [0] * 8
        self.program = PROGRAM

    def handle_interrupt(self):
        global interrupt
        
        if interrupt is True:
            instruction_pointer_old = self.instruction_pointer
            self.instruction_pointer = INTERRUPT_OFFSET
            self.handle_instruction()
            self.instruction_pointer = instruction_pointer_old

            interrupt = False

    def handle_instruction(self):
            operation = PROGRAM[self.instruction_pointer]

            if operation == NOP:
                print("Doing nothing")
                self.instruction_pointer += 1
                pass

            elif operation == ADD:
                self.register[PROGRAM[self.instruction_pointer + 1]] += self.register[
                    PROGRAM[self.instruction_pointer + 2]
                ]
                self.instruction_pointer += 3

            elif operation == SUB:
                self.register[PROGRAM[self.instruction_pointer + 1]] -= self.register[
                    PROGRAM[self.instruction_pointer + 2]
                ]
                self.instruction_pointer += 3

            elif operation == JMP:
                self.instruction_pointer = PROGRAM[self.instruction_pointer + 1]

            elif operation == HLT:
                exit(0)

    def run(self):
        while True:
            self.handle_instruction()
            self.handle_interrupt()


def interrupt_controller_thread():
    global interrupt
    
    while True:
        time.sleep(INTERRUPT_INTERVAL)
        print("Triggering interrupt")
        interrupt = True


if __name__ == "__main__":
    cpu = Cpu()
    pic = threading.Thread(target=interrupt_controller_thread)

    cpu.start()
    pic.start()

    cpu.join()
    pic.join()
