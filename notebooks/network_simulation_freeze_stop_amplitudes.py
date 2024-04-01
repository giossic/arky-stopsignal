#Importing scripts:
import cbgt as cbgt
#from frontendhelpers import * 
#from tracetype import *
#import init_params_hyperdirect as par 
#import popconstruct_hyperdirect as popconstruct
#import qvalues as qval
#import generateepochs as gen
#import generate_stop_dataframe as gen_stop
#import generate_stop_dataframe_2 as gen_stop_2
#import generate_opt_dataframe as gen_opt
#from agentmatrixinit import *
#from agent_timestep_stop_signal import timestep_mutator, multitimestep_mutator
#import pdb
import pipeline_creation as pl_creat
import numpy as np
#import megaloop_stop_signal as ml
import plotting_functions as plt_func
import plotting_helper_functions as plt_help
import matplotlib.pyplot as plt
import pickle

def saveresults_vars(variable, prefix):
    pickle.dump(variable, open(prefix, 'wb'))
    
def loadresults_vars(prefix):
    return pickle.load(open(prefix, "rb"))


def run_simulation(seed_1, seed_2, amplitude_GPeA, amplitude_iSPN,environment): 

    data_dir = "./Data/stop-params_freeze-analysis/amplitudes/iSPN+GPeA_10threads/"
    figure_dir = "./Figures/"
    print(environment)
    
    #Create pipeline

    #Network pipeline

    seed = np.random.randint(0,99999999)
    print(environment)
    #print(seed_1)
    #print(seed_2)
    
    #np.random.seed(onset)
    print('Seed', seed)

    #Create the whole pipeline
    experimentchoice = 'stopsignal'
    number_of_choices = 1
    pl_creat.choose_pipeline(experimentchoice) 
    
    pl = pl_creat.create_main_pipeline(runloop=True)

    #Timestep loop
    #mega_l = ml.mega_loop

    #Adding the timestep loop to the main pipeline
    #pl.add(mega_l)

    plt.rcParams["figure.facecolor"] = "w"
    
    #Running the pipeline

    results = cbgt.ExecutionManager(cores=7).run([pl]*10,[environment]*10)
    
    datatables = cbgt.collateVariable(results,'datatables')
    popfreqs = cbgt.collateVariable(results, 'popfreqs')
   
    cbgt.saveResults(results, data_dir+'network_data_GPeA_'+str(np.round(amplitude_GPeA, 1))+'_iSPN_'+str(np.round(amplitude_iSPN, 1)),['popfreqs','popdata', 'datatables'])
    
    return results
