# Independent numerical validation

Computed directly from the repository CSV using Python, pandas, NumPy, and SciPy. This is independent numerical evidence, not a SAS execution log. Reproduce with `python -m pip install -r validation/requirements.txt` then `python validation/check_results.py`.

```text
Total: 27802
Female affirmative proportion: 0.6902447200804559
Male affirmative proportion: 0.2504849848684721
Pearson chi-square: 5351.939661699363 df: 1 p: 0.0
Expected counts: [[7254.71350982 7660.28649018]
 [6268.28649018 6618.71350982]]
Relative risk Female/Male: 2.755633118858995
95% log-Wald RR CI: [2.66953822 2.84450465]
```
