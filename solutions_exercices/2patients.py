# -*- coding: utf-8 -*-

"""
>>> Preprocess patient 1
"""

patient1 = 'GBM/TCGA-02-0037/'

# normalise stacks
patient1_t1 = zscore_normalize(patient1, 't1')
patient1_t1ce = zscore_normalize(patient1, 't1ce')
patient1_t2 = zscore_normalize(patient1, 't2')
patient1_flair = zscore_normalize(patient1, 'flair')

# Write normalised stacks
sitk.WriteImage(patient1_t1, 'patient1_t1_normalize.nii.gz')
sitk.WriteImage(patient1_t1ce, 'patient1_t1ce_normalize.nii.gz')
sitk.WriteImage(patient1_t2, 'patient1_t2_normalize.nii.gz')
sitk.WriteImage(patient1_flair, 'patient1_flair_normalize.nii.gz')

# Derive masks
patient1_masks = get_masks(patient1)

# Write masks
sitk.WriteImage(patient1_masks['label_full'], 'patient1_seg_label_full.nii.gz')
sitk.WriteImage(patient1_masks['label_nec'], 'patient1_seg_label_nec.nii.gz')
sitk.WriteImage(patient1_masks['label_core'], 'patient1_seg_label_core.nii.gz')
sitk.WriteImage(patient1_masks['label_et'], 'patient1_seg_label_et.nii.gz')

"""
>>> Preprocess patient 2
"""

patient2 = 'LGG/TCGA-CS-5396/'

# Normalise stacks
patient2_t1 = zscore_normalize(patient2, 't1')
patient2_t1ce = zscore_normalize(patient2, 't1ce')
patient2_t2 = zscore_normalize(patient2, 't2')
patient2_flair = zscore_normalize(patient2, 'flair')

# Write normalised stacks
sitk.WriteImage(patient2_t1, 'patient2_t1_normalize.nii.gz')
sitk.WriteImage(patient2_t1ce, 'patient2_t1ce_normalize.nii.gz')
sitk.WriteImage(patient2_t2, 'patient2_t2_normalize.nii.gz')
sitk.WriteImage(patient2_flair, 'patient2_flair_normalize.nii.gz')

# Derive masks
patient2_masks = get_masks(patient2)

# Write masks
sitk.WriteImage(patient2_masks['label_full'], 'patient2_seg_label_full.nii.gz')
sitk.WriteImage(patient2_masks['label_nec'], 'patient2_seg_label_nec.nii.gz')
sitk.WriteImage(patient2_masks['label_core'], 'patient2_seg_label_core.nii.gz')
sitk.WriteImage(patient2_masks['label_et'], 'patient2_seg_label_et.nii.gz')
