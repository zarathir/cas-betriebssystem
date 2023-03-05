
enum Instruction {
    NOP,
}

fn main() {
    let ram = Vec::<Instruction>::new();

    let mut instruction_pointer = 0;

    loop {
        match ram[instruction_pointer] {
            Instruction::NOP => instruction_pointer = instruction_pointer + 1,
        }
    }
}
