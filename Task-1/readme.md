📊 Internship Engagement Analysis (2023–2025)

    This project presents a data-driven dashboard and visual analysis of domain-wise engagement trends among students participating in internships from 2023 to 2025. The script uses a synthetic dataset to simulate real-world engagement metrics such as application counts, participation hours, and domain growth rates.


🚀 Features

📈 Bar plots for:
    Total applications per domain
    Total participation hours per domain
    Growth of domains from 2023 to 2025
    📊 Interactive Dash dashboard for real-time visualization
    📂 Generates a combined static plot image (engagement_plots.png)



🛠️ Technologies Use

    Python 3
    Pandas, NumPy
    Matplotlib, Seaborn for static plots
    Plotly, Dash for web dashboard


📂 File Structure

    .
    ├── task1_engagement_analysis.py   # Main analysis & dashboard script
    ├── engagement_plots.png           # Static visualizations output
    └── README.md                      # Project documentation


📊 Visual Output (Static):-

    After running the script, a PNG file engagement_plots.png will be generated with 3 plots:
    Applications by Domain
    Participation Hours by Domain
    Growth in Applications (2023 to 2025)



🌐 Web Dashboard:-

    The Dash dashboard supports:
    Dropdown for plot selection
    Interactive bar charts and trend lines
    Accessible at http://127.0.0.1:8050



▶️ How to Run:-

1. Install Required Libraries (if not already):
    pip install pandas numpy matplotlib seaborn plotly dash

2. Run the script:
    python task1_engagement_analysis.py


📌 Note:-

    The dataset is synthetically generated for demonstration purposes.
    FutureWarning from seaborn can be safely ignored or fixed by updating the barplot syntax.
