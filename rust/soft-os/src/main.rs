
enum Instruction {
    NOP,
    BLA
}

fn main() {
    let ram = vec![Instruction::NOP, Instruction::BLA, Instruction::NOP];

    let mut instruction_pointer = 0;

    loop {
        match ram[instruction_pointer] {
            Instruction::NOP => {
                instruction_pointer = instruction_pointer + 1;
                println!("Waiting for input");
            }
            Instruction::BLA => {
                instruction_pointer = instruction_pointer + 1
            },
        }
    }
}
