# Hands-on tutorial on gamma-ray astronomy for the 13th IDPASC School

Material for the gamma-ray astronomy tutorial at the [13th IDPASC school](https://indico.lip.pt/event/1710/).

## Pre-requisites
Checking beforehand [the basic usage of Astropy's coordinates](https://learn.astropy.org/tutorials/1-Coordinates-Intro.html) [and the very first part of Gammapy's maps and regions tutorial](https://docs.gammapy.org/dev/tutorials/starting/overview.html) will make easier to go throught these tutorials (it will not take more than 15 mins).


## Downlaod the data for this tutorial
Almost all the data we need for this tutorial are available in the [`gammapy-data`](https://github.com/gammapy/gammapy-data) repository.   
Download the repository and set (in your `.bashrc` or `.zshrc` file) a `GAMMAPY_DATA` evironment variable pointing to this path   
```shell
export GAMMAPY_DATA=<path to where you downloaded the gammapy-data repository>
```

we will also use some LST's Crab Nebula observations recently released to the public.   
You can download them from [zenodo](https://zenodo.org/records/11445184).   
Download the `.zip` file in this same repository and unzip it   

```shell
mkdir crab_lst_data
tar -xzvf 11445184.zip -C crab_lst_data
```

## Download and install the software for this tutorial
Download `gammapy` version `1.2` following [these instructions](https://docs.gammapy.org/1.2/getting-started/index.html#quickstart-setup).   
It is recommended to create a conda environment.

## Binder
You can run these notebooks in MyBinder, remember to download the data there though!

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cosimoNigro/13_idpasc_school_gamma_hands_on/HEAD)
