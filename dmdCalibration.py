import numpy as np

# Give input
alpha_degree = 32.

# Constants for calibration, please adjust if needed
distance_between_posts_in_laser_direction = 212       #distance between the posts following the laser's axis
distance_lens1_pole1 = 145                            #distance between the last lens (before reaching the DMD) and the pole following the laser's axis)
distance_lens1_dmd_laserdir = 200                     #distance between the last lens and the DMD's surface (following the laser beam)
dmd_height = 153                                      #distance between the breadboard and the center of the DMD
rail_height = 10                                      #distance between the breadboard and the top of the rail

# Transformation into radians
theta = 12. / 180 * np.pi
alpha = alpha_degree / 180 * np.pi

# Calculate 1D angles
theta_1D = np.arctan(np.tan(theta) / np.sqrt(2))
alpha_1D = np.arctan(np.tan(alpha) / np.sqrt(2))

# Calculate reflection angle correction
beta_1D = 2*theta_1D - alpha_1D     #beta_1D is the correction needed to be applied to the DMD so that the reflected beam's orientation is horizontal
beta = np.arctan(np.tan(beta_1D) * np.sqrt(2))
beta / np.pi * 180

# Adjust incident angle to maintain diffraction configuration
alpha_1D -= beta_1D

# Print results
print("Tilt the dmd by ",-beta/np.pi*180,"in both the vertical and horizontal axis")    #in our case, positive means backwards (seen from the right-hand profile) and counter-clockwise (seen from the top)
print("alpha_1D is ", alpha_1D/np.pi*180)  #both the horizontal and vertical incident angle

# Initialization of variables
distance_between_poles_ground = 0
pole_1_height = 0
pole_2_height = 0

delta = dmd_height - rail_height

# Calculate distances and heights
distance_between_poles_ground = np.cos(alpha_1D) * distance_between_posts_in_laser_direction
print("The distance between the poles is:",distance_between_poles_ground)

distance_lens1_dmd_ground = np.cos(alpha_1D) * (distance_lens1_dmd_laserdir + distance_lens1_pole1)
print("The distance between the dmd and the first pole is:", distance_lens1_dmd_ground)

pole_1_height = np.tan(alpha_1D) * distance_lens1_dmd_ground + delta
pole_2_height = np.tan(alpha_1D) * (distance_between_poles_ground + distance_lens1_dmd_ground) + delta


# Check for valid pole heights
if (pole_2_height < pole_1_height) :
    print("Pole 2 cannot be shorter than pole 1")

print("The height of the first pole is :",pole_1_height)
print("The height of the second pole is:", pole_2_height)
