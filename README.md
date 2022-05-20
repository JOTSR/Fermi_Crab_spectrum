# Spectrum analysis of the Crab pulsar with the Fermi LAT

Construction and comparison of the theoritical and experimental SED in high energy

This repository records all the process and the tools to perform the construction and the theoritical confrontation of the spectral energy density of the Crab pulsar (J0534+2200) in a field of observation about 5° and 20° with the Fermi LAT as part of an internship in the [astroparticles research group](https://www.lp2ib.in2p3.fr/astro-neutrino/astroparticules/) at the [LP2I/CENBG](https://www.lp2ib.in2p3.fr).

## Requirements

You must have the [FermiBottle container](https://github.com/fermi-lat/FermiBottle) using [Docker](https://www.docker.com/products/docker-desktop/) and have access to [the official Fermi website](https://fermi.gsfc.nasa.gov/)


## Usage

Datas are aviable on https://fermi.gsfc.nasa.gov/ssc/data/access/

### Fast start

1. In your machine
    ```sh
    docker run -it -e HOST_USER_ID=`id -u $USER` -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v "`pwd`":/data -p 8888:8888 fssc/fermibottle su fermi -
    ```
1. In the container
    ```sh
    cd /data
    git clone https://github.com/JOTSR/Fermi_Crab_spectrum.git
    conda activate fermi
    notebook
    ```

### Full setup

1. Follow the [FermiBottle container doc](https://github.com/fermi-lat/FermiBottle/wiki)
1. Clone this project in your personal directory
1. Start conda env
    ```sh
    conda activate fermi
    ```
1. Start jupyter server in the container 
   ```sh
   notebook
   ```
1. And connect to remote server (for example with [VSCode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)).

## Analysis

All the process is detailed in the attached [notebook](./analysis.ipynb)