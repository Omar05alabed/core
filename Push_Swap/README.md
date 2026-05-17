*This activity has been created as part of the 42 curriculum by oalabed, domansou.*

# Push_swap

## Description

Push_swap is a C program that sorts a list of integers using **two stacks** (`a` and `b`) and a limited set of operations. The goal is to sort the numbers in ascending order using the **minimum number of operations**.

---

## Usage

### Compile

```bash
make
```

### Run

```bash
./push_swap [OPTIONS] <numbers>
```

### Options

* `--simple` → O(n²)
* `--medium` → O(n√n)
* `--complex` → O(n log n)
* `--adaptive` → default (based on disorder)
* `--bench` → show performance info

---

## Rules

* Stack `a` starts filled, `b` is empty
* No duplicate numbers
* Allowed operations:
  `sa sb ss pa pb ra rb rr rra rrb rrr`
* Output = list of operations (one per line)
* Errors → print `Error`

---

## Algorithms

* **Simple (O(n²))** → basic sorting (e.g., selection)
* **Medium (O(n√n))** → chunk-based sorting
* **Complex (O(n log n))** → radix sort
* **Adaptive** → chooses strategy based on disorder:

| Disorder | Strategy   |
| -------- | ---------- |
| < 0.2    | O(n)       |
| 0.2–0.5  | O(n√n)     |
| ≥ 0.5    | O(n log n) |

---

## Benchmark (--bench)

Shows:

* Disorder %
* Strategy used
* Total operations
* Count of each operation

---

## Requirements

* No memory leaks
* No crashes
* Follow 42 Norm
* Provide Makefile (`all`, `clean`, `fclean`, `re`)

---
## Resources

Sorting algorithms (Radix, Insertion, Chunking)
Big-O complexity theory
42 subject PDF

## AI Usage

AI was used for:

Understanding algorithm strategies
Debugging ideas and edge cases
Improving test coverage

All code was written and fully understood before submission.

---
## Contributors

## 👥 Contributors

This project was developed collaboratively by **Doa' Manasrah** and **Omar Alabed**, with each contributor focusing on specific aspects of the implementation while working together on integration and testing.

### 🔹 Omar Alabed
Omar was responsible for studying and implementing the core data structures and input handling components of the project. His contributions include:

- **Stack Implementation**
  - Designing and implementing the linked-list based stack structure.
  - Managing memory allocation and deallocation for stack nodes.
  - Implementing utility functions related to stack manipulation.

- **Parsing**
  - Handling command-line arguments and tokenization.
  - Validating numeric inputs and detecting duplicates.
  - Converting input data into usable integer arrays.
  - Implementing error handling for invalid inputs.

- **Benchmark Module**
  - Studying and implementing the benchmarking concept.
  - Writing the code responsible for counting operations.
  - Providing explanations and metrics such as complexity, strategy, and disorder.

**Related Files/Functions:**
- `push_swap.h` (struct definitions related to stack and benchmark)
- Stack utilities: `new_node`, `ft_push`, `stack_size`, `assign_index`, `free_stack`
- Parsing: `ft_atoi`, `to_int_array`, `is_number`, `ft_duplicate`, `print_error`
- Tokenization: `collect_tokens`, `split_whitespace`, `free_split`, `is_space`
- Benchmark: `bench_init`, `bench`, and operation counters within all stack operations

---

### 🔹 Doa' Manasrah
Doa' focused on the algorithmic aspects of the project and the coordination between different modules. Her contributions include:

- **Sorting Algorithms**
  - Studying and implementing efficient sorting strategies.
  - Implementing multiple algorithms such as `simple_sort`, `radix_sort`, `sort_medium_chunk`, and `adaptive_sort`.
  - Developing logic to select the optimal strategy based on the level of disorder.

- **Flags Handling**
  - Designing and implementing command-line flag management.
  - Setting benchmarking strategies and controlling program behavior through flags.

- **Integration**
  - Linking all project components together within the `main` workflow.
  - Ensuring smooth interaction between parsing, stack operations, sorting algorithms, and benchmarking.

**Related Files/Functions:**
- Sorting: `simple_sort`, `radix_sort`, `sort_medium_chunk`, `adaptive_sort`
- Analysis: `compute_disorder`, `is_sorted`
- Flags & Integration: `handle_flags`, `set_strategy`, `check_sorted`, `init_stack`
- Program orchestration within `main.c`

---

### 🤝 Shared Contributions

Both contributors collaborated on several important aspects of the project:

- **Integration of all modules** to ensure seamless functionality.
- **Extensive testing** using a wide range of test cases, including:
  - Valid inputs.
  - Edge cases (e.g., INT limits, single number, already sorted lists).
  - Invalid inputs that should trigger the `"Error"` message.
- **Debugging and optimization** to ensure correctness and efficiency.
- **Project design discussions** and decision-making regarding architecture and strategy selection.

---

### 📁 Summary Table

| Area | Contributor |
|------|------------|
| Stack Implementation | Omar Alabed |
| Parsing & Input Validation | Omar Alabed |
| Benchmark Module | Omar Alabed |
| Sorting Algorithms | Doa' Manasrah |
| Flags Handling | Doa' Manasrah |
| Integration & Main Workflow | Doa' Manasrah |
| Testing & Debugging | Both |


