# -*- coding:utf-8 -*-
# @Author: Niccolò Bonacchi
# @Date: Tuesday, February 12th 2019, 11:49:54 am
# @Last Modified by: Niccolò Bonacchi
# @Last Modified time: 12-02-2019 11:49:57.5757
from alf.extractors.training_trials import *


def extract_all(session_path, save=False, data=False):
    if not data:
        data = raw.load_data(session_path)
    feedbackType = get_feedbackType(session_path, save=save, data=data)
    contrastLeft, contrastRight = get_contrastLR(
        session_path, save=save, data=data)
    probabilityLeft, _ = get_probaLR(session_path, save=save, data=data)
    choice = get_choice(session_path, save=save, data=data)
    rewardVolume = get_rewardVolume(session_path, save=save, data=data)
    feedback_times = get_feedback_times(session_path, save=save, data=data)
    stimOn_times = get_stimOn_times(session_path, save=save, data=data)
    intervals = get_intervals(session_path, save=save, data=data)
    response_times = get_response_times(session_path, save=save, data=data)
    iti_dur = get_iti_duration(session_path, save=save, data=data)
    go_cue_trig_times = get_goCueTrigger_times(session_path, save=save, data=data)
    go_cue_times = get_goCueOnset_times(session_path, save=save, data=data)
    # Missing datasettypes
    # _ibl_trials.goCue_times
    # _ibl_trials.deadTime
    out = {'feedbackType': feedbackType,
           'contrastLeft': contrastLeft,
           'contrastRight': contrastRight,
           'probabilityLeft': probabilityLeft,
           'session_path': session_path,
           'choice': choice,
           'rewardVolume': rewardVolume,
           'feedback_times': feedback_times,
           'stimOn_times': stimOn_times,
           'intervals': intervals,
           'response_times': response_times,
           'iti_dur': iti_dur,
           'goCue_times': go_cue_times,
           'goCueTrigger_times': go_cue_trig_times}
    return out


if __name__ == "__main__":
    sess = '/home/nico/Projects/IBL/IBL-github/iblrig/scratch/test_iblrig_data/Subjects/ZM_1085/2019-02-12/002'  # noqa
    alf_data = extract_all(sess)
    print('.')
