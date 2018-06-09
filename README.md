# Rubiks

The file `rubiks.py` provides an interpreter for evaluating Rubik's cube permutations. It takes no command-line options. The interpreter prints the results of cube permutations in [cycle decomposition form](https://en.wikipedia.org/wiki/Permutation#Cycle_notation). Input to the interpreter should be in standard [Rubik's cube notation](https://www.speedsolving.com/wiki/index.php/3x3x3_notation), not including cube rotations or multiple-layer turns.

For example:

```
> DFDFDF
(uf dr lf df dl rf db)(drb urf ldb frd ufl)
> ESE'S'
(b l d)(f r u)
> R2U2
(uf ub)(drb ulb urf)(dfr ufl ubr)(dr ul ur)(fr br)
> exit()
```

I owe my understanding of the group theory of the Rubik's cube to [this reading](http://www.math.harvard.edu/~jjchen/docs/Group%20Theory%20and%20the%20Rubik's%20Cube.pdf).

## Requirements

Python 3