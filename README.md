# Approx-pi
MT79 project about the pi number estimation

## Requirement:

py 3.5

module: matplotlib

## Usage:

### Basic usage
```bash
python approxPi.py -h
```

### functions:
there's 3 main functions on this program:
* genpi
* estimatepi
* compgraph

#### genpi function:

- Generate pi with Monte-Carlo method and depth=20
```bash
python approxPi.py genpi --method X Y
```
--method can be:
* 1 for classic method
* 2 for Imparis method
* 3 for ramanujan method
* 4 for MonteCarlo method

Y is for the depth of the generated pi.

#### estimatePi

- Search pi's 4th decimals with imparis method
```bash
python approxPi.py estimatepi --method 2 4
```

#### compgraph

- Display a graph to see convergence difference between imparis and classic
```bash
python approxPi.py compgraph 200
```
