import pandas

def savedf(p,a,out):
    data = {'Power': p,
            'Angle': a,
            'out': out}
    df = pandas.DataFrame(data,columns=['Power','Angle','out'])
    df.to_csv(r'data2.csv', index = False)
