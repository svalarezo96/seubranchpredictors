# BranchPredictorsAnalysis
Project for EE801 class


Implemetation in python of the following prediction methods:

* TAGE
* gshare
* bimodal

and prints performance information.

Trace file format is the PC address of the conditional branch instruction followed by the branch itself:

```
40d81e 1
40d81e 1
40d81e 0
40d81e 0
```

## Usage

The script `main.py` contains the simulation of the bimodal and gshare branch predictors.
The script `main_tage.py` contains the simulation of the tage branch predictors.
In order to inyect errors you should define the variables `activate_error_bit0` and `activate_error_bit1` in the function getPredictionFromCounter().

### Notices

The TAGE predictor is implemented with only 3 tables.
