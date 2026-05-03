use std::fs::{self, File};
use std::io::Write;

fn read_define(cfg: &str, key: &str) -> String {
    for line in cfg.lines() {
        if line.starts_with("#define") && line.contains(key) {
            return line.split_whitespace().last().unwrap().replace("\"", "");
        }
    }
    panic!("Missing config: {}", key);
}

fn main() {
    let cfg = fs::read_to_string("fm_config.h").unwrap();

    let out = read_define(&cfg, "IQ_OUTPUT_FILE");

    let mut file = File::create(out).unwrap();

    // Simple test signal (placeholder FM core)
    for i in 0..500_000 {
        let v = (i as f32 * 0.002).sin();
        file.write_all(&v.to_le_bytes()).unwrap(); // I
        file.write_all(&v.to_le_bytes()).unwrap(); // Q
    }

    println!("Rust FM engine finished");
}
