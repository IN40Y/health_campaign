# Health Campaign
This project simulates an ETL pipeline and dashboard for healthcare data, modeled after a real Health Information Exchange (HIE) system I developed. Due to confidentiality, I generated random datasets to showcase skills in data integration, campaign effectiveness analysis, and visualization using Airflow and Plotly in a simplified context.
This repository contains randomly generated datasets used to simulate a real-world project that I developed in the healthcare domain. The original project was part of a larger Health Information Exchange (HIE) system that I built to integrate data from various healthcare organizations. However, due to legal and confidentiality obligations, I am unable to share the actual datasets or code used in that project. This dataset and code aim to demonstrate my approach, skills, and thought process in a simplified, public-friendly version of the original work.

# Project Context:
The real project involved designing and implementing an Airflow-based ETL pipeline that integrated healthcare data from numerous health systems, including Electronic Health Records (EHRs) and Laboratory Information Management Systems (LIMS). My responsibilities included ensuring smooth data flow, developing dashboards to track health campaign effectiveness, and managing various data transformation tasks to standardize information for state-level health system analysis.

# Dataset Description:
1. Health Systems Dataset (health_systems.csv)
  Simulates 10 state-level health systems with fields for:
    - system_id: Unique identifier for each health system.
    - state: The state where the health system operates.
    - region: Geographic region categorization.
    - total_patients: Simulated count of total patients per health system.

2. Patients Dataset (patients.csv)
  Contains data for 1000 patients randomly assigned to the health systems with fields for:
    - patient_id: Unique patient identifier.
    - age: Age of the patient.
    - gender: Gender of the patient.
    - health_system_id: The health system where the patient is registered.
    - campaign_participation: Binary flag (0 or 1) indicating whether the patient participated in a health campaign.
    - health_outcome: Simulated outcome of the patient's health status after campaign participation (Improved, Unchanged, Worsened).

# Purpose of the Dataset:
Key metrics generated include:
- **Campaign Participation Rate**: Percentage of patients who participated in health campaigns.
- **Health Outcome Improvement Rate**: Percentage of patients who showed improved health outcomes after participating in campaigns.
 
# Scope and Limitations:
This dataset is intentionally simplified and represents a small subset of the functionality implemented in the actual project. The real-world project included:

Data integration across multiple health organizations and systems.
Complex data transformations from various formats into standard FHIR (Fast Healthcare Interoperability Resources) formats.
Advanced security mechanisms like role-based access control.
A broader range of metrics, including demographic analysis and longitudinal health outcomes over time.

# What to Expect:
In the code, you will find:

An ETL pipeline simulating the extraction, transformation, and loading of healthcare data.
Interactive Dashboards built with Plotly to visualize health campaign participation and improvement rates by health system.
