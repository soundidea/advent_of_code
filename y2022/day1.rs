use std::fs;
use std::str::FromStr;

fn main() {
  let input = fs::read_to_string("day1_input.txt").unwrap();
  let mut elves: Vec<i32> =
      input.split("\n\n")
           .map(|elf| elf.trim()
                         .split("\n")
                         .map(|snack| i32::from_str(snack)
                                          .unwrap_or(0)
                             ).sum::<i32>()
               ).collect();
  elves.sort_by(|a, b| b.cmp(a));
  println!("part 1: {:?}", elves[0]);
  println!("part 2: {:?}", elves[0..3].iter().sum::<i32>())
}
