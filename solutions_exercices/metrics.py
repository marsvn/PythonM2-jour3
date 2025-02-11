# -*- coding: utf-8 -*-

from sklearn.metrics import precision_score, recall_score

training_precision = precision_score(train_labels, training_predicted_classes)
training_recall = recall_score(train_labels, training_predicted_classes)

testing_precision = precision_score(validation_labels, testing_predicted_classes)
testing_recall = recall_score(validation_labels, testing_predicted_classes)

print('Training precision', training_balanced_accuracy, '; training recall', training_recall)
print('Validation precision', testing_precision, '; Validation recall', testing_recall)

