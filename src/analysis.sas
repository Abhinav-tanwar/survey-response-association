/* Survey Response Association */
%require_input(survey.csv);
data survey;
  length Gender $6 Lied $3;
  infile "&project_root./data/survey.csv" dsd dlm=',' firstobs=2 truncover;
  input Gender $ Lied $ Count;
  /* Explicit numeric ordering makes RR = Female risk / Male risk for Yes. */
  if Gender='Female' then sex_order=1; else sex_order=2;
  if Lied='Yes' then outcome_order=1; else outcome_order=2;
run;
proc format;
  value sexfmt 1='Female' 2='Male';
  value outfmt 1='Yes' 2='No';
run;
proc freq data=survey order=internal;
  weight Count;
  format sex_order sexfmt. outcome_order outfmt.;
  tables sex_order*outcome_order / nocol nopercent chisq expected relrisk;
  title 'Response association and relative risk: Female versus Male';
run;
