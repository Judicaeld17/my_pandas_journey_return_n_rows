#TASK: Create a function which receives a pandas dataframe and nth row as parameters. Return all the rows until nth row from that dataframe.
def my_pandas_journey_return_n_rows(df,nth_row):
    return df.iloc[:nth_row,:]
