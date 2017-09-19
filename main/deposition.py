#!/usr/bin/python

# DEPOSITION

########## HERE IS THE INITIAL SECTION OF PROGRAM HEADER CLASS ##########
# PROGRAM TITLE
  # Sediment Transport & Erosion Prediction

# PROGRAM DESCRIPTION
  # STEP was initiated by Jenderal Soedirman University, a research university of technology located in Indonesia in 2017.
  # STEP is an open-source project use for computing and predict the amount of sediment transport.
  # This program has been tested and should work on almost all Python 3.6 compilers.
  # Feel free to use the source code on your system.

# LOAD HEADER & MODULES

  ### LOADING HEADER ###
  # Header is used for giving information about title and the version of the program

'''
import pyfiglet
pyfiglet.print_figlet("STEP",font="lean",justify="center")
pyfiglet.print_figlet("Sediment Transport & Erosion Prediction",font="digital",justify="center")
version = " Version x.x.x ";
print("{1:^75}".format(" ",version))
'''
      
  ### LOADING MODULES ###
  # After the packages has been satisfied by running setup.py, then import the modules and the alias by running the script below:
    
import glob, os, os.path, shutil, itertools, re, sys, time, threading, pandas as pd, numpy as np
from numpy.polynomial import Polynomial as P
from itertools import zip_longest, groupby, islice
from functools import reduce
from operator import mul
import math
np.set_printoptions(suppress=True, threshold=np.inf, linewidth=np.inf) # Handling output mode and turn scientific mode off, summarization and line-wrapping
  
  # Disabled modules: pickle, chain, csv, ctypes, collections, pprint, from io import StringIO        

# IMPORT LOCAL AND GLOBAL LISTS

  ### IMPORT LOCAL LISTS ###
  # Import lists of path from local file

floc_local = glob.glob('../input/parameter/local*.*') # Load local file contents
cols_local = [0,1] # Read row and column index of local file

  # Read certain columns with Pandas Module

df_local = pd.DataFrame()
for f_local in floc_local:
    df_local = df_local.append(pd.read_csv
                               (f_local, delimiter='\s+', header=None, usecols=cols_local, na_values=['']),
                               ignore_index=True)
arr_local = df_local.values
  
  ### IMPORT GLOBAL LISTS ###
  # Import lists of path from global file
   
floc_global = glob.glob('../input/parameter/global*.*') # Load global file contents
cols_global = [0,1] # Read row and column index of global file

  # Read certain columns with Pandas Module

df_global = pd.DataFrame()
for f_global in floc_global:
    df_global = df_global.append(pd.read_csv
                                 (f_global, delimiter='\s+', header=None, usecols=cols_global, na_values=[''], skiprows=1),
                                 ignore_index=True)    
arr_global = df_global.values
########## HERE IS THE LAST SECTION OF PROGRAM HEADER CLASS ##########



########## HERE IS THE INITIAL SECTION OF DEPOSITION CLASS ##########
# DEPOSITION

  # Deposition = Epsilon x Settling Velocity x Sediment Concentration
  
  # Epsilon coefficient depends on the properties of fluida
  # Settling velocity also called the "fall velocity" or "terminal velocity"
  # Sediment concentration depends on the outout of runoff or overflow VIC fluxes
########## HERE IS THE INITIAL SECTION OF DEPOSITION DATA INPUT CLASS ##########
# RUNOFF

  # Change work directory into input runoff folder
  
runoff_from_main = "../input/runoff/"
fluxes_from_runoff = "../../output/deposition/tempfiles/q/"
main_from_fluxes = "../../../../main/"
os.chdir(runoff_from_main)

 # Remove header and copy the fluxes files into output folder

for fn_fluxes in os.listdir("."):
    with open(fn_fluxes,"r") as f:
        lines_after_6 = f.readlines()[6:]
    with open(fluxes_from_runoff+fn_fluxes,"w") as writefluxes:
        writefluxes.writelines(lines_after_6)

  # Select column no.6 as runoff or overflow 

os.chdir(fluxes_from_runoff)
for file_fluxes in os.listdir("."):
    with open(file_fluxes,"r") as content_fluxes:
        string_fluxes = str(content_fluxes.read().split())
        rplce_str1 = string_fluxes.replace("'","")
        splitby = rplce_str1.split(",")
        list_flxs = list(splitby)
        shorted_flxs = list_flxs[5::11]
        shorted_years = list_flxs[0::11]
        reverse_years = str(shorted_years)
        rplce_str2_years = reverse_years.replace("['","")
        rplce_str3_years = rplce_str2_years.replace("']","")
        rplce_str4_years = rplce_str3_years.replace("[","")
        rplce_str5_years = rplce_str4_years.replace("', ' "," ")
        list_years = rplce_str5_years.split()
        shorted_months = list_flxs[1::11]
        reverse_months = str(shorted_months)
        rplce_str2_months = reverse_months.replace("['","")
        rplce_str3_months = rplce_str2_months.replace("']","")
        rplce_str4_months = rplce_str3_months.replace("[","")
        rplce_str5_months = rplce_str4_months.replace("', ' "," ")
        list_months = rplce_str5_months.split()
        shorted_days = list_flxs[2::11]
        reverse_days = str(shorted_days)
        rplce_str2_days = reverse_days.replace("['","")
        rplce_str3_days = rplce_str2_days.replace("']","")
        rplce_str4_days = rplce_str3_days.replace("[","")
        rplce_str5_days = rplce_str4_days.replace("', ' "," ")
        list_days = rplce_str5_days.split()
        reverse_flxs = str(shorted_flxs)
        rplce_str2 = reverse_flxs.replace("[' ","")
        rplce_str3 = rplce_str2.replace("']","")
        new_line_flxs = rplce_str3.replace("', ' ","\n")
        with open(file_fluxes,"w") as output_flow:
            output_flow.writelines(new_line_flxs)

  # Read the runoff data as a variable

runoff = list()
for file_fluxes in os.listdir("."):
    with open(file_fluxes) as content_runoff:
        read_content_runoff = list((content_runoff.read()).split())
        scalar_array_runoff = np.array(0.0000000000000115740740740741, dtype = float)
        array_content_runoff = np.array(read_content_runoff, dtype = float)
        runoff_result = array_content_runoff * scalar_array_runoff
        value_runoff = runoff_result.tolist()
        runoff.append(value_runoff)
os.chdir(main_from_fluxes)

# EPSILON

  # Change work directory into gll

gll_from_main = "../output/erosion/tempfiles/gll/"
epsilon_from_e = "../../../../input/epsilon/"
e_from_gll = "../../../deposition/tempfiles/e/"
splasherosion_from_e = "../../../erosion/splasherosion/"
main_from_e = "../../../../main/"

'''
  # Copy gll file into output temporary files for deposition (/output/deposition/tempfiles/e/)

os.chdir(gll_from_main)
srcp_gllfe = "."
destp_gllfe = e_from_gll
srcf_gllfe = os.listdir(srcp_gllfe)
for fl_gllfe in srcf_gllfe:
    if fl_gllfe.startswith("fl_"):
        f_gllfe = os.path.join(srcp_gllfe, fl_gllfe)
        if (os.path.isfile(f_gllfe)):
            shutil.copy(f_gllfe, destp_gllfe)

  # Give the whitespace after axis-ordinat and create epsilon.txt into input folder

os.chdir(e_from_gll)
with open("fl_fngll.txt") as epsilon_grid_axisordinat:
    gao_e = str(epsilon_grid_axisordinat.read().split(","))
    gaoe_new = gao_e.replace("\\n"," \n")
    gaoe_new = gaoe_new.replace("['","")
    gaoe_new = gaoe_new.replace("']","")
    with open(epsilon_from_e+"epsilon.txt","w") as inp_gaoe:
        inp_gaoe.writelines(gaoe_new)
  
  # Show pop up dialog to user for filling epsilon coefficient

print("\nPlease fill the Epsilon coefficient in Epsilon directory!")
question_epsilon = input("\nIf You have already completed it, Press Y to continue or press N to exit! ")
if question_epsilon.lower().startswith("y"):
    print("\nPlease wait a moment...")
elif question_epsilon.lower().startswith("n"):
    exit()
elif question_epsilon.lower().startswith(""):
    print("\nERROR-UIEPS\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Epsilon coefficient.\n")
    print("If in a grid the value is not avaliable just type 0.")
    exit()
'''

  ### Copy epsilon file into output temporary files for deposition (/output/deposition/tempfiles/e) ###

os.chdir(gll_from_main)
os.chdir(e_from_gll)
srcp_epsilon = epsilon_from_e
destp_epsilon = "."
srcf_epsilon = os.listdir(srcp_epsilon)
for fl_epsilon in srcf_epsilon:
    f_epsilon = os.path.join(srcp_epsilon, fl_epsilon)
    if (os.path.isfile(f_epsilon)):
        shutil.copy(f_epsilon, destp_epsilon)
 
  # Save file's contents into variable

epsilon = list()
for varlst_epsilon in os.listdir("."):
    if varlst_epsilon.startswith("epsilon"):
        rvarlst_epsilon = open(varlst_epsilon,"r")
        rcvarlst_epsilon = str(rvarlst_epsilon.read())
        rrowvarlst_epsilon = rcvarlst_epsilon.split()
        epsilon.append(rrowvarlst_epsilon) 
    
  # Check if User has already filled every single epsilon coefficient
  # Save the value into a variable list 'value_epsilon'

split_epsilon = ((str(epsilon)).split())
if len(split_epsilon) == 2*(len([name for name in os.listdir(splasherosion_from_e) if os.path.isfile(os.path.join(splasherosion_from_e, name))])):
    for e in epsilon:
        complist_epsilon = [e[x:x+2] for x in range(0, len(e), 2)]
        dict_epsilon = dict(complist_epsilon)
        value_epsilon = list(dict_epsilon.values())
else:
    print("ERROR-UIEPS\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Epsilon coefficient.\n")
    print("If in a grid the value is not avaliable just type 0.")
    exit()
os.chdir(main_from_e)

# SPECIFIC WEIGHT OF SEDIMENT

  # Change work directory into gll

gll_from_main = "../output/erosion/tempfiles/gll/"
gammas_from_gs = "../../../../input/gammas/"
gs_from_gll = "../../../deposition/tempfiles/gs/"
main_from_gs = main_from_e

'''
  # Copy gll file into output temporary files for deposition (/output/deposition/tempfiles/gs/)

os.chdir(gll_from_main)
srcp_gllfgs = "."
destp_gllfgs = gs_from_gll
srcf_gllfgs = os.listdir(srcp_gllfgs)
for fl_gllfgs in srcf_gllfgs:
    if fl_gllfgs.startswith("fl_"):
        f_gllfgs = os.path.join(srcp_gllfgs, fl_gllfgs)
        if (os.path.isfile(f_gllfgs)):
            shutil.copy(f_gllfgs, destp_gllfgs)

  # Give the whitespace after axis-ordinat and create gammas.txt into input folder

os.chdir(gs_from_gll)
with open("fl_fngll.txt") as gammas_grid_axisordinat:
    gao_gs = str(gammas_grid_axisordinat.read().split(","))
    gaogs_new = gao_gs.replace("\\n"," \n")
    gaogs_new = gaogs_new.replace("['","")
    gaogs_new = gaogs_new.replace("']","")
    with open(gammas_from_gs+"gammas.txt","w") as inp_gaogs:
        inp_gaogs.writelines(gaogs_new)
  
  # Show pop up dialog to user for filling gammas coefficient

print("\nPlease fill the Specific Weight of the Sediment in Gammas directory!")
question_gammas = input("\nIf You have already completed it, Press Y to continue or press N to exit! ")
if question_gammas.lower().startswith("y"):
    print("\nPlease wait a moment...")
elif question_gammas.lower().startswith("n"):
    exit()
elif question_gammas.lower().startswith(""):
    print("\nERROR-UIGS\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Gammas coefficient.\n")
    print("If in a grid the value is not avaliable just type 0.")
    exit()
'''
    
  ### Copy gammas file into output temporary files for deposition (/output/deposition/tempfiles/gs) ###

os.chdir(gll_from_main)
os.chdir(gs_from_gll)
srcp_gammas = gammas_from_gs
destp_gammas = "."
srcf_gammas = os.listdir(srcp_gammas)
for fl_gammas in srcf_gammas:
    f_gammas = os.path.join(srcp_gammas, fl_gammas)
    if (os.path.isfile(f_gammas)):
        shutil.copy(f_gammas, destp_gammas)
 
  # Save file's contents into variable

gammas = list()
for varlst_gammas in os.listdir("."):
    if varlst_gammas.startswith("gammas"):
        rvarlst_gammas = open(varlst_gammas,"r")
        rcvarlst_gammas = str(rvarlst_gammas.read())
        rrowvarlst_gammas = rcvarlst_gammas.split()
        gammas.append(rrowvarlst_gammas) 
    
  # Check if User has already filled every single gammas coefficient
  # Save the value into a variable list 'value_gammas'

gamma = 1000.0
split_gammas = ((str(gammas)).split())
if len(split_gammas) == 2*(len([name for name in os.listdir(splasherosion_from_e) if os.path.isfile(os.path.join(splasherosion_from_e, name))])):
    for gs in gammas:
        complist_gammas = [gs[x:x+2] for x in range(0, len(gs), 2)]
        dict_gammas = dict(complist_gammas)
        value_gammas = list(dict_gammas.values())
        for vgs in value_gammas:
            if float(vgs) > float(gamma):
                pass
            elif float(vgs) < float(gamma):
                print("ERROR-UIGS\n\nYour gamma sediment value is less than gamma water")
                exit()
else:
    print("ERROR-UIGS\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Gammas coefficient.\n")
    print("If in a grid the value is not avaliable just type 0.")
    exit()
os.chdir(main_from_gs)

# VISCOSITY

  # Change work directory into gll

gll_from_main = "../output/erosion/tempfiles/gll/"
viscosity_from_v = "../../../../input/viscosity/"
v_from_gll = "../../../deposition/tempfiles/v/"
main_from_v = main_from_e

'''
  # Copy gll file into output temporary files for deposition (/output/deposition/tempfiles/v/)

os.chdir(gll_from_main)
srcp_gllfv = "."
destp_gllfv = v_from_gll
srcf_gllfv = os.listdir(srcp_gllfv)
for fl_gllfv in srcf_gllfv:
    if fl_gllfv.startswith("fl_"):
        f_gllfv = os.path.join(srcp_gllfv, fl_gllfv)
        if (os.path.isfile(f_gllfv)):
            shutil.copy(f_gllfv, destp_gllfv)

  # Give the whitespace after axis-ordinat and create viscosity.txt into input folder

os.chdir(v_from_gll)
with open("fl_fngll.txt") as viscosity_grid_axisordinat:
    gao_v = str(viscosity_grid_axisordinat.read().split(","))
    gaov_new = gao_v.replace("\\n"," \n")
    gaov_new = gaov_new.replace("['","")
    gaov_new = gaov_new.replace("']","")
    with open(viscosity_from_v+"viscosity.txt","w") as inp_gaov:
        inp_gaov.writelines(gaov_new)
  
  # Show pop up dialog to user for filling viscosity coefficient

print("\nPlease fill the Viscosity in viscosity directory!")
question_viscosity = input("\nIf You have already completed it, Press Y to continue or press N to exit! ")
if question_viscosity.lower().startswith("y"):
    print("\nPlease wait a moment...")
elif question_viscosity.lower().startswith("n"):
    exit()
elif question_viscosity.lower().startswith(""):
    print("\nERROR-UIV\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the viscosity coefficient.\n")
    print("If in a grid the value is not avaliable just type 0.")
    exit()
'''
    
  ### Copy viscosity file into output temporary files for deposition (/output/deposition/tempfiles/v) ###

os.chdir(gll_from_main)
os.chdir(v_from_gll)
srcp_viscosity = viscosity_from_v
destp_viscosity = "."
srcf_viscosity = os.listdir(srcp_viscosity)
for fl_viscosity in srcf_viscosity:
    f_viscosity = os.path.join(srcp_viscosity, fl_viscosity)
    if (os.path.isfile(f_viscosity)):
        shutil.copy(f_viscosity, destp_viscosity)
 
  # Save file's contents into variable

viscosity = list()
for varlst_viscosity in os.listdir("."):
    if varlst_viscosity.startswith("viscosity"):
        rvarlst_viscosity = open(varlst_viscosity,"r")
        rcvarlst_viscosity = str(rvarlst_viscosity.read())
        rrowvarlst_viscosity = rcvarlst_viscosity.split()
        viscosity.append(rrowvarlst_viscosity) 
    
  # Check if User has already filled every single viscosity coefficient
  # Save the value into a variable list 'value_viscosity'

split_viscosity = ((str(viscosity)).split())
if len(split_viscosity) == 2*(len([name for name in os.listdir(splasherosion_from_e) if os.path.isfile(os.path.join(splasherosion_from_e, name))])):
    for v in viscosity:
        complist_viscosity = [v[x:x+2] for x in range(0, len(v), 2)]
        dict_viscosity = dict(complist_viscosity)
        value_viscosity = list(dict_viscosity.values())
else:
    print("ERROR-UIV\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the viscosity coefficient.\n")
    print("If in a grid the value is not avaliable just type 0.")
    exit()
os.chdir(main_from_v)

# AVERAGE SEDIMENT DIAMETER

  # Change work directory into gll

gll_from_main = "../output/erosion/tempfiles/gll/"
diameter_from_ds = "../../../../input/diameter/"
ds_from_gll = "../../../deposition/tempfiles/ds/"
main_from_ds = main_from_e

'''
  # Copy gll file into output temporary files for deposition (/output/deposition/tempfiles/ds/)

os.chdir(gll_from_main)
srcp_gllfds = "."
destp_gllfds = ds_from_gll
srcf_gllfds = os.listdir(srcp_gllfds)
for fl_gllfds in srcf_gllfds:
    if fl_gllfds.startswith("fl_"):
        f_gllfds = os.path.join(srcp_gllfds, fl_gllfds)
        if (os.path.isfile(f_gllfds)):
            shutil.copy(f_gllfds, destp_gllfds)

  # Give the whitespace after axis-ordinat and create diameter.txt into input folder

os.chdir(ds_from_gll)
with open("fl_fngll.txt") as diameter_grid_axisordinat:
    gao_ds = str(diameter_grid_axisordinat.read().split(","))
    gaods_new = gao_ds.replace("\\n"," \n")
    gaods_new = gaods_new.replace("['","")
    gaods_new = gaods_new.replace("']","")
    with open(diameter_from_ds+"diameter.txt","w") as inp_gaods:
        inp_gaods.writelines(gaods_new)
  
  # Show pop up dialog to user for filling diameter coefficient

print("\nPlease fill the Average of Sediment Diameter in diameter directory!")
question_diameter = input("\nIf You have already completed it, Press Y to continue or press N to exit! ")
if question_diameter.lower().startswith("y"):
    print("\nPlease wait a moment...")
elif question_diameter.lower().startswith("n"):
    exit()
elif question_diameter.lower().startswith(""):
    print("\nERROR-UID\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the diameter coefficient.\n")
    print("If in a grid the value is not avaliable just type 0.")
    exit()
'''
    
  ### Copy diameter file into output temporary files for deposition (/output/deposition/tempfiles/ds) ###

os.chdir(gll_from_main)
os.chdir(ds_from_gll)
srcp_diameter = diameter_from_ds
destp_diameter = "."
srcf_diameter = os.listdir(srcp_diameter)
for fl_diameter in srcf_diameter:
    f_diameter = os.path.join(srcp_diameter, fl_diameter)
    if (os.path.isfile(f_diameter)):
        shutil.copy(f_diameter, destp_diameter)
 
  # Save file's contents into variable

diameter = list()
for varlst_diameter in os.listdir("."):
    if varlst_diameter.startswith("diameter"):
        rvarlst_diameter = open(varlst_diameter,"r")
        rcvarlst_diameter = str(rvarlst_diameter.read())
        rrowvarlst_diameter = rcvarlst_diameter.split()
        diameter.append(rrowvarlst_diameter) 
    
  # Check if User has already filled every single diameter coefficient
  # Save the value into a variable list 'value_diameter'

split_diameter = ((str(diameter)).split())
if len(split_diameter) == 2*(len([name for name in os.listdir(splasherosion_from_e) if os.path.isfile(os.path.join(splasherosion_from_e, name))])):
    for ds in diameter:
        complist_diameter = [ds[x:x+2] for x in range(0, len(ds), 2)]
        dict_diameter = dict(complist_diameter)
        value_diameter = list(dict_diameter.values())
else:
    print("ERROR-UID\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the diameter coefficient.\n")
    print("If in a grid the value is not avaliable just type 0.")
    exit()
os.chdir(main_from_ds)

# OMEGA

  # Change work directory into gll

gll_from_main = "../output/erosion/tempfiles/gll/"
omega_from_w = "../../../../input/omega/"
w_from_gll = "../../../deposition/tempfiles/w/"
main_from_w = main_from_e

'''
  # Copy gll file into output temporary files for deposition (/output/deposition/tempfiles/w/)

os.chdir(gll_from_main)
srcp_gllfw = "."
destp_gllfw = w_from_gll
srcf_gllfw = os.listdir(srcp_gllfw)
for fl_gllfw in srcf_gllfw:
    if fl_gllfw.startswith("fl_"):
        f_gllfw = os.path.join(srcp_gllfw, fl_gllfw)
        if (os.path.isfile(f_gllfw)):
            shutil.copy(f_gllfw, destp_gllfw)

  # Give the whitespace after axis-ordinat and create omega.txt into input folder

os.chdir(w_from_gll)
with open("fl_fngll.txt") as omega_grid_axisordinat:
    gao_w = str(omega_grid_axisordinat.read().split(","))
    gaow_new = gao_w.replace("\\n"," \n")
    gaow_new = gaow_new.replace("['","")
    gaow_new = gaow_new.replace("']","")
    with open(omega_from_w+"omega.txt","w") as inp_gaow:
        inp_gaow.writelines(gaow_new)
  
  # Show pop up dialog to user for filling omega coefficient

print("\nPlease fill the Omega in omega directory!")
question_omega = input("\nIf You have already completed it, Press Y to continue or press N to exit! ")
if question_omega.lower().startswith("y"):
    print("\nPlease wait a moment...")
elif question_omega.lower().startswith("n"):
    exit()
elif question_omega.lower().startswith(""):
    print("\nERROR-UIO\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the omega coefficient.\n")
    print("If in a grid the value is not avaliable just type 0.")
    exit()
'''
    
  ### Copy omega file into output temporary files for deposition (/output/deposition/tempfiles/w) ###

os.chdir(gll_from_main)
os.chdir(w_from_gll)
srcp_omega = omega_from_w
destp_omega = "."
srcf_omega = os.listdir(srcp_omega)
for fl_omega in srcf_omega:
    f_omega = os.path.join(srcp_omega, fl_omega)
    if (os.path.isfile(f_omega)):
        shutil.copy(f_omega, destp_omega)
 
  # Save file's contents into variable

omega = list()
for varlst_omega in os.listdir("."):
    if varlst_omega.startswith("omega"):
        rvarlst_omega = open(varlst_omega,"r")
        rcvarlst_omega = str(rvarlst_omega.read())
        rrowvarlst_omega = rcvarlst_omega.split()
        omega.append(rrowvarlst_omega) 
 
  # Check if User has already filled every single omega coefficient
  # Save the value into a variable list 'value_omega'

split_omega = ((str(omega)).split())
if len(split_omega) == 2*(len([name for name in os.listdir(splasherosion_from_e) if os.path.isfile(os.path.join(splasherosion_from_e, name))])):
    for w in omega:
        complist_omega = [w[x:x+2] for x in range(0, len(w), 2)]
        dict_omega = dict(complist_omega)
        value_omega = list(dict_omega.values())
        for vo in value_omega:
            if 1.20 < float(vo) < 1.50:
                pass
            elif float(vo) < 1.20 :
                print("ERROR-UIO\n\nYour Omega value is less than 1.2")
                exit()
            elif float(vo) > 1.50:
                print("ERROR-UIO\n\nYour Omega value is greater than 1.5")
                exit()      
else:
    print("ERROR-UIO\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the omega coefficient.\n")
    print("If in a grid the value is not avaliable just type 0.")
    exit()
os.chdir(main_from_w)

# GRAVITY ACCELERATION

g = 9.81 # SI

# SPESIFIC WEIGHT OF WATER

gamma = 1000 # SI
########## HERE IS THE LAST SECTION OF DEPOSITION DATA INPUT CLASS ##########

########## HERE IS THE INITIAL SECTION OF DEPOSITION DATA PROCESS CLASS ##########

# Loading Animation

done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write("\rCalculating deposition " + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n\nDone! Cleaning up residual files...\n')
t = threading.Thread(target=animate)
t.start()
time.sleep(10)
done = True

# INITIAL FLUIDA

Fo = list()
zip_initial_fluida = zip(value_gammas, value_viscosity, value_diameter)
for single_gammas, single_viscosity, single_diameter in zip_initial_fluida:
    single_gammas = float(single_gammas)
    single_viscosity = float(single_viscosity)
    single_diameter = float(single_diameter)
    Fo_indexb = (single_gammas/gamma)-1.0
    Fo_indexu = (36*single_viscosity**2)/(g*(single_diameter**3)*Fo_indexb)
    single_Fo = math.sqrt(((2.0/3.0)+(Fo_indexu)))-math.sqrt((Fo_indexu))
    Fo.append(single_Fo)

# SEDIMENT VELOCITY

Vs = list()
zip_velocity_fluida = zip(Fo, value_gammas, value_diameter)
for sub_Fo, single_gammas, single_diameter in zip_velocity_fluida:
    sub_Fo = float(sub_Fo)
    single_gammas = float(single_gammas)
    single_diameter = float(single_diameter)
    single_Vs = sub_Fo*(math.sqrt((single_gammas-gamma)/gamma))*g*single_diameter
    Vs.append(single_Vs)
 
# SEDIMENT CONCENTRATION

c = list()
zip_sediment_concentration = zip(runoff, value_omega)
for q, single_omega in zip_sediment_concentration:
    single_omega = float(single_omega)
    for qq in q:
        float_qq = float(qq)
        single_c = float_qq**(single_omega-1.0)
        c.append(single_c)
flux_dur = list()
q_from_main = "../output/erosion/tempfiles/q/"
for day_dur in os.listdir(q_from_main):
    flux_dur.append(day_dur)
sample_flux = str(flux_dur[0])
with open(q_from_main+sample_flux) as smpl_dur:
    dlen_dur = len(list((smpl_dur.read()).split()))
q_c = [c[i:i+(dlen_dur)] for i in range(0,len(c),(dlen_dur))]

# DEPOSITION

dep_nf = list()
for dep_namefiles in os.listdir(q_from_main):
    if dep_namefiles.startswith("fluxes"):
        dep_namefile = dep_namefiles.replace("fluxes","deposition")
        dep_nf.append(dep_namefile)

deposition = list()
deposition_from_main = "../output/deposition/"
zip_deposition = zip(dep_nf, value_epsilon, Vs, q_c)
for dnf, eps, data_Vs, qc in zip_deposition:
    float_eps = float(eps)
    float_data_Vs = float(data_Vs)
    with open(deposition_from_main+dnf,"w") as out_dep:
        for qqc in qc:
            float_qqc = float(qqc)
            value_deposition = float_eps * float_data_Vs * float_qqc
            deposition.append(value_deposition)
            out_dep.writelines("%.30f\n" %value_deposition)
########## HERE IS THE LAST SECTION OF DEPOSITION DATA PROCESS CLASS ##########

########## HERE IS THE INITIAL SECTION OF DEPOSITION DATA OUTPUT CLASS ##########
# TRANSPORT SEDIMENT RESULT

  # Index folder path
 
output_from_main = "../output/"
erosion_from_main = "../output/erosion/"
deposition_from_main = "../output/deposition/"

  # Initial empty list for erosion and deposition variable

erosion_var = list()
deposition_var = list()

  # Make list of file name inside of folder erosion and deposition

listdir_erosion = os.listdir(erosion_from_main)
listdir_deposition = os.listdir(deposition_from_main)

  # Make list of file name the transport sediment files 

listdir_transport = os.listdir(runoff_from_main)

  # Zip the list

zip_erosion_deposition = zip(listdir_erosion, listdir_deposition)

# Append every file's content into initial list of erosion and deposition

for erosion_ff, deposition_ff in zip_erosion_deposition:
    if erosion_ff.startswith("erosion"):
        with open(erosion_from_main+erosion_ff) as var_erosion:
            v_erosion = str(var_erosion.read())
            l_erosion = v_erosion.split()
            erosion_var.append(l_erosion)
    if deposition_ff.startswith("deposition"):
        with open(deposition_from_main+deposition_ff) as var_deposition:
            v_deposition = str(var_deposition.read())
            l_deposition = v_deposition.split()
            deposition_var.append(l_deposition)

# Convert list into numpy array

erosion_array = np.array(erosion_var)
deposition_array = np.array(deposition_var)
zip_transport = zip(listdir_transport, erosion_array, deposition_array)
for transport_f, new_single_erosion, new_single_deposition in zip_transport:
    if transport_f.startswith("fluxes"):
        rep_flux = transport_f.replace("fluxes","transport")
        with open(output_from_main+rep_flux,"w") as transport_result:
            for single_year, single_month, single_day, subs_erosion, subs_deposition in zip(list_years, list_months, list_days, new_single_erosion, new_single_deposition):
                float_erosion_result = float(subs_erosion)
                float_deposition_result = float(subs_deposition)
                year = str(single_year)
                month = str(single_month)
                day = str(single_day)
                result = float_erosion_result - float_deposition_result
                transport_result.writelines("%s\t%s\t%s\t%.10f\n" % (year, month, day, result))
########## HERE IS THE LAST SECTION OF DEPOSITION DATA OUTPUT CLASS ##########
########## HERE IS THE LAST SECTION OF DEPOSITION CLASS ##########