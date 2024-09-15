# script_name.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by First Last
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys
import math
# "constants"
# e.g., R_E_KM = 6378.13700
R_E_KM = 6378.13630
E_E    = 0.081819221456
# helper functions

## function description
# def calc_something(param1, param2):
#   pass
def calc_denom(ecc,lat_rad):
    return math.sqrt(1.0-(ecc**2)*(math.sin(lat_rad)**2))

# initialize script arguments
lon_deg=float('nan')
lat_deg=float('nan')
hae_km=float('nan')

# parse script arguments
if len(sys.argv)==4:
    lat_deg = float(sys.argv[1])
    lon_deg = float(sys.argv[2])
    hae_km = float(sys.argv[3])
else:
   print(\
      'Usage: '\
        'python3 llh_to_ecef.py lon_deg lat_deg hae_km'\
     )
   exit()

#lon_rad=lon_deg*math.pi/180
#lat_rad=lat_deg*math.pi/180
lat_rad=math.radians(lat_deg)
lon_rad=math.radians(lon_deg)

denom = calc_denom(E_E,lat_rad)
c_E=R_E_KM/denom
s_E=R_E_KM*(1-(E_E**2.0))/denom
r_x_km=(c_E+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y_km=(c_E+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
#r_z_km=(s_E+hae_km)*math.sin(lat_rad)
r_z_km=(c_E * (1 -E_E**2)+hae_km)*math.sin(lat_rad)
print(r_x_km)
print(r_y_km)
print(r_z_km)
