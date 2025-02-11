# -*- coding: utf-8 -*-

#read data one subject
src = './data/preprocessed/'
count = 0  # choose a number between 0 and 20
t1 = create_data_one_subject(src, count, image_type='t1')
t1ce = create_data_one_subject(src, count, image_type='t1ce')
t2 = create_data_one_subject(src, count, image_type='t2')
flair = create_data_one_subject(src, count, image_type='flair')
seg = create_data_one_subject(src, count, image_type='seg') # return a dict with {label_full, label_nec, label_core, label_et}