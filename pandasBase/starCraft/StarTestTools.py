def fillNAN(data_f):
    if data_f.isnull().values.any():
        data_f1 = data_f.fillna(0.)
    return data_f1


