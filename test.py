# Import
import numpy as np

# Constants
P0 = 101325  # sea-level standard atmospheric pressure (Pa)
L = 0.0065   # temperature lapse rate (K/m)
T0 = 288.15  # sea-level standard temperature (K)
G = 9.8      # acceleration due to gravity (m/s²)
M = 0.029    # molar mass of Earth's air (kg/mol)
R = 8.314    # universal gas constant (J/(mol·K))
CPD = 1005   # Specific heat of dry air at constant pressure (J/(kg*K))
CPV = 1870   # Specific heat of water vapor at constant pressure (J/(kg*K))
RD = 287     # Specific gas constant for dry air (J/(kg*K))
RV = 461     # Specific gas constant for water vapor (J/(kg*K))

def interpolate_lapse_rate(alt, malr, dalr, transition_alt, transition_range):
    """
    Helper Function

    Interpolate lapse rate between MALR and DALR based on altitude
    """

    # Determine if altitude has been reached to transition away from the MALR
    if alt <= transition_alt:
        lapse_rate = malr
    else:
        lapse_rate = malr - ((malr - dalr) / transition_range) * (alt - transition_alt) # Gradually move to DALR as you ascend

    return lapse_rate

def moist_adiabatic_lapse_rate(temp_C, dewp_C, pressure_hPa, mixing_ratio):
    """
    Helper Function

    Calculate the moist adiabatic lapse rate
    """

    return ((CPD + (CPV * mixing_ratio)) / ((1 + (CPV / CPD) * mixing_ratio) * virtual_temp(temp_C, dewp_C, pressure_hPa))) / 1000

def virtual_temp(temp_C, dewp_C, pressure_hPa):
    """
    Helper Function

    Calculate virtual temperature
    """

    return (temp_C + 273.15) / (1 - 0.379 * ((6.11 * (10 ** ((7.5 * dewp_C) / (237.7 + dewp_C)))) / pressure_hPa))

def pressure_at_altitude(altitude):
    """
    Helper Function

    Calculate pressure at specified altitude
    """

    return P0 * (1 - L * altitude / T0) ** (G * M / (R * L)) / 100

# Test values
sfc_temp_C = 31.30
sfc_dewp_C = 25.90
sfc_temp_K = sfc_temp_C + 273.15
sfc_dewp_K = sfc_dewp_C + 273.15
sfc_pres_hPa = 985.0
sfc_height = 170  # In meters at the surface
transition_alt = 1000   # Replace with the altitude where you want the transition to occur
transition_range = 11750 # Where you want the transition to start

# Thermodynamic variables
malr = 6.5 / 1000 # Moist adiabatic lapse rate (6.5K per km)
dalr = 9.8 / 1000 # Dry adiabatic lapse rate (9.8K per km)
adj_err = 1.33    # Correct for temperature of LCL error

# Estimate the LCL properties
t_LCL = (sfc_dewp_K - ((0.001296 * sfc_dewp_K) + 0.1963) * (sfc_temp_K - sfc_dewp_K)) + adj_err # Temperature of LCL
z_LCL = sfc_height + (sfc_temp_K - t_LCL) / malr # Height of LCL in meters

# Original formula
e_s = 6.11 * 10**((7.5 * sfc_temp_C) / (237.7 + sfc_temp_C))

# Calculate mixing ratio
mixing_ratio = 621.97 * (e_s / (sfc_pres_hPa - e_s))

# Testing different temperature values here
virtual_temp_K = virtual_temp(sfc_temp_C, sfc_dewp_C, sfc_pres_hPa)

# Start parcel temp for the parcel trace
parcel_temp_K = virtual_temp_K

# Calculate the actual MALR using the parcel temperature and mixing ratio
malr = moist_adiabatic_lapse_rate(sfc_temp_C, sfc_dewp_C, sfc_pres_hPa, mixing_ratio)

# Initialize the list for parcel data
parcel_data = []

resolution = 100

# Adiabatically lift the parcel
for alt_value in range(int(sfc_height), 16000, resolution):
    # Add the data of the parcel to the list of dictionaries
    parcel_data.append({
        'temperature': parcel_temp_K - 273.15,
        'height': alt_value,
        'pressure': pressure_at_altitude(alt_value)
    })

    print(malr)

    lapse_rate = interpolate_lapse_rate(alt_value, malr, dalr, transition_alt, transition_range)

    # Ensure that the lapse rate doesn't exceed the DALR
    lapse_rate = min(lapse_rate, dalr)

    # Print the parcel temperature for each iteration
    print(f'Parcel Temperature at {alt_value} meters: {round(parcel_temp_K - 273.15, 0)}°C')
    print(f'Instantaneous Lapse Rate at {alt_value} meters: {lapse_rate}')

    # Cool the parcel as it rises
    if alt_value <= z_LCL:
        # Dry adiabatic lapse rate
        parcel_temp_K -= dalr * resolution  # Ascending parcel to LCL
    else:
        # Moist adiabatic lapse rate
        parcel_temp_K -= lapse_rate * resolution # Parcel beyond LCL, adjust lapse rate for parcel