# LSH Research

This repo contains data and queries from the SISAP 2023 indexing challenge https://sisap-challenges.github.io/

Requires python 3.10 or later (for int.bit_count() function)

# TODO

- [X] Check bucket sizes
  - [X] Min, Max and std. dev
  - [X] Histogram
- [X] Check amount of buckets
- [X] Make parameters align
- [ ] Time different parts of the algorithm
  - [ ] Builds
    - [ ] Generate hashes
  - [ ] Query
    - [ ] Hash query points
    - [ ] Retrieve bucket of data
    - [ ] Calculate n-nearest from bucket
- [X] Look into the comparison
  - [X] We compare using indicies, but the distance from a query point to 2+ points could be the same, but have different indicies, warping the perceived recall % (Counting a correct answer as a wrong answer)
- [X] Run in github Actions
  - [ ] Generate results other than console prints
- [ ] Look into using more numpy in general
  - [ ] Specifically the "BinaryPoints" type so we eliminate the strings
- [ ] Implement LSF in terms of binary hamming space
- [ ] Implement multi-probing

# Possible Goals
- [ ] Test on multi-threaded environment
- [ ] 1 Million dataset
- [ ] 10 Million dataset
- [ ] 100 Million dataset
- [ ] Translate to C++
  - [ ] Use SIMD