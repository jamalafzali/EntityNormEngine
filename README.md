# Entity Normalization Engine (ENE)

ENE takes in a stream of input samples, and tries to cluster them based off their types and their similarities.

## Usage
After instantiating the `EntNormEng()` class, we can simply call the `add_entry()` method to add a new sample.

```python
entNorm = EntNormEng()

# Add entries like this
entNorm.add_entry("12345", 'serial')
entNorm.add_entry("plastic bottle", 'good')
entNorm.add_entry("Marks and Spencers Ltd", 'company')
```
Please note that currently we must pass an additional *sample_type* input to the add_entry method. This classification will be done automatically in future. The allowed *sample_types* are as follows:
* '*serial*'
* '*good*'
* '*location*'
* '*company*'
* '*address*'

