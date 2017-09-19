#!/usr/bin/python

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

# IMPORT MODULE

import os
import pyfiglet

# SHOW HEADER

pyfiglet.print_figlet("STEP",font="lean",justify="center")
pyfiglet.print_figlet("Sediment Transport & Erosion Prediction",font="digital",justify="center")
version = " Version 2.7.0 ";
print("{1:^75}".format(" ",version))
print(" ")

# PATHS

pmain = "../../main/"
palpha = "../input/alpha/"
pdiameter = "../input/diameter/"
pepsilon = "../input/epsilon/"
perodibility = "../input/erodibility/"
pforcing = "../input/forcing/"
pgammas = "../input/gammas/"
pgridlatlon = "../input/gridlatlon/"
pgridslope = "../input/gridslope/"
pmanning = "../input/manning/"
pomega = "../input/omega/"
pparameter = "../input/parameter/"
prunoff = "../input/runoff/"
pvegparam = "../input/vegparam/"
pviscosity = "../input/viscosity/"
lendata = "../forcing/"

# ALPHA

  # Save file's contents into variable

os.chdir(palpha)
alpha = list()
for varlst_alpha in os.listdir("."):
    if varlst_alpha.startswith("data_alpha"):
        rvarlst_alpha = open(varlst_alpha,"r")
        rcvarlst_alpha = str(rvarlst_alpha.read())
        rrowvarlst_alpha = rcvarlst_alpha.split()
        alpha.append(rrowvarlst_alpha) 
    
  # Check if User has already filled every single grid slope values
  # Save the value into a variable list 'value_slope'

split_alpha = ((str(alpha)).split())
if len(split_alpha) == 2*13:
    for a in alpha:
        complist_alpha = [a[x:x+2] for x in range(0, len(a), 2)]
        dict_alpha = dict(complist_alpha)
        value_alpha = list(dict_alpha.values())
else:
    print("\nERROR-UIA\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Alpha values.\n")
    print("If in a class the value is not avaliable just type 0.\n")
    exit()
print("\nAlpha OK!")
os.chdir(pmain)

# DIAMATER

  # Save file's contents into variable

os.chdir(pdiameter)
diameter = list()
for varlst_diameter in os.listdir("."):
    if varlst_diameter.startswith("diameter"):
        rvarlst_diameter = open(varlst_diameter,"r")
        rcvarlst_diameter = str(rvarlst_diameter.read())
        rrowvarlst_diameter = rcvarlst_diameter.split()
        diameter.append(rrowvarlst_diameter) 
    
  # Check if User has already filled every single diameter values
  # Save the value into a variable list 'value_diameter'

split_diameter = ((str(diameter)).split())
if len(split_diameter) == 2*(len([name for name in os.listdir(lendata) if os.path.isfile(os.path.join(lendata, name))])):
    for d in diameter:
        complist_diameter = [d[x:x+2] for x in range(0, len(d), 2)]
        dict_diameter = dict(complist_diameter)
        value_diameter = list(dict_diameter.values())
else:
    print("\nERROR-UID\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Diameter values.\n")
    print("If in a grid the value is not avaliable just type 0.\n")
    exit()
print("\nAverage Sediment Diameter OK!")
os.chdir(pmain)

# EPSILON

  # Save file's contents into variable

os.chdir(pepsilon)
epsilon = list()
for varlst_epsilon in os.listdir("."):
    if varlst_epsilon.startswith("epsilon"):
        rvarlst_epsilon = open(varlst_epsilon,"r")
        rcvarlst_epsilon = str(rvarlst_epsilon.read())
        rrowvarlst_epsilon = rcvarlst_epsilon.split()
        epsilon.append(rrowvarlst_epsilon) 
    
  # Check if User has already filled every single epsilon values
  # Save the value into a variable list 'value_epsilon'

split_epsilon = ((str(epsilon)).split())
if len(split_epsilon) == 2*(len([name for name in os.listdir(lendata) if os.path.isfile(os.path.join(lendata, name))])):
    for eps in epsilon:
        complist_epsilon = [eps[x:x+2] for x in range(0, len(eps), 2)]
        dict_epsilon = dict(complist_epsilon)
        value_epsilon = list(dict_epsilon.values())
else:
    print("\nERROR-UIEPS\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Epsilon values.\n")
    print("If in a grid the value is not avaliable just type 0.\n")
    exit()
print("\nEpsilon OK!")
os.chdir(pmain)

# ERODIBILITY

  # Save file's contents into variable

os.chdir(perodibility)
erodibility = list()
for varlst_erodibility in os.listdir("."):
    if varlst_erodibility.startswith("erodibility"):
        rvarlst_erodibility = open(varlst_erodibility,"r")
        rcvarlst_erodibility = str(rvarlst_erodibility.read())
        rrowvarlst_erodibility = rcvarlst_erodibility.split()
        erodibility.append(rrowvarlst_erodibility) 
    
  # Check if User has already filled every single erodibility values
  # Save the value into a variable list 'value_erodibility'

split_erodibility = ((str(erodibility)).split())
if len(split_erodibility) == 2*(len([name for name in os.listdir(lendata) if os.path.isfile(os.path.join(lendata, name))])):
    for e in erodibility:
        complist_erodibility = [e[x:x+2] for x in range(0, len(e), 2)]
        dict_erodibility = dict(complist_erodibility)
        value_erodibility = list(dict_erodibility.values())
else:
    print("\nERROR-UIE\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Erodibility values.\n")
    print("If in a grid the value is not avaliable just type 0.\n")
    exit()
print("\nErodibility OK!")
os.chdir(pmain)

# SPECIFIC WEIGHT OF SEDIMENTS

  # Save file's contents into variable

os.chdir(pgammas)
gammas = list()
for varlst_gammas in os.listdir("."):
    if varlst_gammas.startswith("gammas"):
        rvarlst_gammas = open(varlst_gammas,"r")
        rcvarlst_gammas = str(rvarlst_gammas.read())
        rrowvarlst_gammas = rcvarlst_gammas.split()
        gammas.append(rrowvarlst_gammas) 
    
  # Check if User has already filled every single gammas values
  # Save the value into a variable list 'value_gammas'

gamma = 1000
split_gammas = ((str(gammas)).split())
if len(split_gammas) == 2*(len([name for name in os.listdir(lendata) if os.path.isfile(os.path.join(lendata, name))])):
    for gs in gammas:
        complist_gammas = [gs[x:x+2] for x in range(0, len(gs), 2)]
        dict_gammas = dict(complist_gammas)
        value_gammas = list(dict_gammas.values())
        for vgs in value_gammas:
            if float(vgs) > float(gamma):
                pass
            elif float(vgs) < float(gamma):
                print("\nERROR-UIGS\n\nYour gamma sediment value is less than gamma water\n")
                exit()
else:
    print("\nERROR-UIGS\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Gamma Sediment values.\n")
    print("If in a grid the value is not avaliable just type 0.\n")
    exit()
print("\nGamma Sediment OK!")
os.chdir(pmain)

# GRID SLOPE

  # Save file's contents into variable

os.chdir(pgridslope)
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
if len(split_slope) == 2*(len([name for name in os.listdir(lendata) if os.path.isfile(os.path.join(lendata, name))])):
    for s in slope:
        complist_slope = [s[x:x+2] for x in range(0, len(s), 2)]
        dict_slope = dict(complist_slope)
        value_slope = list(dict_slope.values())
else:
    print("\nERROR-UIS\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Slope values.\n")
    print("If in a grid the value is not avaliable just type 0.\n")
    exit()
print("\nGrid Slope OK!")
os.chdir(pmain)

# MANNING

  # Save file's contents into variable

os.chdir(pmanning)
manning = list()
for varlst_manning in os.listdir("."):
    if varlst_manning.startswith("manning"):
        rvarlst_manning = open(varlst_manning,"r")
        rcvarlst_manning = str(rvarlst_manning.read())
        rrowvarlst_manning = rcvarlst_manning.split()
        manning.append(rrowvarlst_manning) 
    
  # Check if User has already filled every single grid manning values
  # Save the value into a variable list 'value_manning'

split_manning = ((str(manning)).split())
if len(split_manning) == 2*(len([name for name in os.listdir(lendata) if os.path.isfile(os.path.join(lendata, name))])):
    for n in manning:
        complist_manning = [n[x:x+2] for x in range(0, len(n), 2)]
        dict_manning = dict(complist_manning)
        value_manning = list(dict_manning.values())
else:
    print("\nERROR-UIN\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Manning values.\n")
    print("If in a grid the value is not avaliable just type 0.\n")
    exit()
print("\nManning OK!")
os.chdir(pmain)

# OMEGA

  # Save file's contents into variable

os.chdir(pomega)
omega = list()
for varlst_omega in os.listdir("."):
    if varlst_omega.startswith("omega"):
        rvarlst_omega = open(varlst_omega,"r")
        rcvarlst_omega = str(rvarlst_omega.read())
        rrowvarlst_omega = rcvarlst_omega.split()
        omega.append(rrowvarlst_omega) 
    
  # Check if User has already filled every single grid omega values
  # Save the value into a variable list 'value_omega'

split_omega = ((str(omega)).split())
if len(split_omega) == 2*(len([name for name in os.listdir(lendata) if os.path.isfile(os.path.join(lendata, name))])):
    for o in omega:
        complist_omega = [o[x:x+2] for x in range(0, len(o), 2)]
        dict_omega = dict(complist_omega)
        value_omega = list(dict_omega.values())
        for vo in value_omega:
            if 1.20 < float(vo) < 1.50:
                pass
            elif float(vo) < 1.20 :
                print("\nERROR-UIO\n\nYour Omega value is less than 1.2\n")
                exit()
            elif float(vo) > 1.50:
                print("\nERROR-UIO\n\nYour Omega value is greater than 1.5\n")
                exit()  
else:
    print("\nERROR-UIO\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Omega values.\n")
    print("If in a grid the value is not avaliable just type 0.\n")
    exit()
print("\nOmega OK!")
os.chdir(pmain)

# VISCOSITY

os.chdir(pviscosity)
viscosity = list()
for varlst_viscosity in os.listdir("."):
    if varlst_viscosity.startswith("viscosity"):
        rvarlst_viscosity = open(varlst_viscosity,"r")
        rcvarlst_viscosity = str(rvarlst_viscosity.read())
        rrowvarlst_viscosity = rcvarlst_viscosity.split()
        viscosity.append(rrowvarlst_viscosity) 
    
  # Check if User has already filled every single grid viscosity values
  # Save the value into a variable list 'value_viscosity'

split_viscosity = ((str(viscosity)).split())
if len(split_viscosity) == 2*(len([name for name in os.listdir(lendata) if os.path.isfile(os.path.join(lendata, name))])):
    for v in viscosity:
        complist_viscosity = [v[x:x+2] for x in range(0, len(v), 2)]
        dict_viscosity = dict(complist_viscosity)
        value_viscosity = list(dict_viscosity.values())
else:
    print("\nERROR-UIV\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Viscosity values.\n")
    print("If in a grid the value is not avaliable just type 0.\n")
    exit()
print("\nViscosity OK!")
os.chdir(pmain)

# FORCING

  # Save file's contents into variable

os.chdir(pforcing)
forcing = list()
for varlst_forcing in os.listdir("."):
    if varlst_forcing.startswith("data"):
        rvarlst_forcing = open(varlst_forcing,"r")
        rcvarlst_forcing = str(rvarlst_forcing.read())
        rrowvarlst_forcing = rcvarlst_forcing.split()
        forcing.append(rrowvarlst_forcing) 
   
  # Check if User has already filled every single forcing values
  # Save the value into a variable list 'value_forcing'

split_forcing = ((str(forcing)).split())
if len(forcing[0]) == (len(forcing[0][0::4]))*4:
    for r in forcing:
        complist_forcing = [r[x:x+4] for x in range(0, len(r), 4)]
else:
    print("\nERROR-UIF\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the Forcing values.\n")
    print("If in a grid the value is not avaliable just type 0.\n")
    exit()
print("\nForcing OK!")
os.chdir(pmain)

# GRID LATITUDE LONGITUDE

  # Save file's contents into variable

os.chdir(pgridlatlon)
gridlatlon = list()
for varlst_gridlatlon in os.listdir("."):
    if varlst_gridlatlon.startswith("soil"):
        rvarlst_gridlatlon = open(varlst_gridlatlon,"r")
        rcvarlst_gridlatlon = str(rvarlst_gridlatlon.read())
        rrowvarlst_gridlatlon = rcvarlst_gridlatlon.split()
        gridlatlon.append(rrowvarlst_gridlatlon) 

  # Check if User has already filled every single gridlatlon values
  # Save the value into a variable list 'value_gridlatlon'

split_gridlatlon = ((str(gridlatlon)).split())
if len(gridlatlon[0]) == (len(gridlatlon[0][0::11]))*11:
    for gll in gridlatlon:
        complist_gridlatlon = [gll[x:x+2] for x in range(0, len(gll), 2)]
else:
    print("\nERROR-UILL\n\nIt seems You forgot something.\n")
    print("Make sure You fill all the soil parameter values.\n")
    print("If in a grid the value is not avaliable just type 0.\n")
    exit()
print("\nSoil Parameter OK!\n")
os.chdir(pmain)