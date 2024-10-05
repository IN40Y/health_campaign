import plotly.express as px

# Plot campaign participation rate
fig = px.bar(summary_df, x='health_system_id', y='participation_rate', title='Campaign Participation Rate by Health System')
fig.show()

# Plot health improvement rate
fig2 = px.bar(summary_df, x='health_system_id', y='improvement_rate', title='Health Outcome Improvement Rate by Health System')
fig2.show()