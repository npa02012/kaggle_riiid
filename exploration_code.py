'''
asked_first50_ac_q_avg
    - Average for the question when it was asked within the first 50 interactions
    
Given a particular lecture, how likely was a student to answer a particular question correctly
    afterwards as compared to students who did not have the lecture?
    
Lectuers table has a part column (can do p1_lectuers_u_count)

Correct answer to the question
    Most guessed answer by a user when incorrect
'''

if False:
    import sklearn.metrics as metrics
    valid['pred'] = model.predict(valid[FEATURES])
    fpr, tpr, threshold = metrics.roc_curve(valid['answered_correctly'], valid['pred'])
    roc_auc = metrics.auc(fpr, tpr)
    print(roc_auc)

    train['pred'] = model.predict(train[FEATURES])
    fpr, tpr, threshold = metrics.roc_curve(train['answered_correctly'], train['pred'])
    roc_auc = metrics.auc(fpr, tpr)
    print(roc_auc)