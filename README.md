# pymetrics scoring calculator (average among all traits)
## About:
This program is basically a calculator. It took ~1 minute to write and does not produce results that expose information you would not be able to gather with a simple calculator. However, it can save you the time of summing 70+ values and division, and is very easy to setup and run.
<br>
<br>
My primary intention is the inspire others to interpret their results in a simialr way, to create basic code that myself and anyone can add to, and most importantly, to promote transparency in the interview process!

## Setup:
Download your Pymetrics data (JSON file): 
1) Log into Pymetrics website and naviagte to your Settings in upper righthand corner
3) Find "Your Account and Data" and click "Data Privacy Features"
4) In the "Download Your Data" section, click "Request Data"
5) Once it's ready ("Your file is ready for download"), click "Download Data"

Renaming file and creating path:
1) Rename your JSON file "data.json" (no quotes). Not that important: I think the default is your-name.json, in case you can't find the file or if that information is helpful in any way 😁
3) Download pymetrics.py from this repo and place 'pymetrics.py' and your JSON file in the same directory

Command Line:
1) Navigate to the directory your files are in in command line

Finally, run the command "python3 pymetrics.py" * <br>
\* Assuming you have python3 downloaded

## Interpreting Results:
"Average Score" indicates your **average percentile among all factors**
- Factors are "traits" measured from how you performed on games (e.g. "Attention Control", "Flexibility in Multitasking", "Learning from Mistakes Quickly")
- The percentile is **how you ranked among other people who took the assessment**. Since the data is from the pymetrics website, I believe your results are being compared against anyone who has taken the assessment. 
  -  For example, if your score is 70.34%, you ranked above 70.34% of other users

## More information about pymetrics:
- Companies will not necessarily (in fact, they most likely won't) use your average ranking based on every trait i.e. the result that is output by this program. They might prefer specific traits; it just depends how their recruiters/hiring managers decide to intepret scores.
- Recruiters/hiring managers may customize their pymetrics interpretation to classify job seekers into tiers of: **Recommended, Highly Recommended, or Not Recommended** for the position
- In regards to the previous bullet, Pymetrics models abide by the Uniform Guidelines on Employee Selection Procedures **"4/5ths rule of thumb"**
  - "...the pass rate, or impact ratio (IR), of the lowest-passing group over the pass rate of the highest-passing group, must always be greater than 0.8."
  - This would imply that 70%+ are "Highly Recommended" tier, 50-70% are "Recommended", and below 50% are "Not Recommended". It's important to note that pymetrics itself **uses their own models** to determine your percentile (which is probably not a mere average of all scores on all traits like this one), and that **hiring managers can create their own models for determining tiers**.
- Companies often use pyemtrics data of candidates to compare to their current employees scores, in order to determine if you're a good fit at their company

All quoted text is from this paper: https://www.ccs.neu.edu/home/amislove/publications/Pymetrics-FAccT.pdf. It includes interesting information about pymetrics algorithms and some (very limited) information about how pymetrics interprets your results and relays them to their comapany partners. 
<br>
<br>
Section of abstract that summarizes paper concisely: 
<br> 
"In this paper we outline a framework for algorithmic auditing by way of a case-study of pymetrics, a startup that uses machine learning to recommend job candidates to their clients. We discuss how pymetrics approaches the question of fairness given the constraints of ethical, regulatory, and client demands, and how pymetrics’ software implements adverse impact testing. We also present the results of an independent audit of pymetrics’ candidate screening tool."
