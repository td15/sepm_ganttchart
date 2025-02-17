import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# Create a DataFrame to hold tasks and their start and end dates
data = {
    'Task': [
        'Future Planning', 'Documentation', 'Feedback Collection', 
        'Initial Launch', 'App Deployment', 'Server Setup', 
        'Performance Testing', 'Usability Testing', 'Functional Testing', 
        'Search Engine Integration', 'Backend Development', 
        'Frontend Development', 'Database Design', 
        'UI/UX Design', 'Requirement Gathering', 
        'Team Formation & Scope Definition'
    ],
    'Start': [
        '2023-02-18', '2023-02-20', '2023-02-22', 
        '2023-03-01', '2023-03-10', '2023-03-12', 
        '2023-03-15', '2023-03-18', '2023-03-20', 
        '2023-03-25', '2023-03-22', '2023-04-01', 
        '2023-04-05', '2023-04-10', '2023-04-15', 
        '2023-04-20'
    ],
    'End': [
        '2023-02-24', '2023-02-28', '2023-03-09', 
        '2023-03-16', '2023-03-21', '2023-03-18', 
        '2023-03-23', '2023-03-24', '2023-03-30 ', 
        '2023-03-30', '2023-04-02', '2023-04-05', 
        '2023-04-09', '2023-04-14', '2023-04-18', 
        '2023-04-22'
    ]
}

df = pd.DataFrame(data)
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])

# Generate the Gantt chart
fig, ax = plt.subplots(figsize=(10, 6))

for i in range(len(df)):
    ax.barh(df['Task'][i], df['End'][i] - df['Start'][i], left=df['Start'][i], color='skyblue')

# Formatting the date axis
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

plt.title("Gantt Chart - Task Timeline")
plt.xlabel("Timeline")
plt.ylabel("Tasks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='x')

plt.show()
