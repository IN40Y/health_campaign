# ETL process: Calculating campaign participation and health outcomes
def calculate_campaign_effectiveness(patients_df):
    # Group by health system and calculate metrics
    summary = patients_df.groupby('health_system_id').agg(
        total_patients=('patient_id', 'size'),
        total_participated=('campaign_participation', 'sum'),
        improved_outcomes=('health_outcome', lambda x: (x == 'Improved').sum())
    ).reset_index()

    # Calculate effectiveness rate
    summary['participation_rate'] = summary['total_participated'] / summary['total_patients'] * 100
    summary['improvement_rate'] = summary['improved_outcomes'] / summary['total_patients'] * 100

    return summary

# Load and transform data
patients_df = pd.read_csv('patients.csv')
summary_df = calculate_campaign_effectiveness(patients_df)

# Preview summary
print(summary_df.head())