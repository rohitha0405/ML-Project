from scipy.stats import chi2_contingency
class TestChiSquare:
    def findTestResult(self,df):
        dfd = df
        X = df.iloc[:, 1:3].values.astype(int)
        y = df.iloc[:, 4:6].values.astype(int)
        df = [[X], [y]]
        table = [X,y]
        #print(table)
        stat, p, dof, expected = chi2_contingency(table)

        # interpret p-value
        alpha = 0.05
        print("p value is " + str(p))
        if p <= alpha:
            print('Dependent (reject H0)')
        else:
            print('Independent (H0 holds true)')

        pass

        # import scipy.stats as stats
        # x = dfd[:, :0].values.astype(int)
        # y = dfd[:, :1].values.astype(int)
        # table = [x, y]
        # oddsratio, pvalue = stats.fisher_exact()
        # print("OddsR: ", oddsratio, "p-Value:", pvalue)
        # import pandas as pd
        # dfd = pd.DataFrame([list(range(5))], columns=["a{}".format(i) for i in range(5)])
        # print(dfd.iloc[0])
        # print(type(dfd))
        # sr = pd.Series(dfd)
        # print(dfd.pow(sr, axis=1))

        return str(p)