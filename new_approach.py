'''
Training with a different action space
Increased speed and granularity
Decreased turning angle

Changing training track and taking a overlapping approach between 
training to follow centerline and staying in between border
'''

import math 
def reward_function(params):
    '''
    Example of rewarding the agent to stay inside the two borders of the track
    '''
    
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    progress = params['progress']
    speed = params['speed']
    steering = abs(params['steering_angle'])
    
    # Give a very low reward by default
    reward = 1e-8
    MIN_SPEED = 1.25 
    
    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    #if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
    #   reward = reward + 1.0
    
    if speed >= MIN_SPEED:
        reward = reward + 1 # trying positive reinforcement
    
    if not all_wheels_on_track:
        reward *= 1e-8
        
    if progress == 100:
        reward =+ 100
       
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    
    ABS_STEERING_THRESHOLD = 10 # used to be 10
    
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 1e-8
   
    # Always return a float value
    return float(reward)
