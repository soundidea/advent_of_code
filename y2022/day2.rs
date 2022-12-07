use std::fs;

fn main() {
  let input = fs::read_to_string("day2_input.txt").unwrap();
  let turns: Vec<(i32, i32)> =
      input.trim()
           .split("\n")
           .map(|t| (t.chars().nth(0).unwrap() as i32 - 'A' as i32,
                     t.chars().nth(2).unwrap() as i32 - 'X' as i32)).collect();
  println!("part 1: {:?}",
           turns.iter()
                .map(|t| t.1 + 1 + 3 * ((t.1 - t.0 + 1).rem_euclid(3)))
                .sum::<i32>());
  println!("part 2: {:?}",
           turns.iter()
                .map(|t| 3 * t.1 + 1 + ((t.0 + t.1 - 1).rem_euclid(3)))
                .sum::<i32>());
}

