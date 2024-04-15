# Arkypallidal neurons in the external globus pallidus can mediate inhibitory control by altering competition in the striatum
#### C. Giossi, J. Bahuguna, J. E. Rubin, T. Verstynen and C. Vich 

ABSTRACT: Reactive inhibitory control is crucial for survival. Traditionally, this control in mammals was attributed solely to the hyperdirect pathway, with cortical control signals flowing unidirectionally from the subthalamic nucleus (STN) to basal ganglia output regions. Yet recent findings have put this model into question, suggesting that the STN is assisted in stopping actions through ascending control signals to the striatum mediated by the external globus pallidus (GPe). Here we investigate this suggestion by harnessing a biologically-constrained spiking model of the cortico-basal ganglia-thalamic (CBGT) circuit that includes pallidostriatal pathways originating from arkypallidal neurons. Through a series of experiments probing the interaction between three critical inhibitory nodes (the STN, arkypallidal cells, and indirect pathway spiny projection neurons), we find that the GPe acts as a critical mediator of both ascending and descending inhibitory signals in the CBGT circuit. In particular, pallidostriatal pathways regulate this process by weakening the direct pathway dominance of the evidence accumulation process driving decisions, which increases the relative suppressive influence of the indirect pathway on basal ganglia output. These findings delineate how pallidostriatal pathways can facilitate action cancellation by managing the bidirectional flow of information within CBGT circuits.


# Below are the instructions to create a conda environment, install all the dependencies required to run CBGTPy and run notebooks.

## Dependencies.
   * Python 3.8+ (This only needs attention if the user is using Python version < 3, e.g. 2.7. In case, Python version > 3 is been used, the installation script will install the correct version of Python and other dependencies)
   * gcc (already installed in Linux by default, but not in Mac)
   * Xcode (Mac users)
   * CLT  (Mac users)

Xcode and CLT (for Mac users) can be installed by running this on the command line:
   
   	$ xcode-select --install
   
gcc (for Mac users) can be installed by running this on commad line:

     	$ brew install gcc


## Install conda on your machine.
* Download from here https://docs.conda.io/projects/miniconda/en/latest/
	
* Change the directory to where the executable file was downloaded:

  		$ cd <directory where executable was downloaded>
  	
* In the directory, where the executable file (eg. Miniconda3-latest-MacOSX-x86_64.sh) is downloaded, type the following on your command line:

	* Mac
 
			$ bash Miniconda3-latest-MacOSX-x86_64.sh
 	* Linux
  
   			$ bash Miniconda3-latest-Linux-x86_64.sh


## Download arky-stopsignal-main folder.
	
 	$  git clone https://github.com/CoAxLab/CBGTPy.git

 * Change the directory:

		$ cd CBGTPy
  	

## Create a conda environment by typing the following on the command line. Choose an environment name, e.g. cbgtpy_env.
	$ conda create -n <env name> python=3.8 pyyaml
	
E.g., if the <env name> is "cbgtpy_env", then use:
 
	$ conda create -n cbgtpy_env python=3.8 pyyaml
 
## Activate the conda environment.
	$ conda activate cbgtpy_env
 or 
  	
   	$ source activate cbgtpy_env
   
## Run the installation file. 

You will be asked which multiprocessing library you want to install. Although "ray" is the recommended version, it may cause problems on some machines.
Hence CBGTPy is designed to use the default Python multiprocessing APIs, that need a third-party library (pathos). Pathos is installed by default. 
You can choose to install ray by typing "y" to the prompted question. If "n" is typed, ray will not be installed. 
Some basic benchmarking for the three options - (a) no multiprocessing (b) with pathos (c) with ray - are stated below.
	
* For 5 simulations, 3 trials each on an Apple M1 machine with OS Ventura 13.2.1:
 (a) none: 664s; (b) pathos: 331s; (c) ray:  266s.
  	
* For 5 simulations, 3 trials each on a 11th Gen Intel Core(TM) i7-11800H with Windows 10:
 (a) none: 525s; (b) pathos: 386s; (c) ray: 232s.

		$ python install.py <env name>

	* For the environment name cbgtpy_env:

  			$ python install.py cbgtpy_env
 
## Test by running:
	$ ipython

* On the ipython prompt:

 		$ import pathos

## If there is an error, deactivate and activate the conda environment again.

## If you plan to use "ray", start the ray server as described below. If not, skip this step.
* On the shell prompt:

		$ ray start --head --port=6379 --redis-password="cbgt2"
  
* The above line should be sufficient to start the ray server. In case is not, it would give back the machine IP. The machine IP could be used in the following command:

  		$ ray start --address='< machine ip>:6379' --redis-password='cbgt2'
    
  For e.g. for IP 192.168.1.167:

  		$ ray start --address='192.168.1.167:6379' --redis-password='cbgt2'



## From the shell prompt, start jupyter notebooks. There are three example notebooks provided which can be executed from the jupyter notebook environment.
* network_simulation-n-choice.ipynb (Runs a n-choice task)
* network_simulation-stop-signal.ipynb (Runs a stop-signal task)
* network_simulation-n-choice-optostim.ipynb (Shows an example of optogenetic stimulation during a n-choice task)
 
		$ jupyter-notebook 
 	
  	or
  		
        	$ jupyter notebook

## If the libraries pathos and ray are not still visible (gives an error saying they are not found) in the jupyter notebook, then execute these commands at the beginning of the notebook.
	
        import sys
	import yaml
	with open('environment.yml') as f:
	    doc = yaml.safe_load(f)
	    
	sys.path.append(doc['prefix']+"/lib/python3.8/site-packages/")

## Only if you want to delete the conda environment !!!
	$ conda remove --name cbgtpy_env --all
