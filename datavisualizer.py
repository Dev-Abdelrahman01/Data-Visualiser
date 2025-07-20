#!/usr/bin/env python3
"""
DataVisualizer - Professional Data Visualization Tool
A beginner-friendly Python project demonstrating:
- Data handling with Pandas
- Data visualization with Matplotlib and Seaborn
- File I/O operations
- Professional chart creation
- Command-line interface design
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

# Set the style for better-looking plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def display_banner():
    """Display the application banner."""
    print("=" * 60)
    print("           DATAVISUALIZER")
    print("     Professional Data Visualization Tool")
    print("=" * 60)
    print()

def load_data(filename="sample_data.csv"):
    """Load data from a CSV file."""
    try:
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            return None
        
        data = pd.read_csv(filename)
        print(f"✓ Successfully loaded data from '{filename}'")
        print(f"  Dataset shape: {data.shape[0]} rows, {data.shape[1]} columns")
        print(f"  Columns: {', '.join(data.columns.tolist())}")
        return data
    
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def display_data_preview(data):
    """Display a preview of the loaded data."""
    print("\n" + "="*60)
    print("DATA PREVIEW")
    print("="*60)
    print("\nFirst 5 rows:")
    print(data.head())
    
    print("\nData types:")
    print(data.dtypes)
    
    print("\nBasic statistics:")
    print(data.describe())

def create_line_plot(data, save_path="plots"):
    """Create a line plot showing trends over time."""
    plt.figure(figsize=(12, 8))
    
    # Create subplots for multiple metrics
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Business Performance Trends', fontsize=16, fontweight='bold')
    
    # Sales trend
    axes[0, 0].plot(data['Month'], data['Sales'], marker='o', linewidth=2, markersize=6)
    axes[0, 0].set_title('Monthly Sales Trend', fontweight='bold')
    axes[0, 0].set_ylabel('Sales ($)')
    axes[0, 0].tick_params(axis='x', rotation=45)
    axes[0, 0].grid(True, alpha=0.3)
    
    # Profit trend
    axes[0, 1].plot(data['Month'], data['Profit'], marker='s', color='green', linewidth=2, markersize=6)
    axes[0, 1].set_title('Monthly Profit Trend', fontweight='bold')
    axes[0, 1].set_ylabel('Profit ($)')
    axes[0, 1].tick_params(axis='x', rotation=45)
    axes[0, 1].grid(True, alpha=0.3)
    
    # Customer growth
    axes[1, 0].plot(data['Month'], data['Customers'], marker='^', color='purple', linewidth=2, markersize=6)
    axes[1, 0].set_title('Customer Growth', fontweight='bold')
    axes[1, 0].set_ylabel('Number of Customers')
    axes[1, 0].tick_params(axis='x', rotation=45)
    axes[1, 0].grid(True, alpha=0.3)
    
    # Expenses trend
    axes[1, 1].plot(data['Month'], data['Expenses'], marker='d', color='red', linewidth=2, markersize=6)
    axes[1, 1].set_title('Monthly Expenses', fontweight='bold')
    axes[1, 1].set_ylabel('Expenses ($)')
    axes[1, 1].tick_params(axis='x', rotation=45)
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save the plot
    os.makedirs(save_path, exist_ok=True)
    filename = f"{save_path}/line_plot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✓ Line plot saved as: {filename}")
    
    plt.show()
    return filename

def create_bar_chart(data, save_path="plots"):
    """Create a bar chart comparing different metrics."""
    plt.figure(figsize=(14, 8))
    
    # Set up the data for grouped bar chart
    x = range(len(data['Month']))
    width = 0.25
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Create bars
    bars1 = ax.bar([i - width for i in x], data['Sales'], width, label='Sales', alpha=0.8)
    bars2 = ax.bar(x, data['Expenses'], width, label='Expenses', alpha=0.8)
    bars3 = ax.bar([i + width for i in x], data['Profit'], width, label='Profit', alpha=0.8)
    
    # Customize the chart
    ax.set_title('Monthly Financial Performance Comparison', fontsize=16, fontweight='bold')
    ax.set_xlabel('Month', fontweight='bold')
    ax.set_ylabel('Amount ($)', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(data['Month'], rotation=45)
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    def add_value_labels(bars):
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                   f'${height:,.0f}', ha='center', va='bottom', fontsize=8)
    
    add_value_labels(bars1)
    add_value_labels(bars2)
    add_value_labels(bars3)
    
    plt.tight_layout()
    
    # Save the plot
    os.makedirs(save_path, exist_ok=True)
    filename = f"{save_path}/bar_chart_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✓ Bar chart saved as: {filename}")
    
    plt.show()
    return filename

def create_scatter_plot(data, save_path="plots"):
    """Create a scatter plot to show relationships between variables."""
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle('Relationship Analysis', fontsize=16, fontweight='bold')
    
    # Sales vs Customers
    axes[0].scatter(data['Customers'], data['Sales'], alpha=0.7, s=100, c=data['Profit'], cmap='viridis')
    axes[0].set_xlabel('Number of Customers', fontweight='bold')
    axes[0].set_ylabel('Sales ($)', fontweight='bold')
    axes[0].set_title('Sales vs Customers\n(Color = Profit)', fontweight='bold')
    axes[0].grid(True, alpha=0.3)
    
    # Add trend line
    z = np.polyfit(data['Customers'], data['Sales'], 1)
    p = np.poly1d(z)
    axes[0].plot(data['Customers'], p(data['Customers']), "r--", alpha=0.8, linewidth=2)
    
    # Expenses vs Profit
    axes[1].scatter(data['Expenses'], data['Profit'], alpha=0.7, s=100, c=data['Sales'], cmap='plasma')
    axes[1].set_xlabel('Expenses ($)', fontweight='bold')
    axes[1].set_ylabel('Profit ($)', fontweight='bold')
    axes[1].set_title('Expenses vs Profit\n(Color = Sales)', fontweight='bold')
    axes[1].grid(True, alpha=0.3)
    
    # Add trend line
    z2 = np.polyfit(data['Expenses'], data['Profit'], 1)
    p2 = np.poly1d(z2)
    axes[1].plot(data['Expenses'], p2(data['Expenses']), "r--", alpha=0.8, linewidth=2)
    
    plt.tight_layout()
    
    # Save the plot
    os.makedirs(save_path, exist_ok=True)
    filename = f"{save_path}/scatter_plot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✓ Scatter plot saved as: {filename}")
    
    plt.show()
    return filename

def create_histogram(data, save_path="plots"):
    """Create histograms to show data distribution."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Data Distribution Analysis', fontsize=16, fontweight='bold')
    
    # Sales distribution
    axes[0, 0].hist(data['Sales'], bins=8, alpha=0.7, color='skyblue', edgecolor='black')
    axes[0, 0].set_title('Sales Distribution', fontweight='bold')
    axes[0, 0].set_xlabel('Sales ($)')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Profit distribution
    axes[0, 1].hist(data['Profit'], bins=8, alpha=0.7, color='lightgreen', edgecolor='black')
    axes[0, 1].set_title('Profit Distribution', fontweight='bold')
    axes[0, 1].set_xlabel('Profit ($)')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Expenses distribution
    axes[1, 0].hist(data['Expenses'], bins=8, alpha=0.7, color='lightcoral', edgecolor='black')
    axes[1, 0].set_title('Expenses Distribution', fontweight='bold')
    axes[1, 0].set_xlabel('Expenses ($)')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Customers distribution
    axes[1, 1].hist(data['Customers'], bins=8, alpha=0.7, color='plum', edgecolor='black')
    axes[1, 1].set_title('Customers Distribution', fontweight='bold')
    axes[1, 1].set_xlabel('Number of Customers')
    axes[1, 1].set_ylabel('Frequency')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save the plot
    os.makedirs(save_path, exist_ok=True)
    filename = f"{save_path}/histogram_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✓ Histogram saved as: {filename}")
    
    plt.show()
    return filename

def create_heatmap(data, save_path="plots"):
    """Create a correlation heatmap."""
    plt.figure(figsize=(10, 8))
    
    # Select only numeric columns for correlation
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    
    # Calculate correlation matrix
    correlation_matrix = numeric_data.corr()
    
    # Create heatmap
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
                square=True, fmt='.2f', cbar_kws={'shrink': 0.8})
    
    plt.title('Correlation Matrix Heatmap', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    
    # Save the plot
    os.makedirs(save_path, exist_ok=True)
    filename = f"{save_path}/heatmap_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✓ Heatmap saved as: {filename}")
    
    plt.show()
    return filename

def display_menu():
    """Display the visualization menu."""
    print("\n" + "="*60)
    print("VISUALIZATION OPTIONS")
    print("="*60)
    print("1. 📈 Line Plot - Show trends over time")
    print("2. 📊 Bar Chart - Compare different metrics")
    print("3. 🔍 Scatter Plot - Analyze relationships")
    print("4. 📋 Histogram - Show data distribution")
    print("5. 🌡️  Heatmap - Correlation analysis")
    print("6. 🎯 Generate All Plots")
    print("7. 📄 Show Data Preview")
    print("8. Exit")
    print()

def get_user_choice():
    """Get the user's menu choice."""
    while True:
        try:
            choice = int(input("Enter your choice (1-8): "))
            if 1 <= choice <= 8:
                return choice
            else:
                print("Please enter a number between 1 and 8.")
        except ValueError:
            print("Please enter a valid number.")

def generate_analysis_report(data, plot_files):
    """Generate a simple analysis report."""
    report = f"""
DATA ANALYSIS REPORT
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*60}

DATASET OVERVIEW:
- Total records: {len(data)}
- Time period: {data['Month'].iloc[0]} to {data['Month'].iloc[-1]}

KEY METRICS:
- Total Sales: ${data['Sales'].sum():,}
- Total Expenses: ${data['Expenses'].sum():,}
- Total Profit: ${data['Profit'].sum():,}
- Average Monthly Sales: ${data['Sales'].mean():,.0f}
- Average Monthly Profit: ${data['Profit'].mean():,.0f}
- Peak Sales Month: {data.loc[data['Sales'].idxmax(), 'Month']} (${data['Sales'].max():,})
- Peak Profit Month: {data.loc[data['Profit'].idxmax(), 'Month']} (${data['Profit'].max():,})

GROWTH ANALYSIS:
- Sales Growth: {((data['Sales'].iloc[-1] / data['Sales'].iloc[0]) - 1) * 100:.1f}%
- Customer Growth: {((data['Customers'].iloc[-1] / data['Customers'].iloc[0]) - 1) * 100:.1f}%
- Profit Margin (Average): {(data['Profit'].mean() / data['Sales'].mean()) * 100:.1f}%

GENERATED VISUALIZATIONS:
"""
    
    for i, plot_file in enumerate(plot_files, 1):
        report += f"{i}. {os.path.basename(plot_file)}\n"
    
    return report

def save_report(report, filename="analysis_report.txt"):
    """Save the analysis report to a file."""
    try:
        with open(filename, 'w') as file:
            file.write(report)
        print(f"✓ Analysis report saved as: {filename}")
        return True
    except Exception as e:
        print(f"Error saving report: {e}")
        return False

def main():
    """Main application entry point."""
    display_banner()
    
    # Load the data
    data = load_data()
    if data is None:
        print("Cannot proceed without data. Exiting...")
        return
    
    plot_files = []
    
    try:
        while True:
            display_menu()
            choice = get_user_choice()
            
            if choice == 8:
                print("\nThank you for using DataVisualizer!")
                print("Your visualizations have been saved in the 'plots' folder.")
                
                # Generate and save analysis report
                if plot_files:
                    report = generate_analysis_report(data, plot_files)
                    save_report(report)
                    print("Analysis report generated!")
                
                break
            
            elif choice == 7:
                display_data_preview(data)
                continue
            
            print(f"\n{'='*60}")
            print("GENERATING VISUALIZATION...")
            print(f"{'='*60}")
            
            if choice == 1:
                filename = create_line_plot(data)
                plot_files.append(filename)
            elif choice == 2:
                filename = create_bar_chart(data)
                plot_files.append(filename)
            elif choice == 3:
                # Import numpy for trend lines
                import numpy as np
                filename = create_scatter_plot(data)
                plot_files.append(filename)
            elif choice == 4:
                filename = create_histogram(data)
                plot_files.append(filename)
            elif choice == 5:
                filename = create_heatmap(data)
                plot_files.append(filename)
            elif choice == 6:
                print("Generating all visualizations...")
                import numpy as np
                plot_files.append(create_line_plot(data))
                plot_files.append(create_bar_chart(data))
                plot_files.append(create_scatter_plot(data))
                plot_files.append(create_histogram(data))
                plot_files.append(create_heatmap(data))
                print("✓ All visualizations generated!")
            
            input("\nPress Enter to continue...")
    
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please restart the program.")

if __name__ == "__main__":
    main()

