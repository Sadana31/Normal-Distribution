import random
import plotly.express as px
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go 
import csv 

score = []

with open('data.csv', newline='') as f:
    df = csv.DictReader(f)

    for row in df:
        score.append(float(row["math score"]))
        
    
# calculating mean, median, mode and std
mean = sum(score)/len(score)
median = statistics.median(score)
mode = statistics.mode(score)
std = statistics.stdev(score)

# finding 1, 2 and 3 standard deviation start and end values
first_std_start,first_std_end = mean - std, mean + std

second_std_start,second_std_end = mean - (std*2), mean + (std*2)

third_std_start,third_std_end = mean - (std*3) , mean + (std*3)

# calculating the % of data in 1,2,3 std deviation
# find out result
data_within_one_std = [result for result in score
if result > first_std_start and result < first_std_end]

data_within_two_std = [result for result in score 
if result > second_std_start and result < second_std_end]

data_within_three_std = [result for result in score 
if result > third_std_start and result < third_std_end]


# graph
fig = ff.create_distplot([score],["result"],show_rug=False)
fig.update_layout(title_text="Graph of the student's performance in Math")
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="Mean of the data"))
fig.add_trace(
    go.Scatter(x=[first_std_start,first_std_start],
    y=[0,0.17],mode="lines",name="1st Standard Deviation start")
)
fig.add_trace(
    go.Scatter(x=[first_std_end,first_std_end],
    y=[0,0.17],mode="lines",name="1st Standard Deviation end")
)

fig.add_trace(
    go.Scatter(x=[second_std_start,second_std_start],
    y=[0,0.17],mode="lines",name="2nd Standard Deviation start")
)
fig.add_trace(
    go.Scatter(x=[second_std_end,second_std_end],
    y=[0,0.17],mode="lines",name="2nd Standard Deviation end")
)
fig.add_trace(
    go.Scatter(x=[third_std_start,third_std_start],
    y=[0,0.17],mode="lines",name="3rd Standard Deviation start")
)
fig.show()

print("Mean of the student's math score is: ", format(mean))
print("Median of the student's math score is: ", format(median))
print("Mode of the student's math score is: ", format(mode))
print("")
print("Standard Deviation of the student's math score is: ", format(std))

print(format(len(data_within_one_std)*100.0/len(score)),
"% of data lies within first standard deviation: ")

print("")

print(format(len(data_within_two_std)*100.0/len(score)), 
"% of data lies within two standard deviation: ")

print("")

print(format(len(data_within_three_std)*100.0/len(score)),
"% of data lies within third standard deviation: ")

print("")





