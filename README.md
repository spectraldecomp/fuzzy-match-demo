# fuzzy-match-demo
Fuzzy matching search on thousands of company records. 

### Known Bugs
* Resulting sorted lists are not always max length; some data gets dropped.
* Fuzzy search is not perfect, may need to tweak the scorer.
* Data needs more defined cutoff points for clearer output.

Be sure to `pip install python-Levenshtein`.
