import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dataframe with your test results
data = {
    'Configuration': [
        'TCP Streaming (1KB)', 'TCP Stop-Wait (1KB)', 'TCP Stop-Wait (4KB)',
        'UDP Streaming (1KB)', 'UDP Stop-Wait (1KB)', 'UDP Streaming (4KB)', 'UDP Stop-Wait (4KB)'
    ],
    'Time_500MB': [0.51, 7.85, 2.00, 33.16, 42.34, 8.13, 11.21],
    'Time_1GB': [1.03, 15.72, 4.02, 66.69, 87.32, 16.36, 22.83]
}

df = pd.DataFrame(data)

# Function to plot bar charts
def plot_bar_chart(time_column, title, filename):
    plt.figure(figsize=(12, 6))
    plt.bar(df['Configuration'], df[time_column], color=['blue', 'red', 'green', 'purple', 'orange', 'cyan', 'magenta'])
    plt.title(title)
    plt.xlabel('Configuration')
    plt.ylabel('Time (seconds)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

# Generate and save the plots
plot_bar_chart('Time_500MB', 'Transmission Time Comparison (500 MB)', 'transmission_time_500MB.png')
plot_bar_chart('Time_1GB', 'Transmission Time Comparison (1 GB)', 'transmission_time_1GB.png')

import matplotlib.pyplot as plt
import numpy as np

# Data
configurations = [
    "TCP Streaming (1KB)", "TCP Stop-Wait (1KB)", "TCP Stop-Wait (4KB)",
    "UDP Streaming (1KB)", "UDP Stop-Wait (1KB)", "UDP Streaming (4KB)", "UDP Stop-Wait (4KB)"
]
time_500mb = [0.51, 7.85, 2.00, 33.16, 42.34, 8.13, 11.21]
time_1gb = [1.03, 15.72, 4.02, 66.69, 87.32, 16.36, 22.83]

x = np.arange(len(configurations))
width = 0.35  # Bar width

# Plot
fig, ax = plt.subplots(figsize=(12, 6))
bars1 = ax.bar(x - width/2, time_500mb, width, label='500MB', color='blue')
bars2 = ax.bar(x + width/2, time_1gb, width, label='1GB', color='red')

# Labels and formatting
ax.set_xlabel("Configuration")
ax.set_ylabel("Time (seconds)")
ax.set_title("500MB vs 1GB Transmission Time")
ax.set_xticks(x)
ax.set_xticklabels(configurations, rotation=45, ha="right")
ax.legend()

plt.tight_layout()
plt.savefig("500MB_vs_1GB.png")
plt.show()
