#!/usr/bin/python

# SPLASH EROSION

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
print(" ")
'''

  ### LOADING MODULES ###
  # After the packages has been satisfied by running setup.py, then import the modules and the alias by running the script below:
    
import glob, os, shutil, itertools, re, sys, time, threading, pandas as pd, numpy as np
from itertools import zip_longest, groupby, islice
from functools import reduce
from operator import mul
np.set_printoptions(suppress=True, threshold=np.inf, linewidth=np.inf) # Handling output mode and turn scientific mode off, summarization and line-wrapping
    
  # Disabled modules: pickle, chain, csv, ctypes, collections, pprint, from io import StringIO

# FLUSH OUTPUT FOLDER

  # Loading Animation

done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write("\rIdentifying splash erosion data " + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')
t = threading.Thread(target=animate)
t.start()
time.sleep(10)
done = True

  # Flush and clean up the contents of output folder to make sure there is no files inside

output_directory = '../output'
for dirpath, dirnames, filenames in os.walk(output_directory):
    # Remove regular files and ignore directories
    for filename in filenames:
        os.unlink(os.path.join(dirpath, filename))
        
# IMPORT LOCAL AND GLOBAL LISTS

  ### IMPORT LOCAL LISTS ###
  # Import lists of folder path from local file

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
  # Import lists of folder path from global file
   
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



########## HERE IS THE INITIAL SECTION OF SPLASH EROSION CLASS ##########
# SPLASH EROSION EQUATION

  # Splash Erosion =  Alpha x Squared of Rainfall Intensity

  # Alpha will be calibrated by multiplied with the fraction of cover vegetation
  
  # Before run this script below, User should provide the rainfall intensity for every single grid in input directory named "forcing"

########## HERE IS THE INITIAL SECTION OF GRID CELL CLASS ##########
# Grid Lat-Long

  ### COLUMNS SELECTION FOR CONTENT ###

  # Load array data list from local file with initial name 'soil' located in /input/gridlatlon

floc_gll = arr_local[0,1] # Save Grid Lat-Lon folder path into a variable  
flist_gll = glob.glob(floc_gll) # Load Grid Lat-Lon content from the folder path
cols_gll = [1,2,3] # Index 1,2,3 are Grid, Latitude, Longitude

  # Reading certain rows and columns with Pandas Module

df_gll = pd.DataFrame()
for f_gll in flist_gll:
    df_gll = df_gll.append(pd.read_csv
                           (f_gll, delimiter='\s+', header=None, usecols=cols_gll, na_values=['']),
                           ignore_index=True)
arr_gll = df_gll.values

  # Writing selected rows and columns into a file

gll_stripped = "../output/erosion/tempfiles/gll/gll.txt"
with open(gll_stripped, 'w') as f_gll:
    f_gll.write(np.array2string(arr_gll, separator=' '))

  # Read the content of filename list of gll.txt

with open(gll_stripped) as gll_strp:
    gll_strpin = gll_strp.read()
    # remove brackets from gll string list 
    rmb_gll_strpin_1 = gll_strpin.replace('[[',' ')
    rmb_gll_strpin_2 = rmb_gll_strpin_1.replace('[','')
    rmb_gll_strpin_3 = rmb_gll_strpin_2.replace(']','')
    rmb_gll_strpin_4 = rmb_gll_strpin_3.replace(']]','')
    rmd_gll = re.compile("(?<=\d)(\.)(?!\d)")
    rmb_gll_strpin_5 = rmd_gll.sub("",rmb_gll_strpin_4)
rmbd_gll_strpin = gll_stripped # Overwrite gll.txt
with open(rmbd_gll_strpin, 'w') as wr_rmbd:
    wr_rmbd.write(rmb_gll_strpin_5)
    
  ### COLUMNS SELECTION FOR FILE NAME ###

  # Open file path to be read

fl_fngll = open(floc_gll, 'r')

  # Writing temporary file named fl_fngll.txt contains stripped columns
  
tmp_fngll = '../output/erosion/tempfiles/gll/fl_fngll.txt'
  
  # Iterate over the lines and write it into a file

fn_gll = open(tmp_fngll,'w')
for line_gll in fl_fngll:
    # Split the line into a list of column values
    columns_gll = line_gll.split(' ')
    # Clean any whitespace off the items
    columns_gll = [col.strip() for col in columns_gll]
    # Ensure the column has at least one value before printing
    if columns_gll:
        clat = str(columns_gll[2])
        clon = str(columns_gll[3])
        filename_splasherosion = clat+"_"+clon
    # Write the list into a file
    fn_gll.write("%s\n" %filename_splasherosion)
fn_gll.close()
    
  ### GLL WRITE INTO MULTIPLE FILES & NAME IT BASED ON FL_FNGLL.TXT ###
               
  # Definition function for grouping
  
def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, * args)

  # How many lines will be read and write into a file?

n = 1
 
  # Read the content of filename list of splasherosion
  
with open(tmp_fngll) as lfn_gll:
    lfrn_gll = lfn_gll.read().splitlines()
    
  # Stripped GLL path location and initial definition of splasherosion filename

stripped_gll_floc = gll_stripped
dfn_of_se = '../output/erosion/splasherosion/splasherosion_{0}'

  # Write lists of filename into file

with open(stripped_gll_floc) as f:
    for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
        with open(dfn_of_se.format(i * n), 'w') as fout:
            fout.writelines(g)

  # Rename splasherosion_[number] to be se_[lat]_[lon]

root_splasherosion = '../output/erosion/splasherosion'
replace_by = 'se_{0}'
for lsfn_gll in lfrn_gll[::-1]:
    for item_splasherosion in os.listdir(root_splasherosion):
        fullpath_splasherosion = os.path.join(root_splasherosion, item_splasherosion)
    shutil.move(fullpath_splasherosion, fullpath_splasherosion.replace(item_splasherosion, replace_by.format(lsfn_gll)))
########## HERE IS THE LAST SECTION OF GRID CELL CLASS ##########

########## HERE IS THE INITIAL SECTION OF RAINFALL INTENSITY CLASS ##########
# Rainfall Intensity

  ### Copy entire forcing files into output temporary files for erosion (/output/erosion/tempfiles/ri) ###

srcp_ri = arr_local[1,1]
destp_ri = '../output/erosion/tempfiles/ri'
srcf_ri = os.listdir(srcp_ri)
for fl_ri in srcf_ri:
    f_ri = os.path.join(srcp_ri, fl_ri)
    if (os.path.isfile(f_ri)):
        shutil.copy(f_ri, destp_ri)
        
  ### Columns selection ###

  # Create list of filename to be read
  
os.chdir(destp_ri) # Change directory to /output/erosion/tempfiles/ri
with open("ri_flist.txt","w") as ri_flst: # Create a empty file ri_list.txt
    for ri_flist in glob.glob("data_*_*"): # Take name lists of forcing data
        ri_flst.write(str(ri_flist) + '\n') # Write it down into ri_list.txt
tmp_fnri = 'ri_flist.txt' # Save filename lists of rainfall intensity into a variable
with open(tmp_fnri) as lfn_ri: # Create list of filename to be read
    lfr_ri = lfn_ri.read().splitlines() # Make a list with newlines as separator
main_from_ri = "../../../../main"
os.chdir(main_from_ri) # Change directory to /main/

  # Stripping columns per file
  
os.chdir(destp_ri) # Change directory to /output/erosion/tempfiles/ri
for row in lfr_ri:
    # Read and write with same filename 
    fl_fnri = open(row, 'r') # Open file name to be read
    # Write temporary file named data_lat_lon.txt contains stripped columns
    tmp_fnri = "%s" %row
    fn_ri = open(tmp_fnri,'w')
    forcing_from_ri = "../../../../input/forcing/"
    rain = forcing_from_ri+str(row)
    # Iterate over the lines and write it into a file
    for line_ri in open(rain, 'r'):
        # Split the line into a list of column values
        columns_ri = line_ri.split(' ')
        # Clean any white space off the items
        columns_ri = [col.strip() for col in columns_ri]
        # Ensure the column has at least one value before printing
        if columns_ri:
            mmph2mps = float((1/10**3)/(60*60))
            ri = (float(columns_ri[0])*mmph2mps)**2
            ri_sqr = str("%.30f" %ri)
        fn_ri.write("%s\n" %ri_sqr)
    fn_ri.close()
os.chdir(main_from_ri) # Change directory to /main/
########## HERE IS THE LAST SECTION OF RAINFALL INTENSITY CLASS ##########

########## HERE IS THE INITIAL SECTION OF CV ALPHA PARAMETER CALIBRATION CLASS ##########
# Cover Vegetation Coefficient 
    
  # Load array data list from global or local file with name file veg_param
  # Active one of these parameters to choose local or global file as your vegetation parameter path

  # Active path from global file
   
#fglob_vp = arr_globalfile[138,1] # Save vegetation parameter path into a variable
#fglist_vp = glob.glob(flist_vp) # Load path from globalfile_vp

  # Active path from local file

floc_vp = arr_local[2,1] # Save vegetation parameter path into a variable
flist_vp = glob.glob(floc_vp) # Load path from localfile_vp

cols_vp = [0,1] # Index 0 is Grid and Classes and Index 1 is Class Nominal and Class Fraction
  
  # Read certain columns with Pandas Module

df_vp = pd.DataFrame()
for f_vp in flist_vp:
    df_vp = df_vp.append(pd.read_csv
            (f_vp, delimiter='\s+', header=None, usecols=cols_vp, na_values=['']),
            ignore_index=True)
arr_vp = df_vp.values

  # Writing list into a file

cv_output = "../output/erosion/tempfiles/cv/cv.txt"
with open(cv_output, 'w') as f_vp:
    f_vp.write(np.array2string(arr_vp, separator=' '))

  # Save vegetation parameter array into a variable

with open(cv_output) as var_cv:
    variable_cv = var_cv.read()
    strvariable_cv = str(variable_cv)

  # Save vegetation parameter array and also remove the bracket then write it into a file

with open(cv_output,"w") as rmbd_cv:
    rmb_vp1 = strvariable_cv.replace('[[ ','')
    rmb_vp2 = rmb_vp1.replace(' [ ','')
    rmb_vp3 = rmb_vp2.replace(']','')
    rmb_vp4 = rmb_vp3.replace(']]','')
    rmd_an = re.compile("(?<=\d)(\.)(?!\d)")
    rmb_vp5 = rmd_an.sub("",rmb_vp4)
    rmbd_cv.write(rmb_vp5)

  # Split the list into strings and lines

with open(cv_output) as str2lst_cv:
    strtolist_cv = str(str2lst_cv.read()) # Convert the list into string
    cv_perline = strtolist_cv.rstrip().splitlines() # Split the list per row line
    cv_pernumber = strtolist_cv.split() # Split the list into per string

  # Get data content of second column in cv.txt

nclass = cv_pernumber[1::2] 
str_nclass = str(nclass)
rep_nclass = str_nclass.replace("'1', '1'","'1', '0.99999'")
rep_nclass = rep_nclass.replace("['","")
rep_nclass = rep_nclass.replace("']","")
rep_nclass = rep_nclass.replace("', '"," ")
spt_nclass = rep_nclass.split()

  # Get the quantity of classes per grid

qclasses = list() # Generate empty list called qclasses
for qclass in spt_nclass: # Its mean every single data in nclass variable
    # Selection the data, everything starts with "0" will be removed
    prefix_zero = 0
    if qclass.startswith(str(prefix_zero)):
        pass
    else:
        qclasses.append(qclass)

  # If the grid has only 1 class and the value of cv fraction is 1, execute script below
  
str_qclasses = str(qclasses)
prefix_one = str_qclasses.replace("'1.', '1.'","'1.'") # qClasses 1 with cv value = 1 (other format)
#prefix_one = str_qclasses.replace("'1', '1'","'1'") # qClasses 1 with cv value = 1
rid_the_dot = re.sub("[\.]","",prefix_one)
qclasses_new = re.findall(r'\d+', rid_the_dot)

  # Save the iterated lines into a variable

cquantity = list()
for quantity in qclasses_new:
    class_quantity = int(quantity)+1
    cquantity.append(class_quantity)

  # Grab the grid as filename

cvname = list()
with open(floc_gll) as fn_sepdgridclass:
    fn_cvout = fn_sepdgridclass.read()
    fn_cvout = fn_cvout.split('\n')
    for each_fncvout in fn_cvout:
        ff = each_fncvout.split(' ')
        cvname.append(ff[1])

  # Write the selected lines into files

with open(cv_output,"r") as mycvfile:
    for name, N in zip(cvname, cquantity):
        head = list(islice(mycvfile, N))
        cv_from_main = "../output/erosion/tempfiles/cv/"
        with open(cv_from_main+name,"w") as s:
            s.writelines(head)

  # Save file's contents into variable

vcv = list()
for varlst_cv in os.listdir(cv_from_main):
    if varlst_cv.startswith("cv"):
        pass
    else:
        rvarlst_cv = open(cv_from_main+varlst_cv,"r")
        rcvarlst_cv = str(rvarlst_cv.read())
        rrowvarlst_cv = rcvarlst_cv.split()
        vcv.append(rrowvarlst_cv[2::])

# Alpha Parameter
  
  # Change directory into input alpha folder

alpha_from_root = "../input/alpha/"
#os.chdir(alpha_from_root)

'''
  # Get and create file of alpha
  
with open("data_alpha.txt","w") as wf_alpha:
    for cveg in range(1,14):
        wf_alpha.writelines("%i \n" %cveg)
root_from_alpha = "../../main/"
os.chdir(root_from_alpha)

  # Show pop up dialog to user for filling alpha value

print("\nPlease fill the Alpha values in Alpha directory!")
question_alpha = input("\nIf You have already completed it, Press Y to continue or press N to exit! ")
if question_alpha.lower().startswith("y"):
    print("\nPlease wait a moment...")
elif question_alpha.lower().startswith("n"):
    exit()
'''

  ### Copy alpha file into output temporary files for erosion (/output/erosion/tempfiles/a) ###

srcp_alpha = alpha_from_root
destp_alpha = '../output/erosion/tempfiles/a/'
srcf_alpha = os.listdir(srcp_alpha)
for fl_alpha in srcf_alpha:
    f_alpha = os.path.join(srcp_alpha, fl_alpha)
    if (os.path.isfile(f_alpha)):
        shutil.copy(f_alpha, destp_alpha)
        
  # Save file's contents into variable

va = list()
for varlst_a in os.listdir(destp_alpha):
    rvarlst_a = open(destp_alpha+varlst_a,"r")
    rcvarlst_a = str(rvarlst_a.read())
    rrowvarlst_a = rcvarlst_a.split()
    va.append(rrowvarlst_a)

# Calibration Parameter

  # Split alpha list every 2 elements
  # Split cover vegetation every 2 elements
  # Dictionary with same key will be combined or merged
  # Multiply in every single key and sum up to get calibration parameter

for a in va:
    try:
        complist_alpha = [a[x:x+2] for x in range(0, len(a), 2)]
        dict_alpha = dict(complist_alpha)
    except:
        continue

cp = list()

for cv in vcv:
    try:
        complist_cover_vegetation = [cv[x:x+2] for x in range(0, len(cv),2)]
        dict_cover_vegetation = dict(complist_cover_vegetation)
        dict_combine = {k: [dict_cover_vegetation[k],dict_alpha[k]] for k in dict_cover_vegetation}
        for key in dict_combine.keys():
            dict_combine[key] = [float(dict_combine[key][0]),float(dict_combine[key][1])]
        muldict_combine = {key: reduce(mul, value) for key, value in dict_combine.items()}
        summuldict_combine = sum(muldict_combine.values())
        cp.append("%.5f" %summuldict_combine)
    except:
        print("\nERROR-UIA\n\nIt seems You forgot something.\n")
        print("Make sure You fill all the Alpha values.\n")
        print("If in a class the value is not avaliable just type 0.")
        exit()
########## HERE IS THE LAST SECTION OF CV ALPHA PARAMETER CALIBRATION CLASS ##########

########## HERE IS THE INITIAL SECTION OF MULTIPLICATION OF ALPHA AND RAINFALL INTENSITY SQUARE CLASS ##########
# Reload Rainfall Intensity

  # Load file's contents of rainfall intensity into variable

rainfall_intensity = list()
for varlst_ri in os.listdir(destp_ri):
    if varlst_ri.startswith("data"):
        rvarlst_ri = open(destp_ri+"/"+varlst_ri,"r")
        rcvarlst_ri = str(rvarlst_ri.read())
        rrowvarlst_ri = rcvarlst_ri.split()
        rainfall_intensity.append(rrowvarlst_ri)

# Matrix Multiplication
  
  # Multiplication of Squared Rainfall Intensity with Calibration Parameter

mm_from_main = "../output/erosion/tempfiles/mm/"
for name4splasherosion, irain, pc in zip(os.listdir(destp_ri), rainfall_intensity, cp):
    array_pc = np.array(pc, dtype=float)
    array_rain = np.array(irain, dtype=float)
    result = array_pc * array_rain
    if name4splasherosion.startswith("data_"):
        with open(mm_from_main+name4splasherosion,"w") as results:
            results.write(np.array2string(result,separator='\n', formatter={'float_kind':lambda result: "%.30f" % result}))
        
# Loading animation

print(" ")
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write("\rCalculating splash erosion " + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n\nDone! Identifying sheet erosion data...\n')
t = threading.Thread(target=animate)
t.start()
time.sleep(10)
done = True
########## HERE IS THE LAST SECTION OF MULTIPLICATION OF ALPHA AND RAINFALL INTENSITY SQUARE CLASS ##########

########## HERE IS THE INITIAL SECTION OF SPLASH EROSION REPORT CLASS ##########
# SPLASH EROSION REPORT

  ### REPORT THE CALCULATION ###

  # Print path of splash erosion filename list into a file named content_se.txt
  
floc_content_se = "../output/erosion/tempfiles/ri/content_se.txt" # Save file path into a variable
each_content_se = open(floc_content_se, "w") # Open write mode with metode below:
for item_se in os.listdir(root_splasherosion): # Make a list of splash erosion filename
    content_se = root_splasherosion+"/"+str(item_se) # Save full path of splash erosion files into a variable called content_se
    s_content_se = str(content_se) # Convert into string class
    each_content_se.write("%s\n" %s_content_se) # Write the list into content_se.txt
    #print(item_se) # Print list of filename
    #print(s_content_se) # Print full path of filename list
each_content_se.close() # Close function
loc_content_se = open(floc_content_se,"r") # Open read mode with floc_content-se as location of filename list
data_content_se = loc_content_se.read().splitlines() # Read per line and save it into variable (list)
#print(data_content_se)

  # Print path of splash erosion filename list into a file named content_splsherosion.txt
  
root_splsherosion = mm_from_main # Root for splas herosion data file
floc_content_splsherosion = "../output/erosion/tempfiles/mm/content_splsherosion.txt"  # Save file path into a variable
each_content_splsherosion = open(floc_content_splsherosion, "w") # Open write mode with metode below:
for item_splsherosion in os.listdir(root_splsherosion): # Make a list of splash erosion filename
    if re.match("data_",item_splsherosion): # If the content of folder mm has initial name "data_" so they would be printed and save them into a variable
        content_splsherosion = root_splsherosion+"/"+str(item_splsherosion) # Save full path of splash erosion files into a variable called content_splsherosion.txt
        s_content_splsherosion = str(content_splsherosion) # Convert into string class
        each_content_splsherosion.write("%s\n" %s_content_splsherosion)  # Write the list into content_splsherosion.txt
        #print(item_ri) # Print list of filename
        #print(content_ri) # Print full path of filename list
each_content_splsherosion.close() # Close function
loc_content_splsherosion = open(floc_content_splsherosion,"r") # Open read mode with floc_content_splsherosion as location of filename list
data_content_splsherosion = loc_content_splsherosion.read().splitlines() # Read per line and save it into variable (list)
#print(data_content_ri)

  # Read each file's content of splasherosion

sd_gll = []
for grid_ll in data_content_se:
    read_grid_ll = open(grid_ll,"r")
    plread_grid_ll = read_grid_ll.read()
    rplgll = plread_grid_ll.rstrip().split('\n')
    sd_gll.append(rplgll)
    #print(rplgll)
# print(sd_gll)

  # Read each file's content of rainfall intensity

sd_splsherosion = []
for rain_splsherosion in data_content_splsherosion:
    read_rain_splsherosion = open(rain_splsherosion,"r")
    plread_rain_splsherosion = read_rain_splsherosion.read()
    rplrainisplsherosion = plread_rain_splsherosion.rstrip().split('\n')
    sd_splsherosion.append(rplrainisplsherosion)
    #print(rplraini)
#print(sd_ri)

  # Merge to the Report

report = []
for i in itertools.zip_longest(sd_gll,sd_splsherosion):
    str_se_done = str(i)
    report.append("%s\n" %str_se_done)
locse_report = "../output/erosion/tempfiles/se/report.txt"
with open(locse_report,"w") as report_se:
    report_se.writelines(report)

  # Read splasherosion filenames

fnfl_gll = []
for se_nameit in os.listdir(root_splasherosion):
    fnfl_gll.append(se_nameit)
#print(fnfl_gll)

  # Write combined data into each splasherosion files          
  
def grouper(n, iterable, fillvalue=None): # Definition function for grouping
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, * args)

n = 1 # How many lines will be read and write into a file?
    
dst_of_se = '../output/erosion/splasherosion/splsherosion_{0}' # Report file location and definition splasherosion filename

with open(locse_report) as f: # Write lists of filename into file
    for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
        with open(dst_of_se.format(i * n), 'w') as fout:
            # Remove brackets from gll string list
            str_g = str(g)
            rone1 = str_g.replace('("(','')
            rtwo2 = rone1.replace("['  ",'')
            rthree3 = rtwo2.replace("'], ['",'\t\t')
            rfour4 = rthree3.replace("', '",'\n\t\t\t\t\t\t\t\t\t\t')
            rfive5 = rfour4.replace("'","")
            rsix6 = rfive5.replace("]","")
            rseven7 = rsix6.replace(")","")
            reight8 = rseven7.replace('n",',"")
            rnine9 = reight8.replace('\\','')
            rten10 = rnine9.replace('[','')
            fout.writelines(rten10)

  # Rename splasherosion_[number] to be se_[lat]_[lon]

path_splsherosion = []
for item_splasherosion in os.listdir(root_splasherosion):
    if item_splasherosion.startswith("splsherosion"):
        fullpath_splasherosion1 = os.path.join(root_splasherosion, item_splasherosion)
        path_splsherosion.append("%s" %fullpath_splasherosion1)
path_se = []
for item_splasherosion in os.listdir(root_splasherosion):
    if item_splasherosion.startswith("se_"):
        fullpath_splasherosion2 = os.path.join(root_splasherosion, item_splasherosion)
        path_se.append("%s" %fullpath_splasherosion2)
t = len(path_se)
for i in range(0,t):
    shutil.move(path_splsherosion[i], path_se[i])
########## HERE IS THE LAST SECTION OF SPLASH EROSION REPORT CLASS ##########        
########## HERE IS THE LAST SECTION OF SPLASH EROSION CLASS ##########

########## HERE IS THE INITIAL SECTION OF REPORT REVISION CLASS ##########        
# REPORT REVISION

  # Grab and rename the file name

mm_from_main = "../output/erosion/tempfiles/mm/"
se_from_main = "../output/erosion/splasherosion/"
filename_se = list()
for rev_se in os.listdir(mm_from_main):
    if rev_se.startswith("data"):
        new_rev_se = rev_se.replace("data","se")
        filename_se.append(new_rev_se)
splasherosion_new = list()
for cont_se in os.listdir(mm_from_main):
    if cont_se.startswith("data"):
        with open(mm_from_main+cont_se,"r") as cse:
            cse_read = str(cse.read())
            cse_rep = cse_read.replace("[","")
            cse_rep = cse_rep.replace("]","")
            cse_spl = cse_rep.split()
            splasherosion_new.append(cse_spl)
for fn_se, se_new in zip(filename_se, splasherosion_new):
    with open(se_from_main+fn_se,"w") as fse:
        for senew in se_new:
            float_senew = float(senew)
            fse.writelines("%.30f\n" %float_senew)
########## HERE IS THE LAST SECTION OF REPORT REVISION CLASS ##########