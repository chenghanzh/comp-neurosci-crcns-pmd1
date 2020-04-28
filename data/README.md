# Data Description

In this data exploration, I am using pmd-1 dataset.

### How to retrieve data
The original data are organized nicely in ".mat" form. Thus, I use method "loadmat" from the package "scipy.io" to directly obtain the data in a JSON-like organization. Then, I reorganized the data in the following form. 

### Data Structure Organization
*read_data()* returns different values depends on whether the parameter indicates a raw data or processed data. 

#### Raw Data
For raw data, *read_data()* returns the following in order:
  * header
    * a description of the file, includes original file type, recorded platform and recorded time
  * version
    * data version name. Currently all 1.0
  * globals
    * Other metadata
  * M1_units
    * Processed M1 units data.
    * Type: list of dictionary of length #units. Each dictionary in the list refers to a electrode and items in the dictionary are as follows:
        * "id": a 1 x 2 array; [electrode_number, unit_ordinal]. Gives the electrode number that the unit was recorded from as well as whether the unit was the first (1), second (2), etc. unit recorded from that electrode
        * "waveform": a #units x #spikes array. Gives the waveform for each spike of that unit
        * "time of spike": a 1 x #spikes array. Gives the time of each spike
        * "mean inter-spike interval": mean inter-spike interval (ISI) for this unit
        * "offline_sorter_channel": in the offline sorting software, the channel of this unit
  * PMd_units
    * Processed PMd units data.
    * Type: list of dictionary of length #units. Each dictionary in the list refers to a electrode and items in the dictionary are as follows:
        * "id": a 1 x 2 array; [electrode_number, unit_ordinal]. Gives the electrode number that the unit was recorded from as well as whether the unit was the first (1), second (2), etc. unit recorded from that electrode
        * "waveform": a #units x #spikes array. Gives the waveform for each spike of that unit
        * "time of spike": a 1 x #spikes array. Gives the time of each spike
        * "mean inter-spike interval": mean inter-spike interval (ISI) for this unit
        * "offline_sorter_channel": in the offline sorting software, the channel of this unit
  * trials
    * Trial information contains metadata about each trial and M1 / PMd information related to that trial
    * Type: a list of dictionary of length #trials. Each dictionary in the list refers to a trial. Items in the dictionary are as follows:
        * "start time": trial start time in seconds
        * "end time": trial end time in seconds
        * "M1 waveform": items only for "MM_S1_raw.mat". M1 waveform information associated with this trial.
        * "M1 time of spike": items only for "MM_S1_raw.mat". M1 time information corresponds to M1 waveform of this trial.
        * "PMd waveform": PMd waveform information associated with this trial
        * "PMd time of spike": PMd time information corresponds to M1 waveform of this trial
        * "first target info", "second target info", "third target info", "fourth target info": a dictionary of experiment object information with the following items:
            * "appearance time": time of target appearance
            * "movement onset time": time of movement onset towards target
            * "peak velocity time": time of peak velocity towards target
            * "x location": target x location
            * "y location": target y location
        * "result": trial result
            * 82: Reward (successful trial)
            * 65: Abort (fails trial prior to the go cue, e.g., by leaving the center of work space during delay period)
            * 70: Fail (fails trial after the go cue, e.g., by not making it to the target in time)
            * 74: Incomplete (e.g., fails trial by not holding on target for enough time)
  * cont: a list of dictionary of length #time_bins that contains timing and kinematic information about each time stamp. Items in each dictionary:
    * "time": time stamps for each bin
    * "position": numpy array (1x2) containing the x and y positions of the arm for each time bin
    * "cont_vel": numpy array (1x2) containing the x and y velocities of the arm for each time bin
    * "cont_acc": numpy array (1x2) containing the x and y accelerations of the arm for each time bin. Calculated from the velocity rather than measured directly.
  
#### Processed Data
For processed data, *read_data()* returns the following in order:
* header
        * a description of the file, includes original file type, recorded platform and recorded time
* version
    * data version name. Currently all 1.0
  * globals
    * Other metadata
* reaches
    * A list of dictionary of length #reaches that contains information for each list. Items in the dictionary are as follows:
        * "trial number": trial number of this reach
        * "reach number": object number of this reach inside the trial
        * "start time": the time that the reach started in seconds
        * "appear time": the approximate time that the reach target (go cue) appeared
        * "end time": the time that the reach ended in seconds
        * "reach position start": a 1x2 array ([x position, y position]) denoting the starting position of the reach in cm.
        * "reach position end": a 1x2 array ([x position, y position]) denoting the ending position of the reach
        * "reach direction angle": the angle of the reach in radians, based upon the starting and ending positions
        * "reach length": the length of the reach in cm, based upon the starting and ending positions
        * "target on": a binary array (#time_bins x 1) which indicates approximately when the reach target (go cue) appeared (entry = 1 when go cue appeared, entry = 0 otherwise)
        * "kinematics": a list of dictionary of length #time_bins with the kinematic data for that reach. Items in the dictionary are as follows:
            * "position": a 1x2 array ([x position, y position]) indicates x, y position of reach, on-screen cursor, in cm
            * "velocity": a 1x2 array ([x velocity, y velocity]) indicates x, y velocity of reach, on-screen cursor, in cm/sec
            * "acceleration": a 1x2 array ([x acceleration, y acceleration]) indicates x, y acceleration of reach on-screen cursor, in cm/sec^2
            * "timestamp": time stamps for each measurement in seconds
        * "M1 neural data": an array (#neurons x #time_bins) which contains the spikes for each neuron in M1. Each entry in this array is an integer equal to the number of spikes that occurred for a given neuron in a given time bin
        * "PMd neural data": an array (#neurons x #time_bins) which contains the spikes for each neuron in PMd. Each entry in this array is an integer equal to the number of spikes that occurred for a given neuron in a given time bin
        * "time window": a binary array (#time_bins_trial x 1) which indicates which time bins, of all available during each trial, were used for the given reach. There can be up to four reaches per trial, and this array simply indicates the part of the trial that was used
        * "timestamps": an array (#time_bins x 1) with the timestamp of that bin in seconds
* trials
    * Trial information contains metadata about each trial and M1 / PMd information related to that trial
    * Type: a list of dictionary of length #trials. Each dictionary in the list refers to a trial. Items in the dictionary are as follows:
        * "start time": trial start time in seconds
        * "end time": trial end time in seconds
        * "first target info", "second target info", "third target info", "fourth target info": a dictionary of experiment object information with the following items:
            * "appearance time": time of target appearance
            * "movement onset time": time of movement onset towards target
            * "peak velocity time": time of peak velocity towards target
            * "x location": target x location
            * "y location": target y location
        * "result": trial result
            * 82: Reward (successful trial)
            * 65: Abort (fails trial prior to the go cue, e.g., by leaving the center of work space during delay period)
            * 70: Fail (fails trial after the go cue, e.g., by not making it to the target in time)
            * 74: Incomplete (e.g., fails trial by not holding on target for enough time)

### Data Processing Methods
* read_data: the function chooses to call *read_raw_data(file_name)* or *read_processed_data(file_name)* based on the parameter file_name.
* read_raw_data:
    * First use scipy.io to read all the .mat file
    * Read metadata: name, version, globals
    * Decides whether the file contains M1 data or not (only "MM_S1_raw.mat" contains M1 data)
    * Read and store M1 (if necessary) and PMd data
        * Read the whole M1 / PMd data
        * For each unit, read "id", "wf" (waveform), "ts" (time of spike), "misi" (mean inter-spike interval) and "offline_sorter_channel" information. If information is stored as a 1x1 array, unwrap it as a single number.
        * Organize all the information into a dictionary.
        * Append the dictionary into the list
    * Read and store trial information:
        * Read start time and end time by indexing
        * Find the corresponding M1 / PMd data that is between the start and end time of this trial
            * Based on observation, all trials goes one by one. Thus, I find the first electrophysiological data of the current trial by recording and looking after the index of the last electrophysiological data of the previous trial.
        * Get the subarray of M1 / PMd data of this trial
        * Read 4 object information by indexing and organize them into dictionary
        * Organize all the information relates to this trial to a dictionary 
        * Append the dictionary to trials list
    * Read and store kinetic information
        * Go through each time bin
        * Read timestamp, position, velocity, acceleration information related to each time bin
        * Store the information as a dictionary
        * Append to the kinetic information list
    * Return the data
        
 * read_processed_data:
    * First use scipy.io to read all the .mat file
    * Read metadata: name, version, globals
    * For all the reaches:
        * Find "trial_num" (trial number), "reach_num" (reach number), "reach_st" (start time), "cue_on" (appear time), "reach_end" (end time), "reach_pos_st" (reach position start), "reach_pos_end" (reach position end), "reach_dir" (reach direction angle), "reach_len" (reach length), "target_on" (target on), "neural_data_M1" (M1 neural data), "neural_data_PMd" (PMd neural data), "time_window": (time window), "timestamps" (timestamps) by indexing
        * For each time bin in "kinematics", read and organize "position" ([x position, y position]),  "velocity" ([x velocity, y velocity]),  "acceleration" ([x acceleration, y acceleration]), "timestamp" into a dictionary and append information for each time bin to a list.
        * Organize all the information and list of kinematics into a dictionary and append to a list of reaches
    * For trial information:
        * Read "block_info"
        * Read "start_time", "end_time", "result"
        * Read "appearance time", "movement onset time", "peak velocity time", "x location", "y location" for all 4 objects
        * Organize all the information into a dictionary and append to a trial list
    * Return the data