import boto3
import os
import pandas as pd
import io
import lightgbm as lgb
import datatable as dt

class local_work():
    
    def __init__(self):
        self.s3_session = boto3.Session()
        self.s3_client = boto3.client('s3')
        self.s3_resource = boto3.resource('s3')
        self.bucket_name = 'npa02012-main'
        self.s3_bucket = self.s3_resource.Bucket(self.bucket_name)
        
    def download_riiid_files(self):
        # Download riiideducation package
        self.s3_client.download_file(self.bucket_name
                                    ,'kaggle_data/riiid-test-answer-prediction/riiideducation/__init__.py'
                                    ,'./input/riiideducation/__init__.py')
        tmp = 'competition.cpython-37m-x86_64-linux-gnu.so'
        self.s3_client.download_file(self.bucket_name
                                    ,'kaggle_data/riiid-test-answer-prediction/riiideducation/' + tmp
                                    ,'./input/riiideducation/' + tmp)
        
        if not os.path.isfile('./input/train.csv'):
            # Download train.csv
            self.s3_client.download_file(self.bucket_name
                                        ,'kaggle_data/riiid-test-answer-prediction/train.csv'
                                        ,'./input/train.csv')

        # Download example_sample_submission.csv and move to /kaggle/input
        save_to = '/home/ubuntu/kaggle_riiid/input/example_sample_submission.csv'
        self.s3_client.download_file(self.bucket_name
                                    ,'kaggle_data/riiid-test-answer-prediction/example_sample_submission.csv'
                                    ,save_to)
        move_to = '/kaggle/input/riiid-test-answer-prediction/example_sample_submission.csv'
        os.rename(save_to, move_to)

        # Download example_test.csv and move to /kaggle/input
        save_to = '/home/ubuntu/kaggle_riiid/input/example_test.csv'
        self.s3_client.download_file(self.bucket_name
                                    ,'kaggle_data/riiid-test-answer-prediction/example_test.csv'
                                    ,save_to)
        move_to = '/kaggle/input/riiid-test-answer-prediction/example_test.csv'
        os.rename(save_to, move_to)
        
    def get_train_data(self, data_types_dict, nrow=None):
        if nrow is None:
            return(dt.fread("./input/train.csv"
                            ,columns=set(data_types_dict.keys())).to_pandas())
        else:
            return(dt.fread("./input/train.csv"
                            ,columns=set(data_types_dict.keys())
                            ,max_nrows=nrow).to_pandas())

    def get_questions_data(self):
        key = 'kaggle_data/riiid-test-answer-prediction/questions.csv'
        obj = self.s3_client.get_object(Bucket=self.bucket_name, Key=key)
        df_questions = pd.read_csv(io.BytesIO(obj['Body'].read()))
        df_questions = df_questions[['question_id', 'part']]
        return(df_questions)
    
    def make_model(self, df_train, df_valid, target, features):
        params = {
            'objective': 'binary',
            'seed': 0,
            'metric': 'auc',
            'learning_rate': 0.05,
            'max_bin': 800,
            'num_leaves': 60
        }
        d_train = lgb.Dataset(df_train[features], label=df_train[target])
        d_valid = lgb.Dataset(df_valid[features], label=df_valid[target])

        model = lgb.train(
            params, 
            d_train, 
            num_boost_round=10000,
            valid_sets=[d_train, d_valid], 
            early_stopping_rounds=50,
            verbose_eval=50
        )
        return(model)
    
    
    
    
    
    
    
    
    
    
    
    
    
        
