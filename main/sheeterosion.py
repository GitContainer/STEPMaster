#!/usr/bin/python

# SHEET EROSION

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



########## HERE IS THE INITIAL SECTION OF SHEET EROSION CLASS ##########
# SHEET EROSION EQUATION

  # Sheet Erosion =  Rill Erodibility x Critical Shear Stress**1.5

  # Critical Shear Stress will be calculated based on Specific Weight, Slope and Radius of Hydrolic
  # User should provide the rill erodibility for every single grid

########## HERE IS THE INITIAL SECTION OF CRITICAL SHEAR STRESS CLASS ##########
########## HERE IS THE INITIAL SECTION OF OVERLAND FLOW CLASS ##########
# OVERLAND FLOW CLASS

  # Change work directory into input runoff folder
  
runoff_from_main = "../input/runoff/"
fluxes_from_runoff = "../../output/erosion/tempfiles/q/"
main_from_fluxes = "../../../../main/"
fluxes_from_main = "../output/erosion/tempfiles/q/"
os.chdir(runoff_from_main)

 # Remove header and copy the fluxes files into output folder

ordered_files_runoff_main = sorted(os.listdir("."), key=lambda x: (int(re.sub('\D','',x)),x))
for fn_fluxes in ordered_files_runoff_main:
    with open(fn_fluxes,"r") as f:
        lines_after_6 = f.readlines()[6:]
    with open(fluxes_from_runoff+fn_fluxes,"w") as writefluxes:
        writefluxes.writelines(lines_after_6)

  # Select column no.6 as runoff or overflow 

os.chdir(fluxes_from_runoff)
ordered_files_fluxes_runoff = sorted(os.listdir("."), key=lambda x: (int(re.sub('\D','',x)),x))
for file_fluxes in ordered_files_fluxes_runoff:
    with open(file_fluxes,"r") as content_fluxes:
        string_fluxes = str(content_fluxes.read().split())
        rplce_str1 = string_fluxes.replace("'","")
        splitby = rplce_str1.split(",")
        list_flxs = list(splitby)
        shorted_flxs = list_flxs[5::11]
        reverse_flxs = str(shorted_flxs)
        rplce_str2 = reverse_flxs.replace("[' ","")
        rplce_str3 = rplce_str2.replace("']","")
        new_line_flxs = rplce_str3.replace("', ' ","\n")
        with open(file_fluxes,"w") as output_flow:
            output_flow.writelines(new_line_flxs)

  # Get day duration
  
flux_dur = list()
for day_dur in ordered_files_fluxes_runoff:
    flux_dur.append(day_dur)
sample_flux = str(flux_dur[0])
with open(sample_flux) as smpl_dur:
    dlen_dur = len(list((smpl_dur.read()).split()))

  # Read the runoff data as a variable

runoff = list()
for file_fluxes in ordered_files_fluxes_runoff:
    with open(file_fluxes) as content_runoff:
        read_content_runoff = list((content_runoff.read()).split())
        scalar_array_runoff = np.array(0.0000000000000115740740740741, dtype = float)
        array_content_runoff = np.array(read_content_runoff, dtype = float)
        runoff_result = array_content_runoff * scalar_array_runoff
        value_runoff = runoff_result.tolist()
        runoff.append(value_runoff)  
os.chdir(main_from_fluxes)
########## HERE IS THE LAST SECTION OF OVERLAND FLOW CLASS ##########

########## HERE IS THE INITIAL SECTION OF GRID SIZE CLASS ##########
# GRID SIZE

  # Change work directory into gll

gll_from_main = "../output/erosion/tempfiles/gll/"
main_from_gll = main_from_fluxes
os.chdir(gll_from_main)

  # Grab the input from gll.txt and get the grid size

with open("gll.txt","r") as axisordinat:
    ordinat_y = str(axisordinat.read().split())
    rplce_apstrf = ordinat_y.replace("'","")
    spltby_com = rplce_apstrf.split(",")
    lst_ordinaty = list(spltby_com)
    shorted_y = lst_ordinaty[2:6:3]
    first_y = float(str(shorted_y[0]))
    sec_y = float(str(shorted_y[1]))
    deg_grid_size = sec_y - first_y
    km_grid_size = 111.12 * deg_grid_size # 111.12 is a convertion number from degree to kilometer
    grid_size = km_grid_size * 1000.0
os.chdir(main_from_gll)
########## HERE IS THE LAST SECTION OF GRID SIZE CLASS ##########

########## HERE IS THE INITIAL SECTION OF GRID SLOPE CLASS ##########
# GRID SLOPE  
  
  # Change work directory into gll

grdslp_from_stemp = "../../../../input/gridslope/"
stemp_from_gll = "../s/"
splasherosion_from_stemp = '../../splasherosion/'

'''
  # Copy gll file into output temporary files for erosion (/output/erosion/tempfiles/s/)

os.chdir(gll_from_main)
srcp_gllf = "."
destp_gllf = stemp_from_gll
srcf_gllf = os.listdir(srcp_gllf)
for fl_gllf in srcf_gllf:
    if fl_gllf.startswith("fl_"):
        f_gllf = os.path.join(srcp_gllf, fl_gllf)
        if (os.path.isfile(f_gllf)):
            shutil.copy(f_gllf, destp_gllf)

  # Give the whitespace after axis-ordinat and create gridslope.txt into input folder

os.chdir(stemp_from_gll)
with open("fl_fngll.txt") as grid_axisordinat:
    gao = str(grid_axisordinat.read().split(","))
    gao_new = gao.replace("\\n"," \n")
    gao_new = gao_new.replace("['","")
    gao_new = gao_new.replace("']","")
    with open(grdslp_from_stemp+"gridslope.txt","w") as inp_gao:
        inp_gao.writelines(gao_new)
  
  # Show pop up dialog to user for filling grid slope value

print("\nPlease fill the grid Slope values in Grid Slope directory!")
question_slope = input("\nIf You have already completed it, Press Y to continue or press N to exit! ")
if question_slope.lower().startswith("y"):
    print("\nPlease wait a moment...\n")
elif question_slope.lower().startswith("n"):
    exit()
elif question_slope.lower().startswith(""):
    print("\nERROR-UIS\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Slope values.\n")
    print("If in a grid the value is not avaliable just type 0.")
    exit()
'''

  ### Copy slope file into output temporary files for erosion (/output/erosion/tempfiles/s) ###

os.chdir(gll_from_main)
os.chdir(stemp_from_gll)
srcp_slope = grdslp_from_stemp
destp_slope = "."
srcf_slope = os.listdir(srcp_slope)
for fl_slope in srcf_slope:
    f_slope = os.path.join(srcp_slope, fl_slope)
    if (os.path.isfile(f_slope)):
        shutil.copy(f_slope, destp_slope)
 
  # Save file's contents into variable

slope = list()
for varlst_slope in os.listdir("."):
    if varlst_slope.startswith("gridslope"):
        rvarlst_slope = open(varlst_slope,"r")
        rcvarlst_slope = str(rvarlst_slope.read())
        rrowvarlst_slope = rcvarlst_slope.split()
        slope.append(rrowvarlst_slope) 
    
  # Check if User has already filled every single grid slope values
  # Save the value into a variable list 'value_slope'

split_slope = ((str(slope)).split())
ordered_files_splasherosion_stemp = sorted(os.listdir(splasherosion_from_stemp), key=lambda x: (int(re.sub('\D','',x)),x))
if len(split_slope) == 2*(len([name for name in ordered_files_splasherosion_stemp if os.path.isfile(os.path.join(splasherosion_from_stemp, name))])):
    for s in slope:
        complist_slope = [s[x:x+2] for x in range(0, len(s), 2)]
        dict_slope = dict(complist_slope)
        value_slope = list(dict_slope.values())
else:
    print("\nERROR-UIS\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Slope values.\n")
    print("If in a grid the value is not avaliable just type 0.")
    exit()
os.chdir(main_from_gll)
########## HERE IS THE LAST SECTION OF GRID SLOPE CLASS ##########

########## HERE IS THE INITIAL SECTION OF MANNING COEFFICIENT CLASS ##########
# MANNING COEFFICIENT

  # Change work directory into gll

manning_from_n = "../../../../input/manning/"
n_from_gll = "../n/"

'''
  # Copy gll file into output temporary files for erosion (/output/erosion/tempfiles/n/)

os.chdir(gll_from_main)
srcp_gllfn = "."
destp_gllfn = n_from_gll
srcf_gllfn = os.listdir(srcp_gllfn)
for fl_gllfn in srcf_gllfn:
    if fl_gllfn.startswith("fl_"):
        f_gllfn = os.path.join(srcp_gllfn, fl_gllfn)
        if (os.path.isfile(f_gllfn)):
            shutil.copy(f_gllfn, destp_gllfn)

  # Give the whitespace after axis-ordinat and create manning.txt into input folder

os.chdir(n_from_gll)
with open("fl_fngll.txt") as manning_grid_axisordinat:
    gao_n = str(manning_grid_axisordinat.read().split(","))
    gaon_new = gao_n.replace("\\n"," \n")
    gaon_new = gaon_new.replace("['","")
    gaon_new = gaon_new.replace("']","")
    with open(manning_from_n+"manning.txt","w") as inp_gaon:
        inp_gaon.writelines(gaon_new)
  
  # Show pop up dialog to user for filling manning coefficient

print("Please fill the Manning coefficient in Manning directory!")
question_manning = input("\nIf You have already completed it, Press Y to continue or press N to exit! ")
if question_manning.lower().startswith("y"):
    print("\nPlease wait a moment...")
elif question_manning.lower().startswith("n"):
    exit()
elif question_manning.lower().startswith(""):
    print("\nERROR-UIM\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Manning coefficient.\n")
    print("If in a grid the value is not avaliable just type 0.")
    exit()
'''

  ### Copy slope file into output temporary files for erosion (/output/erosion/tempfiles/n) ###

os.chdir(gll_from_main)
os.chdir(n_from_gll)
srcp_manning = manning_from_n
destp_manning = "."
srcf_manning = os.listdir(srcp_manning)
for fl_manning in srcf_manning:
    f_manning = os.path.join(srcp_manning, fl_manning)
    if (os.path.isfile(f_manning)):
        shutil.copy(f_manning, destp_manning)
 
  # Save file's contents into variable

manning = list()
for varlst_manning in os.listdir("."):
    if varlst_manning.startswith("manning"):
        rvarlst_manning = open(varlst_manning,"r")
        rcvarlst_manning = str(rvarlst_manning.read())
        rrowvarlst_manning = rcvarlst_manning.split()
        manning.append(rrowvarlst_manning) 
    
  # Check if User has already filled every single manning coefficient
  # Save the value into a variable list 'value_manning'

split_manning = ((str(manning)).split())
ordered_files_splasherosion_temp = sorted(os.listdir(splasherosion_from_stemp), key=lambda x: (int(re.sub('\D','',x)),x))
if len(split_manning) == 2*(len([name for name in ordered_files_splasherosion_temp if os.path.isfile(os.path.join(splasherosion_from_stemp, name))])):
    for n in manning:
        complist_manning = [n[x:x+2] for x in range(0, len(n), 2)]
        dict_manning = dict(complist_manning)
        value_manning = list(dict_manning.values())
else:
    print("\nERROR-UIM\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Manning coefficient.\n")
    print("If in a grid the value is not avaliable just type 0.")
    exit()
os.chdir(main_from_gll)
########## HERE IS THE LAST SECTION OF MANNING COEFFICIENT CLASS ##########

########## HERE IS THE INITIAL SECTION OF POLYNOMIAL EQUATION CLASS ##########
# POLYNOMIAL EQUATION

  # Loading animation

print(" ")
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write("\rCalculating polynomial equation to get depth of channel flow " + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n\nPlease be patient. This could take some time...\n\n')
t = threading.Thread(target=animate)
t.start()
time.sleep(10)
done = True

  # Define coefficient of equation

x5_init = list()
for val_slope in value_slope:
    arr_slope = np.array(val_slope, dtype=float)
    arr_gsize = np.array(grid_size, dtype=float)
    x5 = arr_slope**1.5 * arr_gsize**5
    x5_init.append(x5)
x2_init = list()
for q, n in zip(runoff, value_manning):
    arr_mannning = np.array(n, dtype=float)
    for subq in q:
        arr_runoff = np.array(subq, dtype=float)
        x2 = 4 * arr_runoff**3 * arr_mannning**3
        x2_init.append(x2)
x2_per_grid = [x2_init[i:i+(dlen_dur)] for i in range(0,len(x2_init),(dlen_dur))]
x0_init = list()
for q_x0, n_x0 in zip(runoff, value_manning):
    arr_gsizex0 = np.array(grid_size, dtype=float)
    arr_manningx0 = np.array(n_x0, dtype=float)
    for subq_x0 in q_x0:
        arr_runoffx0 = np.array(subq_x0, dtype=float)
        x0 = arr_runoffx0**3 * arr_gsizex0**2 * arr_manningx0**3
        x0_init.append(x0)
x0_per_grid = [x0_init[i:i+(dlen_dur)] for i in range(0,len(x0_init),(dlen_dur))]

  # Extract x2_init and x0_init into files
  
x2_from_main = "../output/erosion/tempfiles/p/x2/"
ordered_files_fluxes_main = sorted(os.listdir(fluxes_from_main), key=lambda x: (int(re.sub('\D','',x)),x))
for x2_namefiles, x2s in zip(ordered_files_fluxes_main, x2_per_grid):
    with open(x2_from_main+x2_namefiles,"w") as x2_output:
        for x2sp in x2s:
            str_x2sp = str(x2sp)
            x2_output.writelines("%s\n" %str_x2sp)
x0_from_main = "../output/erosion/tempfiles/p/x0/"
for x0_namefiles, x0s in zip(ordered_files_fluxes_main, x0_per_grid):
    with open(x0_from_main+x0_namefiles,"w") as x0_output:
        for x0sp in x0s:
            str_x0sp = str(x0sp)
            x0_output.writelines("%s\n" %str_x0sp)
  
  # Read the x2s and x0s and save them into a variable

x2ss = list()
x0ss = list()
ordered_files_x2_main = sorted(os.listdir(x2_from_main), key=lambda x: (int(re.sub('\D','',x)),x))
ordered_files_x0_main = sorted(os.listdir(x0_from_main), key=lambda x: (int(re.sub('\D','',x)),x))
for listfile_x2s, listfile_x0s in zip(ordered_files_x2_main, ordered_files_x0_main):
    with open(x2_from_main+listfile_x2s) as var_x2s:
        v_x2s = str(var_x2s.read().split())
        r_x2s = v_x2s.replace("[","")
        r_x2s = r_x2s.replace("]","")
        r_x2s = r_x2s.replace("'","")
        r_x2s = r_x2s.replace(",'","")
        r_x2s = r_x2s.replace(","," ")
        l_x2s = r_x2s.split()
        x2ss.append(l_x2s)
    with open(x0_from_main+listfile_x0s) as var_x0s:
        v_x0s = str(var_x0s.read().split())
        r_x0s = v_x0s.replace("[","")
        r_x0s = r_x0s.replace("]","")
        r_x0s = r_x0s.replace("'","")
        r_x0s = r_x0s.replace(",'","")
        r_x0s = r_x0s.replace(","," ")
        l_x0s = r_x0s.split()
        x0ss.append(l_x0s)
x5ss_array = np.array(x5_init, dtype = float)
x2ss_array = np.array(x2ss, dtype = float)
x0ss_array = np.array(x0ss, dtype = float)
  # Formulating polynomial equation

h = list()  
for x5p, x2p, x0p in zip(x5ss_array, x2ss_array, x0ss_array):
    pass
    for x2pp, x0pp in zip(x2p, x0p):
        x5p_float = float(x5p)
        x2p_float = float(x2pp)
        x0p_float = float(x0pp)
        p = P([-x0p_float,0,-x2p_float,0,0,x5p_float])
        roots = p.roots()
        for i in range(len(roots)):
            if np.isreal(roots[i]):
                depth = np.real(roots[i])
                h.append(depth)
########## HERE IS THE LAST SECTION OF POLYNOMIAL EQUATION CLASS ##########

########## HERE IS THE INITIAL SECTION OF DEPTH CHANNEL FLOW CLASS ##########
# DEPTH CHANNEL FLOW

  # Get the depth

new_sheet_depth = list()
for sheet_depth in h:
    hdepth = str(sheet_depth)
    new_sheet_depth.append(hdepth)
str_new_sheet_depth = str(new_sheet_depth)
rep_new_sheet_depth = str_new_sheet_depth.replace("'0.0', '0.0', '0.0', '0.0', '0.0'","'0.0'")
rep_new_sheet_depth = rep_new_sheet_depth.replace("['","")
rep_new_sheet_depth = rep_new_sheet_depth.replace("', '"," ")
rep_new_sheet_depth = rep_new_sheet_depth.replace("']","")
list_sheet_depth = rep_new_sheet_depth.split()
sheet_depth_per_grid = [list_sheet_depth[i:i+(dlen_dur)] for i in range(0,len(list_sheet_depth),(dlen_dur))]
str_prob = str(sheet_depth_per_grid)
########## HERE IS THE LAST SECTION OF DEPTH CHANNEL CLASS ##########

########## HERE IS THE INITIAL SECTION OF HYDRAULIC RADIUS CLASS ##########
# HYDRAULIC RADIUS

  # Make a list of hydraulic radius

RH = list()
for vdepth in sheet_depth_per_grid:
    pass
    for depth_per_day in vdepth:
        fvwidth = float(grid_size)
        fvdepth = float(depth_per_day)
        rh = (fvwidth * fvdepth) / (fvwidth + (2 * fvdepth))
        RH.append(rh)
RH_per_grid = [RH[i:i+(dlen_dur)] for i in range(0,len(RH),(dlen_dur))]

  # Write files for hydraulic radius

hydroradius_from_main = "../output/erosion/tempfiles/r/"
ordered_files_fluxes_main = sorted(os.listdir(fluxes_from_main), key=lambda x: (int(re.sub('\D','',x)),x))
fnlist_RH = ordered_files_fluxes_main
for out_RH, sRH in zip(fnlist_RH, RH_per_grid):
    with open(hydroradius_from_main+out_RH,"w") as wo_RH:
        for ssRH in sRH:
            str_ssRH = str(ssRH)
            wo_RH.writelines("%s\n" %str_ssRH)
########## HERE IS THE LAST SECTION OF HYDRAULIC RADIUS CLASS ##########

########## HERE IS THE INITIAL SECTION OF SHEAR STRESS CLASS ##########
# SHEAR STRESS

  # Specific Weight

question_gamma = 1000
gamma = float(question_gamma)
    
  # Shear Stress Calculation

tau = list()
for valslope, radius_hydrolic in zip(value_slope, RH_per_grid):
    pass
    for rad_hydro in radius_hydrolic:
        float_g = float(gamma)
        float_RH = float(rad_hydro)
        float_s = float(valslope)
        shear_stress = float_g * float_RH * float_s
        tau.append(shear_stress)
tau_per_grid = [tau[i:i+(dlen_dur)] for i in range(0,len(tau),(dlen_dur))]
########## HERE IS THE LAST SECTION OF SHEAR STRESS CLASS ##########
########## HERE IS THE LAST SECTION OF CRITICAL SHEAR STRESS CLASS ##########

########## HERE IS THE INITIAL SECTION OF ERODIBILITY CLASS ##########
# ERODIBILITY

  # Change work directory into gll

erodibility_from_k = "../../../../input/erodibility/"
k_from_gll = "../k/"

'''
  # Copy gll file into output temporary files for erosion (/output/erosion/tempfiles/k/)

os.chdir(gll_from_main)
srcp_gllfk = "."
destp_gllfk = k_from_gll
srcf_gllfk = os.listdir(srcp_gllfk)
for fl_gllfk in srcf_gllfk:
    if fl_gllfk.startswith("fl_"):
        f_gllfk = os.path.join(srcp_gllfk, fl_gllfk)
        if (os.path.isfile(f_gllfk)):
            shutil.copy(f_gllfk, destp_gllfk)

  # Give the whitespace after axis-ordinat and create erodibility.txt into input folder

os.chdir(k_from_gll)
with open("fl_fngll.txt") as erodibility_gao:
    ero_k = str(erodibility_gao.read().split(","))
    erok = ero_k.replace("\\n"," \n")
    erok = erok.replace("['","")
    erok = erok.replace("']","")
    with open(erodibility_from_k+"erodibility.txt","w") as inp_erok:
        inp_erok.writelines(erok)
  
  # Show pop up dialog to user for filling erodibility values

print("\nPlease fill the Erodibility values in Erodibility directory!")
question_eoridibility = input("\nIf You have already completed it, Press Y to continue or press N to exit! ")
if question_eoridibility.lower().startswith("y"):
    print("\nPlease wait a moment...\n")
elif question_eoridibility.lower().startswith("n"):
    exit()
elif question_slope.lower().startswith(""):
    print("\nERROR-UIE\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Erodibility values.\n")
    print("If in a grid the value is not avaliable just type 0.")
    exit()
'''   
    
  ### Copy erodibility file into output temporary files for erosion (/output/erosion/tempfiles/k) ###

os.chdir(gll_from_main)
os.chdir(k_from_gll)
srcp_erodibility = erodibility_from_k
destp_erodibility = "."
srcf_erodibility = os.listdir(srcp_erodibility)
for fl_erodibility in srcf_erodibility:
    f_erodibility = os.path.join(srcp_erodibility, fl_erodibility)
    if (os.path.isfile(f_erodibility)):
        shutil.copy(f_erodibility, destp_erodibility)
 
  # Save file's contents into variable

erodibility = list()
for varlst_erodibility in os.listdir("."):
    if varlst_erodibility.startswith("erodibility.txt"):
        rvarlst_erodibility = open(varlst_erodibility,"r")
        rcvarlst_erodibility = str(rvarlst_erodibility.read())
        rrowvarlst_erodibility = rcvarlst_erodibility.split()
        erodibility.append(rrowvarlst_erodibility) 
    
  # Check if User has already filled every single erodibility values
  # Save the value into a variable list 'value_erodibility'

split_erodibility = ((str(erodibility)).split())
ordered_files_splasherosion_temp = sorted(os.listdir(splasherosion_from_stemp), key=lambda x: (int(re.sub('\D','',x)),x))
if len(split_erodibility) == 2*(len([name for name in ordered_files_splasherosion_temp if os.path.isfile(os.path.join(splasherosion_from_stemp, name))])):
    for k in erodibility:
        complist_erodibility = [k[x:x+2] for x in range(0, len(k), 2)]
        dict_erodibility = dict(complist_erodibility)
        value_erodibility = list(dict_erodibility.values())
else:
    print("ERROR-UIE\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Erodibility values.\n")
    print("If in a class the value is not avaliable just type 0.")
    exit()
os.chdir(main_from_gll)
########## HERE IS THE LAST SECTION OF ERODIBILITY CLASS ##########

########## HERE IS THE INITIAL SECTION OF SHEET EROSION CALCULATION CLASS ##########
# SHEET EROSION CALCULATION

  # Loading animation

done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write("\rCalculating sheet erosion " + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n\nDone! Identifying deposition data...\n\n')
t = threading.Thread(target=animate)
t.start()
time.sleep(10)
done = True

  # Peform the calculation

she_erosion = list()
for valero, taupg in zip(value_erodibility, tau_per_grid):
    pass
    for t in taupg:
        float_valero = float(valero)
        float_t = float(t)
        sheet_erosion = float_valero * float_t**1.5
        she_erosion.append(sheet_erosion)
she_per_grid = [she_erosion[i:i+(dlen_dur)] for i in range(0,len(she_erosion),(dlen_dur))]
########## HERE IS THE LAST SECTION OF SHEET EROSION CALCULATION CLASS ##########
########## HERE IS THE LAST SECTION OF SHEET EROSION CLASS ##########

########## HERE IS THE INITIAL SECTION OF SHEET EROSION REPORT CLASS ##########
# REPORT

  # Index folder path

mm_from_main = "../output/erosion/tempfiles/mm/"
mm2_from_main = "../output/erosion/sheeterosion/"

  # Write the results into files

report_sheeterosion = list()
for lst_files in os.listdir(mm_from_main):
    if lst_files.startswith("data_"):
        report_sheeterosion.append(lst_files)
ordered_files_mm_main = sorted(report_sheeterosion, key=lambda x: (int(re.sub('\D','',x)),x))
she_nf = list()
for she_namefiles in ordered_files_mm_main:
    if she_namefiles.startswith("data_"):
        she_namefile = she_namefiles.replace("data","she")
        she_nf.append(she_namefile)
for nf_she, she in zip(she_nf,she_per_grid):
    with open(mm2_from_main+nf_she,"w") as create_she:
        for sh in she:
            float_sh = float(sh)
            create_she.writelines("%.30f\n"%float_sh)
########## HERE IS THE LAST SECTION OF SHEET EROSION REPORT CLASS ##########