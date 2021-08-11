# Multipath Offloading Simulator

This code performs the simulations for the experiments relative to the paper Multipath Computation Offloading for Mobile Augmented Reality

## Getting Started

### Prerequisites

Run the code in a virtual environment with the following dependencies:

* python 3 (Tested with Python 3.7)
* numpy 1.17.2 
* matplotlib 3.1.1 

```
    $ virtualenv --python=python3 venv
    $ source venv/bin/activate
    $ pip install numpy matplotlib
```

### Run the code

All simulations are contained in a file named main_*.py as follows;

* Figure 9: main_all.py
* Figure 10a and 10c: main_wifi_delay.py
* Figure 10b and 10d: main_wifi_bandwidth.py
* Figure 11: main_random.py
* Figure 12a and 12c: main_random_wifi_delay.py
* Figure 12b and 12d: main_random_wifi_latency.py
* Figure 13: main_5g.py

Run the corresponding file as follows:

```
    $ python main.py
```

The code will generate Figures in figs/

## Code structure

Configuration files are stored in the configs/ directory. Files named main_*.py
run the experiments. Figures are stored in figs/. Outputs will be saved in .txt files of their corresponding .py files. 
The code structure is as follows:

```
./
├── configs -> Contains the configuration files for all experiments
│   ├── config_5g -> Figure 13
│   ├── config_all -> Figure 9
│   ├── config_random -> Figure 11
│   ├── config_random_wifi_bandwidth -> Figures 12a and 12c
│   ├── config_random_wifi_delay -> Figures 12b and 12d
│   ├── config_single
│   ├── config_wifi_bandwidth -> Figures 10b and 10d
│   └── config_wifi_delay -> Figures 10a and 10c
├── figs -> Figures are stored here
├── __init__.py
├── LICENSE
├── main_5g.py -> Figure 13
├── main_all.py -> Figure 9
├── main_random.py -> Figure 11
├── main_random_wifi_bandwidth.py -> Figures 12a and 12c
├── main_random_wifi_delay.py -> Figures 12b and 12d
├── main_single.py 
├── main_wifi_bandwidth.py -> Figures 10b and 10d
├── main_wifi_delay.py -> Figures 10a and 10c
├── README
├── sim -> Simulator code
│   ├── intermittentlink.py
│   ├── link.py
│   ├── randomlink.py
│   ├── server.py
│   ├── simulator.py
│   ├── statistics.py
│   └── task.py
```



