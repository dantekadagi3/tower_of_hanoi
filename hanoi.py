def move_disk(n, from_rod, to_rod):
    print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")

def solve_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        move_disk(n, from_rod, to_rod)
        return
    solve_hanoi(n - 1, from_rod, aux_rod, to_rod)
    move_disk(n, from_rod, to_rod)
    solve_hanoi(n - 1, aux_rod, to_rod, from_rod)

def calculate_steps(n):
    return 2 ** n - 1

def main():
    num_disks = int(input("Enter the number of disks: "))
    
    from_rod = input("Enter the starting rod (A, B, or C): ").upper()
    
    to_rod = input("Enter the destination rod (A, B, or C): ").upper()
    
    if (from_rod == 'A' and to_rod == 'B') or (from_rod == 'B' and to_rod == 'A'):
        aux_rod = 'C'
    elif (from_rod == 'A' and to_rod == 'C') or (from_rod == 'C' and to_rod == 'A'):
        aux_rod = 'B'
    else:
        aux_rod = 'A'

    print(f"Solving Tower of Hanoi with {num_disks} disks from rod {from_rod} to rod {to_rod}:")
    solve_hanoi(num_disks, from_rod, to_rod, aux_rod)
    
    steps = calculate_steps(num_disks)
    print(f"Number of steps taken: {steps}")

if __name__ == "__main__":
    main()
