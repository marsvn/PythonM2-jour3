# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 1, sharex=True, squeeze=True, figsize=(20, 10))

axes[0].plot(features_p1_t1_full, label='features from patient 1 for the full segmentation in T1 modality', color='red')
axes[0].plot(features_p2_t1_full, label='features from patient 2 for the full segmentation in T1 modality', color='green')
axes[0].set_yscale('symlog')
axes[0].set_ylabel('symlog')
axes[0].set_xlabel('feature id')
axes[0].set_xticklabels(features_columns, rotation='vertical')
axes[0].set_title("Features from Patient 1 for the full segmentation in T1 modality")

axes[1].plot(features_p1_t1_full - features_p2_t1_full)
axes[1].set_yscale('symlog')
axes[1].set_ylabel('symlog')
axes[1].set_xlabel('feature id')
axes[1].set_xticks(range(len(features_p1_t1_full)))
axes[1].set_xticklabels(features_columns, rotation=90)
axes[1].set_title("Difference")
plt.subplots_adjust(wspace=0, hspace=0)
plt.show();
