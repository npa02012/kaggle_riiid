## Kaggle Riiid Competition

This is the repository I used to develop my code for the [Kaggle Riiid competition](https://www.kaggle.com/c/riiid-test-answer-prediction).  

Although I didn't do as well as I'd hope, I had several valuable takeaways:

* Configuration methods in [setup.sh](https://github.com/npa02012/kaggle_riiid/blob/main/setup.sh):
	* Installing a specific version of Python and building a venv + ipykernel with it.
	* Installing LightGBM.
* Python coding techniques:
	* Using the [datatable](https://datatable.readthedocs.io/en/latest/) package to quickly read a large CSV.
	* Using defaultdicts and 'nested' dictionaries.
	* Using [numba](https://numba.pydata.org/) to accelerate Python code execution.
	* SQLite with Python.
* Machine learning techniques:
	* Iteratively creating features (in a  for loop). Why this would be desirable in production situations.
	* [Continuation training](https://stackoverflow.com/questions/45654998/lightgbm-continue-training-a-model) of LightGBM models.
	* [Stacking](https://www.kaggle.com/c/riiid-test-answer-prediction/discussion/209577) of LightGBM models.
	* Interesting [neural net solutions](https://www.kaggle.com/c/riiid-test-answer-prediction/discussion/210113).
