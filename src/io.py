# -*- coding: utf-8 -*-
# -*- mode: python -*-
"""Functions for file IO"""
from __future__ import print_function, division, absolute_import
import scipy.io as sio
import numpy as np


def read_data(file_name):
    if file_name=="MM_S1_raw.mat" or file_name=="MT_S1_raw.mat" or file_name=="MT_S2_raw.mat" or file_name=="MT_S3_raw.mat":
        return read_raw_data(file_name)
    if file_name=="MM_S1_processed.mat" or file_name=="MT_S1_processed.mat" or file_name=="MT_S2_processed.mat" or file_name=="MT_S3_processed.mat":
        return read_processed_data(file_name)
    return None


def read_raw_data(file_name):
    raw = sio.loadmat('./data/' + file_name)
    M1_used = False
    if file_name=="MM_S1_raw.mat":
        M1_used = True

    header = raw["__header__"]
    version = raw["__version__"]
    globals = raw["__globals__"]

    M1_units = []
    M1_units_num = 0
    if M1_used:
        M1_raw = raw["M1"][0][0]
        M1_units_raw = M1_raw[0][0]
        M1_sg_raw = M1_raw[1]
        M1_units_num = 67

        for unit in M1_units_raw:
            id = unit["id"][0]
            wf = unit["wf"]
            ts = unit["ts"][0]
            misi = unit["misi"][0][0]
            offline_sorter_channel = unit["offline_sorter_channel"][0][0]
            cur_unit = {"id": id,
                        "waveform": wf,
                        "time of spike": ts,
                        "mean inter-spike interval": misi,
                        "offline sorter channel": offline_sorter_channel}
            M1_units.append(cur_unit)

    PMd = raw["PMd"][0][0]
    PMd_units_raw = PMd[0][0]
    PMd_units = []
    PMd_units_num = len(PMd_units_raw)

    for unit in PMd_units_raw:
        id = unit["id"][0]
        wf = unit["wf"]
        ts = unit["ts"][0]
        misi = unit["misi"][0][0]
        offline_sorter_channel = unit["offline_sorter_channel"][0][0]
        cur_unit = {"id": id,
                    "waveform": wf,
                    "time of spike": ts,
                    "mean inter-spike interval": misi,
                    "offline sorter channel": offline_sorter_channel}
        PMd_units.append(cur_unit)
    # print(PMd_units[51]["time of spike"].shape)
    trial_raw = raw["trial_table"]

    trials = []

    if M1_used:
        M1_start_all = np.zeros(M1_units_num, dtype=int)
        PMd_start_all = np.zeros(PMd_units_num, dtype=int)

        for trial in trial_raw:
            start_time = trial[0]
            end_time = trial[21]
            M1_wf = []
            M1_ts = []

            for i in range(M1_units_num):
                M1_start_single = M1_start_all[i]
                while M1_units[i]["time of spike"][M1_start_single] < start_time:
                    M1_start_single = M1_start_single + 1
                M1_end_single = M1_start_single
                while M1_units[i]["time of spike"][M1_end_single] <= end_time:
                    M1_end_single = M1_end_single + 1
                M1_start_all[i] = M1_end_single
                M1_wf.append(M1_units[i]["waveform"][:, M1_start_single:M1_end_single])
                M1_ts.append(M1_units[i]["time of spike"][M1_start_single:M1_end_single])

            PMd_wf = []
            PMd_ts = []
            for i in range(PMd_units_num):
                PMd_start_single = PMd_start_all[i]
                # print(i)
                while PMd_start_single<PMd_units[i]["time of spike"].shape[0] and PMd_units[i]["time of spike"][PMd_start_single] < start_time:
                    PMd_start_single = PMd_start_single + 1
                PMd_end_single = PMd_start_single
                while PMd_end_single<PMd_units[i]["time of spike"].shape[0] and PMd_units[i]["time of spike"][PMd_end_single] <= end_time:
                    PMd_end_single = PMd_end_single + 1
                PMd_start_all[i] = PMd_end_single
                PMd_wf.append(PMd_units[i]["waveform"][:, PMd_start_single:PMd_end_single])
                PMd_ts.append(PMd_units[i]["time of spike"][PMd_start_single:PMd_end_single])

            first_target = {"appearance time": trial[1],
                            "movement onset time": trial[2],
                            "peak velocity time": trial[3],
                            "x location": trial[4],
                            "y location": trial[5]}

            second_target = {"appearance time": trial[6],
                             "movement onset time": trial[7],
                             "peak velocity time": trial[8],
                             "x location": trial[9],
                             "y location": trial[10]}

            third_target = {"appearance time": trial[11],
                            "movement onset time": trial[12],
                            "peak velocity time": trial[13],
                            "x location": trial[14],
                            "y location": trial[15]}

            fourth_target = {"appearance time": trial[16],
                             "movement onset time": trial[17],
                             "peak velocity time": trial[18],
                             "x location": trial[19],
                             "y location": trial[20]}

            result = trial[22]

            trial_info = {"start time": start_time,
                          "end_time": end_time,
                          "M1 waveform": M1_wf,
                          "M1 time of spike": M1_ts,
                          "PMd waveform": PMd_wf,
                          "PMd time of spike": PMd_ts,
                          "first target info": first_target,
                          "second target info": second_target,
                          "third target info": third_target,
                          "fourth target info": fourth_target,
                          "result": result
                          }
            trials.append(trial_info)
    else:
        PMd_start_all = np.zeros(PMd_units_num, dtype=int)

        for trial in trial_raw:
            start_time = trial[0]
            end_time = trial[21]

            PMd_wf = []
            PMd_ts = []
            for i in range(PMd_units_num):
                PMd_start_single = PMd_start_all[i]
                while PMd_start_single<PMd_units[i]["time of spike"].shape[0] and PMd_units[i]["time of spike"][PMd_start_single] < start_time:
                    PMd_start_single = PMd_start_single + 1
                PMd_end_single = PMd_start_single
                while PMd_end_single<PMd_units[i]["time of spike"].shape[0] and PMd_units[i]["time of spike"][PMd_end_single] <= end_time:
                    PMd_end_single = PMd_end_single + 1
                PMd_start_all[i] = PMd_end_single
                PMd_wf.append(PMd_units[i]["waveform"][:, PMd_start_single:PMd_end_single])
                PMd_ts.append(PMd_units[i]["time of spike"][PMd_start_single:PMd_end_single])

            first_target = {"appearance time": trial[1],
                            "movement onset time": trial[2],
                            "peak velocity time": trial[3],
                            "x location": trial[4],
                            "y location": trial[5]}

            second_target = {"appearance time": trial[6],
                             "movement onset time": trial[7],
                             "peak velocity time": trial[8],
                             "x location": trial[9],
                             "y location": trial[10]}

            third_target = {"appearance time": trial[11],
                            "movement onset time": trial[12],
                            "peak velocity time": trial[13],
                            "x location": trial[14],
                            "y location": trial[15]}

            fourth_target = {"appearance time": trial[16],
                             "movement onset time": trial[17],
                             "peak velocity time": trial[18],
                             "x location": trial[19],
                             "y location": trial[20]}

            result = trial[22]

            trial_info = {"start time": start_time,
                          "end time": end_time,
                          "PMd waveform": PMd_wf,
                          "PMd time of spike": PMd_ts,
                          "first target info": first_target,
                          "second target info": second_target,
                          "third target info": third_target,
                          "fourth target info": fourth_target,
                          "result": result
                          }
            trials.append(trial_info)

    cont_raw = raw["cont"][0][0]
    cont_t = cont_raw[0]
    cont_pos = cont_raw[2]
    cont_vel = cont_raw[3]
    cont_acc = cont_raw[4]
    time_bins = cont_t.shape[0]
    cont = []
    for i in range(time_bins):
        cont_info = {"time": cont_t[i],
                     "position": cont_pos[i],
                     "cont_vel": cont_vel[i],
                     "cont_acc": cont_acc[i]}
        cont.append(cont_info)

    return header, version, globals, M1_units, PMd_units, trials, cont

def read_processed_data(file_name):
    raw = sio.loadmat('./data/'+file_name)
    header = raw["__header__"]
    version = raw["__version__"]
    globals = raw["__globals__"]

    data_raw = raw["Data"][0][0]

    reaches = []
    for i in range(data_raw[0].shape[0]):
        trial_num = data_raw["trial_num"][i][0][0][0]
        reach_num = data_raw["reach_num"][i][0][0][0]
        reach_st = data_raw["reach_st"][i][0][0][0]
        cue_on = data_raw["cue_on"][i][0][0][0]
        reach_end = data_raw["reach_end"][i][0][0][0]
        reach_pos_st = data_raw["reach_pos_st"][i][0][0]
        reach_pos_end = data_raw["reach_pos_end"][i][0][0]
        reach_dir = data_raw["reach_dir"][i][0][0][0]
        reach_len = data_raw["reach_len"][i][0][0][0]
        target_on = data_raw["target_on"][i][0]
        kinematics_raw = data_raw["kinematics"][i][0]
        kinematics = []
        for time in kinematics_raw:
            kinematics_pos = [time[0], time[1]]
            kinematics_vel = [time[2], time[3]]
            kinematics_acc = [time[4], time[5]]
            kinematics_timestamp = time[6]
            kinematics_info = {"position": kinematics_pos,
                               "velocity": kinematics_vel,
                               "acceleration": kinematics_acc,
                               "timestamp": kinematics_timestamp}
            kinematics.append(kinematics_info)
        neural_data_M1 = data_raw["neural_data_M1"][i][0]
        neural_data_PMd = data_raw["neural_data_PMd"][i][0]
        time_window = data_raw["time_window"][i][0]
        timestamps = data_raw["timestamps"][i][0]

        reach = {"trial number": trial_num,
                 "reach number": reach_num,
                 "start time": reach_st,
                 "appear time": cue_on,
                 "end time": reach_end,
                 "reach position start": reach_pos_st,
                 "reach position end": reach_pos_end,
                 "reach direction angle": reach_dir,
                 "reach length": reach_len,
                 "target on": target_on,
                 "kinematics": kinematics,
                 "M1 neural data": neural_data_M1,
                 "PMd neural data": neural_data_PMd,
                 "time window": time_window,
                 "timestamps": timestamps
                 }
        reaches.append(reach)

    trials = []
    trial_raw = data_raw["block_info"]
    for trial in trial_raw:
        start_time = trial[0]
        end_time = trial[21]
        first_target = {"appearance time": trial[1],
                        "movement onset time": trial[2],
                        "peak velocity time": trial[3],
                        "x location": trial[4],
                        "y location": trial[5]}

        second_target = {"appearance time": trial[6],
                         "movement onset time": trial[7],
                         "peak velocity time": trial[8],
                         "x location": trial[9],
                         "y location": trial[10]}

        third_target = {"appearance time": trial[11],
                        "movement onset time": trial[12],
                        "peak velocity time": trial[13],
                        "x location": trial[14],
                        "y location": trial[15]}

        fourth_target = {"appearance time": trial[16],
                         "movement onset time": trial[17],
                         "peak velocity time": trial[18],
                         "x location": trial[19],
                         "y location": trial[20]}

        result = trial[22]

        trial_info = {"start time": start_time,
                      "end_time": end_time,
                      "first target info": first_target,
                      "second target info": second_target,
                      "third target info": third_target,
                      "fourth target info": fourth_target,
                      "result": result
                      }
        trials.append(trial_info)

    return header, version, globals, reaches, trials


# read_data("MM_S1_raw.mat")
# read_data("MM_S1_processed.mat")
# read_data("MT_S1_raw.mat")
# read_data("MT_S1_processed.mat")
# read_data("MT_S2_raw.mat")
# read_data("MT_S2_processed.mat")
# read_data("MT_S3_processed.mat")
# read_data("MT_S3_processed.mat")