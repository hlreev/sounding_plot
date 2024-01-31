'''
Thermo Module

Calculates the physics/thermodynamics needed to plot a parcel trace on each sounding
'''

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

def plot_parcel_trace(temp_C, dewp_C, pres):
    """
    Helper Function

    To plot the parcel trace and find the LCL for each sounding.
    """

    # Surface observations (converted to from degreeC to K)
    sfc_temp_C = temp_C[0]
    sfc_dewp_C = dewp_C[0]
    sfc_pres_hPa = pres[0]
    sfc_height = 170  # In meters at the surface

    # Thermodynamic variables
    dalr = 9.8 / 1000 # Dry adiabatic lapse rate (9.8K per km)

    # Calculate saturation vapor pressure at current parcel temp
    e_s = 6.11 * 10 ** ((7.5 * sfc_temp_C) / (237.7 + sfc_temp_C))

    # Calculate mixing ratio using specific humidity
    mixing_ratio = 621.97 * (e_s / (sfc_pres_hPa - e_s))

    # Testing different temperature values here
    virtual_temp_K = virtual_temp(sfc_temp_C, sfc_dewp_C, sfc_pres_hPa)

    # Calculate the actual MALR using the parcel temperature and mixing ratio
    malr = moist_adiabatic_lapse_rate(sfc_temp_C, sfc_dewp_C, sfc_pres_hPa, mixing_ratio)

    # Estimate the LCL properties
    z_LCL = ((sfc_temp_C - sfc_dewp_C) / 10) * 1247 + sfc_height

    # Adjust the parcel trace adjustment for MALR to DALR
    transition_alt = 1000   # Replace with the altitude where you want the transition to occur
    transition_range = 11750 # Where you want the transition to start

    # Initialize data for parcel trace
    parcel_data = []
    lapse_rates = []
    resolution = 100 # Data resolution in meters
    parcel_temp_K = virtual_temp_K

    # Adiabatically lift the parcel
    for alt_value in range(int(sfc_height), 16000, resolution):
        # Add the data of the parcel to the list of dictionaries
        parcel_data.append({
            'temperature': parcel_temp_K - 273.15,
            'height': alt_value,
            'pressure': pressure_at_altitude(alt_value)
        })

        # Check if the current altitude is below or at the LCL
        if alt_value <= z_LCL:
            # Use DALE
            lapse_rate = dalr 
        else:
            lapse_rate = interpolate_lapse_rate(alt_value, malr, dalr, transition_alt, transition_range)

        # Ensure that the lapse rate doesn't exceed the DALR
        lapse_rate = min(lapse_rate, dalr)
        lapse_rates.append(lapse_rate)

        # Cool the parcel as it rises
        parcel_temp_K -= lapse_rate * resolution  # Adjust lapse rate for 

    return parcel_data

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