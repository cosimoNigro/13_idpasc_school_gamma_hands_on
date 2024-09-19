# Hands-on tutorial on gamma-ray astronomy for the 13th IDPASC School

Material for the gamma-ray astronomy tutorial at the 13th IDPASC school.

## Downlaod the data for this tutorial

Almost all the data we need for this tutorial are available in the `gammapy-data` repository.   
Download the repository and set a `GAMMAPY_DATA` evironment variable pointing to this path   
```shell
export GAMMAPY_DATA=<path to where you downloaded the gammapy-data repository>
```

we will also use some LST's Crab Nebula observations recently released to the public.   
You can download them from [zenodo](https://zenodo.org/records/11445184).   
Download the `.zip` file in this reposity and unzip it   

```shell
mkdir crab_lst_data
tar -xzvf 11445184.zip -C crab_lst_data
```

## Download and install the software for this tutorial

Download `gammapy` version `1.2` following [these instructions](https://docs.gammapy.org/1.2/getting-started/index.html#quickstart-setup).   
It is recommended to create a conda environment.
