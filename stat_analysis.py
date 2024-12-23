import json
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import scipy.stats as stats
from collections import Counter
from plotly.subplots import make_subplots

def analyze_feature_lengths(data):
    """
    Analyzes the distribution of feature lengths and counts.

    Args:
        data: A list of dictionaries, each representing a DNA sequence entry.

    Returns:
        None
    """

    # Extract feature lengths for a specific feature type (e.g., 'CDS')
    feature_lengths = []
    feature_types = []
    for entry in data:
        for feature in entry['features']:
            feature_types.append(feature['type'])
            if feature['type'] == 'CDS':
                feature_lengths.append(len(feature['sequence']))

    # Statistical analysis
    mean_length = np.mean(feature_lengths)
    median_length = np.median(feature_lengths)
    std_dev = np.std(feature_lengths)

    print(f"Mean CDS length: {mean_length:.2f} bp")
    print(f"Median CDS length: {median_length:.2f} bp")
    print(f"Standard deviation of CDS length: {std_dev:.2f} bp")

    # Shapiro-Wilk test for normality
    shapiro_test = stats.shapiro(feature_lengths)
    print(f"Shapiro-Wilk test p-value: {shapiro_test.pvalue:.4f}")

    # Count the number of features by type
    feature_counts = Counter(feature_types)

    # Create subplots for optimized rendering
    fig = make_subplots(
        rows=3, cols=2,
        subplot_titles=(
            "Histogram of CDS Lengths",
            "Feature Type Distribution",
            "Boxplot of CDS Lengths",
            "Violin Plot of CDS Lengths",
            "Heatmap of Feature Type Proportions",
            "Scatter Plot of Feature Lengths"
        )
    )

    # 1. Histogram
    fig_hist = px.histogram(
        x=feature_lengths,
        nbins=30,
        labels={'x': 'CDS Length (bp)', 'y': 'Count'},
        template='plotly'
    )
    for trace in fig_hist.data:
        fig.add_trace(trace, row=1, col=1)

    # 2. Bar Chart
    fig_bar = px.bar(
        x=list(feature_counts.keys()),
        y=list(feature_counts.values()),
        labels={'x': 'Feature Type', 'y': 'Count'},
        template='plotly'
    )
    for trace in fig_bar.data:
        fig.add_trace(trace, row=1, col=2)

    # 3. Boxplot
    fig.add_trace(
        go.Box(y=feature_lengths, boxmean='sd', marker_color='orange'),
        row=2, col=1
    )

    # 4. Violin Plot
    fig.add_trace(
        go.Violin(y=feature_lengths, box_visible=True, line_color='blue', meanline_visible=True),
        row=2, col=2
    )

    # 5. Heatmap
    feature_proportions = {key: value / sum(feature_counts.values()) for key, value in feature_counts.items()}
    fig.add_trace(
        go.Heatmap(
            z=[list(feature_proportions.values())],
            x=list(feature_proportions.keys()),
            y=['Proportion'],
            colorscale='Viridis',
            showscale=True
        ),
        row=3, col=1
    )

    # 6. Scatter Plot
    random_features = [len(feature['sequence']) for entry in data for feature in entry['features'] if 'sequence' in feature]
    fig_scatter = px.scatter(
        x=range(len(random_features)),
        y=random_features,
        labels={'x': 'Feature Index', 'y': 'Feature Length (bp)'},
        template='plotly'
    )
    for trace in fig_scatter.data:
        fig.add_trace(trace, row=3, col=2)

    # Update layout
    fig.update_layout(
        height=1200, width=1000,
        title="DNA Feature Length Analysis",
        showlegend=False
    )

    # Show the figure
    fig.show()

