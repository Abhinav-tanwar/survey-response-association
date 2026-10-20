import pandas as pd,numpy as np
from scipy import stats
from pathlib import Path
root=Path(__file__).resolve().parents[1]
d=pd.read_csv(root/'data/survey.csv');t=d.pivot(index='Gender',columns='Lied',values='Count').loc[['Female','Male'],['Yes','No']].to_numpy()
a,b,c,e=t.ravel();assert int(t.sum())==27802
rr=(a/(a+b))/(c/(c+e));se=np.sqrt(1/a-1/(a+b)+1/c-1/(c+e));ci=np.exp(np.log(rr)+np.array([-1,1])*stats.norm.ppf(.975)*se)
r=stats.chi2_contingency(t,correction=False)
print('Total:',t.sum());print('Female affirmative proportion:',a/(a+b));print('Male affirmative proportion:',c/(c+e));print('Pearson chi-square:',r.statistic,'df:',r.dof,'p:',r.pvalue);print('Expected counts:',r.expected_freq);print('Relative risk Female/Male:',rr);print('95% log-Wald RR CI:',ci);assert (r.expected_freq>=5).all()
