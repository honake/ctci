# Editorial

## Bit Manipulation: Lonely Integer

### XOR
XOR forms an Abelian Group as it has the following properties.

* Commutativity: A xor B = B xor A
* Associativity: (A xor B) xor C = A xor (B xor C)
* Identity exists: there is a bit string, 0, (of length N) such that A xor 0 = A for any A
* Each element is its own inverse: for each A, A xor A = 0.

## DP: Coin Change

### Tips
Use `grid[row][column]` rather than `grid[x][y]` as it is confusing.
