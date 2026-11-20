---
type: concept
tags: [hdl, verilog, digital-design, verification]
sources: ["[[chapter-5-hdl-behavioral-model-source]]", "My Note My Life/6 - Full Note/Behavioral Model.md", "My Note My Life/6 - Full Note/Test Bench.md"]
updated: 2026-11-20
---

# HDL Behavioral Modeling and Testbenches

Core principles of behavioral modeling and simulation testbenches in Verilog HDL, covering procedural blocks, sensitivity lists, blocking vs. non-blocking assignments, conditional/case constructs, and verification timing.

---

## 1. Behavioral Modeling Overview

Behavioral modeling describes *what* a digital circuit does algorithmically rather than specifying gate-level structure:
- Uses **procedural blocks** (`initial` and `always`), all of which execute **concurrently** with respect to one another.
- Inside each procedural block, statements execute **sequentially** or **in parallel** depending on the assignment operator used.
- The left-hand side (LHS) of procedural assignments must be variable types (`reg`).

---

## 2. Procedural Blocks: `initial` vs. `always`

| Feature | `initial` block | `always` block |
|---|---|---|
| **Execution** | Executes **once** | Executes **continuously** in a loop |
| **Start time** | Starts at simulation time `0` | Starts at simulation time `0` |
| **Triggering** | No sensitivity/trigger list; starts automatically | Controlled by a **trigger (sensitivity) list** |
| **Synthesis** | Generally **not synthesizable** | Primarily used for **synthesizable hardware** |
| **Logic use** | Inappropriate for combinational/sequential hardware | Used for both combinational and sequential logic |
| **Best for** | Testbenches and simulation initialization | Implementing actual hardware functionality |

### Rules for `always` Blocks
```verilog
always @(<trigger_list>) begin
    <procedural_statements>
end
```
- A module may contain an unlimited number of `initial` and `always` blocks, all running concurrently.
- Procedural blocks **cannot be nested** inside one another.

---

## 3. Trigger (Sensitivity) Lists

- Introduced by `@(...)` and contain **signals** (scalar or vector, `wire` or `reg`), not expressions.
- A single module can contain both level-triggered and edge-triggered `always` blocks:
  - **Level-triggered (Combinational logic):** Executes whenever any listed signal changes state.
    - Old style: `@(sig1 or sig2 or sig3)`
    - New style: `@(sig1, sig2, sig3)` (or `@(*)`)
  - **Edge-triggered (Sequential logic):** Executes on rising (`posedge`) or falling (`negedge`) transitions.
    - Old style: `@(posedge clk or negedge rst_n)`
    - New style: `@(posedge clk, negedge rst_n)`

---

## 4. Clock vs. Control Signals

| Feature | Clock Signal (`clk`) | Control Signal (`reset`, `set`, etc.) |
|---|---|---|
| **Primary role** | **Synchronizes** module state updates | **Handles** specific overrides/operations |
| **Trigger list status** | **Always included** in sequential trigger lists | Included for asynchronous control; omitted for synchronous control |
| **Trigger type** | Rising (`posedge`) or falling (`negedge`) edge | Active-low or active-high level |
| **Checking inside block** | **Not checked** inside the block | **Always checked** inside the block (e.g., `if (reset == 0)`) |
| **Examples** | System clock, master timing signal | Reset, Clear, Set, Preset |

---

## 5. Blocking (`=`) vs. Non-Blocking (`<=`) Assignments

| Feature | Blocking Assignment (`=`) | Non-Blocking Assignment (`<=`) |
|---|---|---|
| **Execution** | Statements execute **one by one** in written order | All assignments update **simultaneously** at the end of the time step |
| **Timing** | Each statement completes before the next starts | Statements do not block one another |
| **Hardware type** | Primarily **combinational circuits** | Primarily **sequential circuits** (flip-flops/registers) |
| **Evaluation** | LHS updates immediately and is visible to the next line | RHS is evaluated at the start of the time step; LHS updates at the end |
| **Sensitivity** | Level-triggered `always` blocks or `initial` blocks | Edge-triggered `always` blocks |
| **Order dependency** | Statement order is **critical** | Statement order is **not** order-dependent for independent registers |

---

## 6. Conditional and Case Statements

- **`if-else` and ternary (`? :`):** Use `? :` for simple conditional assignments. In combinational `always` blocks, **always pair every `if` with an `else`** to avoid inferring unintended latches.
- **`casex`:** Treats both `x` and `z` bits as "don't care".
- **`casez`:** Treats `z` (and `?`) bits as "don't care", while `x` remains a distinct value.

---

## 7. Simulation and Testbenches

A **testbench** is written in the same HDL (Verilog) as the design, but uses non-synthesizable constructs to stimulate and verify the Unit Under Test (UUT):
- **No module ports:** A top-level testbench module has no external `input`/`output` port list.
- **Stimulus generation:** Uses `initial begin ... end` blocks (and clock generators) to drive UUT inputs.
- **Simulation timing:** Propagation and stimulus delays are modeled with `#<time_units>` (for example, `#10` advances simulation time by 10 time units).

---

## Related Notes
- [[finite-state-machine]]
