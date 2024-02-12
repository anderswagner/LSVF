# LSH Research

This repo contains data and queries from the SISAP 2023 indexing challenge https://sisap-challenges.github.io/

Requires python 3.10 or later (for int.bit_count() function)

# TODO

- [X] Check bucket sizes
  - [ ] Min, Max and std. dev
  - [ ] Histogram
- [X] Check amount of buckets
- [X] Make parameters align
- [ ] Time different parts of the algorithm
  - [ ] Builds
    - [ ] Generate hashes
  - [ ] Query
    - [ ] Hash query points
    - [ ] Retrieve bucket of data
    - [ ] Calculate n-nearest from bucket
- [ ] Look into the comparison
  - [ ] We compare using indicies, but the distance from a query point to 2+ points could be the same, but have different indicies, warping the perceived recall % (Counting a correct answer as a wrong answer)
- [ ] Run in github Actions
  - [ ] Generate results other than console prints

# End Goals
- [ ] Implement LSF
- [ ] Implement multi-probing
- [ ] Test on multi-threaded environment
- [ ] 1 Million dataset
- [ ] 10 Million dataset
- [ ] 100 Million dataset
- [ ] Translate to C++
  - [ ] Use SIMD