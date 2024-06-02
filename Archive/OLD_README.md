# L(ocality) S(ensitive) V(oronoi) F(ilter)

A take on LSH, resulting in a "Voronoi"-like topology with filtering and other techniques applied from FALCONN++

## LSH Research

This repo contains data and queries from the SISAP 2023 indexing challenge https://sisap-challenges.github.io/

Requires python 3.10 or later (for int.bit_count() function)

## TODO

- [X] Check bucket sizes
  - [X] Min, Max and std. dev
  - [X] Histogram
- [X] Check amount of buckets
- [X] Make parameters align
- [X] Time different parts of the algorithm
  - [X] Builds
    - [X] Generate hashes
    - [X] Hash data to buckets
  - [X] Query
    - [X] Hash query points
    - [X] Retrieve bucket of data
    - [X] Calculate n-nearest from bucket
- [X] Look into the comparison
  - [X] We compare using indicies, but the distance from a query point to 2+ points could be the same, but have different indicies, warping the perceived recall % (Counting a correct answer as a wrong answer)
- [X] Run in github Actions
  - [ ] Generate results other than console prints
- [X] Look into using more numpy in general
  - [X] Specifically the "BinaryPoints" type so we eliminate the strings
- [X] Implement LSF in terms of binary hamming space
- [ ] Implement multi-probing
- [ ] Do embedding onto unit-sphere
  - [ ] Allowing for Cross-polytope LSH
- [X] Name the algorithm
- [ ] Combination buckets

# Possible Goals
- [ ] Test on multi-threaded environment
- [ ] 1 Million dataset
- [ ] 10 Million dataset
- [ ] 100 Million dataset
- [ ] Translate to C++
  - [ ] Use SIMD

# Prioritized
- [ ] Embedding + falconn++
- [ ] Cutaway inside buckets
- [ ] Related works study
- [ ] Theoretical foundations

- [ ] Combinatorics
- [ ] Larger datasets
- [ ] Multi-probing

# Notes for writing
- [ ] Pseudo algorithm
- [ ] Theoretical questions
- [ ] Related work
  - [ ] Look into the entire design space and approaches
- [ ] Experiment with x,y 0-D and plot distance (full run through the LSH)