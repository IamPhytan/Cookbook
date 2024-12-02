use itertools::Itertools;

fn main() {
    let a: Vec<i32>;
    let b: Vec<u32>;

    a = vec![5, 6, 5, -28];
    // b = a.iter().map(|&x| x as u32).collect();
    b = a
        .to_owned()
        .into_iter()
        .filter(|&x| x >= 0)
        .map(|x| x as u32)
        .collect();
    println!("{:?} {:?}", a, b);

    let c: Vec<_> = a
        .iter()
        .map(|&elem| match elem {
            5 => 0,
            2 | 4 | 6 => 1,
            _ => -1,
        })
        .collect();
    println!("{:?}", c);

    let nums: Vec<u8> = vec![5, 4, 6, 3, 9, 8, 1];
    let chars: Vec<char> = nums.iter().sorted().map(|x| (x + 64) as char).collect();
    println!("{:?}\n{:?}", nums, chars);
}
