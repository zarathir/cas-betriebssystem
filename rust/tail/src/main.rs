use std::{process::Command};

fn main() {
    if let Ok(path) = std::env::current_dir() {
        let file = path.join("logdatei");
        Command::new("tail")
            .args(["-f", &file.display().to_string()])
            .status()
            .expect("Failed to execute command");
    }
}
