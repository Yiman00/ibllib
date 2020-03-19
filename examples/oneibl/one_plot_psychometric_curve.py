import matplotlib.pyplot as plt

from oneibl.one import ONE

from load_mouse_data import get_behavior  # TODO WRITE DEPENDENCY;
from behavior_plots import plot_psychometric # TODO THESE MODULES ARE NOT IN IBLLIB

one = ONE()

# Get session information (FYI, not used for plotting)
ses_ids = one.search(subjects='IBL_14', date_range='2018-11-27')
print(one.list(ses_ids[0]))

# Use function to get behavioral information
df = get_behavior('IBL_14', date_range='2018-11-27')

# -- Plot the psychometric curve
plt.figure()
plot_psychometric(df, ax=plt.axes(), color="orange")
