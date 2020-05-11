================================================================================

# Reproduction of results with swedish modifications
This repository has the same content as the Imperial College covid19model 

https://github.com/ImperialCollegeLondon/covid19model/tree/144356c4dc487ed7f42fa86bc6f2210c6399ecc7

with the addition of the file covariate-size-effects.r that can be used to produce the covariate plot as 

```
Rscript covariate-size-effects.r <base-XXX-stanfit.Rdata>
```

where XXX is replaced with the number of your file (located in the results folder after the code have been run).

This README only differs by this first section. 
Follow the instructions for later versions to set up the environment required to run the code.

================================================================================

# covid19model
Code for modelling estimated deaths and cases for COVID19. 

This repository has code for replication purposes. The bleeding edge code and advancements are done in a private repository. Ask report authors for any collaborations. 
