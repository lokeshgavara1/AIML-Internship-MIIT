import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Set random seed for reproducibility
np.random.seed(42)

# Create synthetic dataset
domains = ['Machine Learning', 'Web Development', 'Data Science', 'Cybersecurity', 
           'Mobile App Development', 'Cloud Computing', 'IoT']
n_students = 500

data = {
    'Student_ID': range(1, n_students + 1),
    'Domain': np.random.choice(domains, n_students, p=[0.25, 0.2, 0.2, 0.15, 0.1, 0.05, 0.05]),
    'Applications': np.random.randint(1, 5, n_students),
    'Participation_Hours': np.random.randint(10, 100, n_students),
    'Year': np.random.choice([2023, 2024, 2025], n_students, p=[0.3, 0.3, 0.4])
}

df = pd.DataFrame(data)

# Analysis 1: Most Popular Domains by Application Count
app_count = df.groupby('Domain')['Applications'].sum().sort_values(ascending=False)
print("Most Popular Domains by Applications:\n", app_count)

# Analysis 2: Participation Hours by Domain
part_hours = df.groupby('Domain')['Participation_Hours'].sum().sort_values(ascending=False)
print("\nTotal Participation Hours by Domain:\n", part_hours)

# Analysis 3: Emerging Domains (Growth in Applications 2023-2025)
yearly_apps = df.pivot_table(values='Applications', index='Domain', columns='Year', aggfunc='sum', fill_value=0)
yearly_apps['Growth_23_25'] = ((yearly_apps[2025] - yearly_apps[2023]) / yearly_apps[2023].replace(0, 1)) * 100
emerging_domains = yearly_apps['Growth_23_25'].sort_values(ascending=False)
print("\nEmerging Domains (Growth % from 2023 to 2025):\n", emerging_domains)

# Visualizations
plt.figure(figsize=(15, 10))

# Plot 1: Applications by Domain
plt.subplot(2, 2, 1)
sns.barplot(x=app_count.values, y=app_count.index, palette='viridis')
plt.title('Total Applications by Domain')
plt.xlabel('Applications')
plt.ylabel('Domain')

# Plot 2: Participation Hours by Domain
plt.subplot(2, 2, 2)
sns.barplot(x=part_hours.values, y=part_hours.index, palette='magma')
plt.title('Total Participation Hours by Domain')
plt.xlabel('Hours')
plt.ylabel('Domain')

# Plot 3: Emerging Domains
plt.subplot(2, 2, 3)
sns.barplot(x=emerging_domains.values, y=emerging_domains.index, palette='coolwarm')
plt.title('Domain Growth (2023 to 2025)')
plt.xlabel('Growth (%)')
plt.ylabel('Domain')

plt.tight_layout()
plt.savefig('engagement_plots.png')

# Dash Dashboard
app = Dash(__name__)

app.layout = html.Div([
    html.H1('Internship Domain Engagement Dashboard'),
    dcc.Dropdown(
        id='plot-type',
        options=[
            {'label': 'Applications by Domain', 'value': 'apps'},
            {'label': 'Participation Hours by Domain', 'value': 'hours'},
            {'label': 'Yearly Applications Trend', 'value': 'trend'}
        ],
        value='apps'
    ),
    dcc.Graph(id='engagement-graph')
])

@app.callback(
    Output('engagement-graph', 'figure'),
    Input('plot-type', 'value')
)
def update_graph(plot_type):
    if plot_type == 'apps':
        fig = px.bar(x=app_count.values, y=app_count.index, orientation='h',
                     labels={'x': 'Applications', 'y': 'Domain'}, title='Applications by Domain')
    elif plot_type == 'hours':
        fig = px.bar(x=part_hours.values, y=part_hours.index, orientation='h',
                     labels={'x': 'Hours', 'y': 'Domain'}, title='Participation Hours by Domain')
    else:
        fig = go.Figure()
        for domain in yearly_apps.index:
            fig.add_trace(go.Scatter(x=yearly_apps.columns[:-1], y=yearly_apps.loc[domain, [2023, 2024, 2025]],
                                     mode='lines+markers', name=domain))
        fig.update_layout(title='Yearly Applications Trend', xaxis_title='Year', yaxis_title='Applications')
    return fig

if __name__ == '__main__':
    app.run(debug=True, port=8050)
