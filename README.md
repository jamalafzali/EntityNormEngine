# Entity Normalization Engine (ENE)

ENE takes in a stream of input samples, and tries to cluster them based off their types and their similarities.

## Usage
After instantiating the `EntNormEng()` class, we can simply call the `add_entry()` method to add a new sample.

```python
entNorm = EntNormEng()

# Add entries like this
entNorm.add_entry("12345")
entNorm.add_entry("plastic bottle")
entNorm.add_entry("Marks and Spencers Ltd")
```

Please note that the `add_entry()` method can also take an additional *sample_type* argument for testing of each type's normalisation algorithm.
For example `entNorm.add_entry("Marks and Spencers", "company")`.
The allowed *sample_types* are as follows:
* '*serial*'
* '*good*'
* '*location*'
* '*company*'
* '*address*'

