if False:
    # Get features_dicts
    tmp = {'N_TRAIN_ROWS' : 1 * 1000000
            ,'n_skip_rows' : 0
          }
    train, valid, questions_df, features_dicts = read_and_preprocess(KAGGLE_RUN, tmp)
    
    # Get models
    tmp = {'model_names' : ['final_model_1', 'final_model_2', 'final_model_3', 'final_model_4', 'final_model_5']}
    TARGET, FEATURES, models = train_and_evaluate(train, valid, KAGGLE_RUN="test", final_params=tmp)
    
    # Test inference
    dont_include = [
        ['prior_question_had_explanation', 'elapsed_time_u_avg', 'community', 'n_tags']
        ,['prior_question_had_explanation', 'community', 'n_tags']
        ,['prior_question_had_explanation', 'n_tags']
        ,['community', 'n_tags']
        ,[]
    ]
        
    inference(TARGET, FEATURES, models, questions_df, features_dicts, dont_include)

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