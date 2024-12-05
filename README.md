# Turbine Power Prediction
A machine learning model with a data pipeline to capture, clean, extract, analyze, and store wind turbine data.
# Description
## Project Function
Currently companies are using formulas and linear analysis in attempts to model wind turbines, however have come up short due to the complexity of real world wind conditions. This project has attempted to take the data collected by the power curve working group, a member of the Consortium for the Advancement of Remote Sensing, and create a more realistic model of wind turbines.
## Power Curve Working Group Dataset
The dataset used for this analysis was the Power Curve Working Groups first dataset that comes from a moderately complex cold climate Swedish site surrounded by relatively low forestry. With values collected on approximately 10 minute intervals of mean wind speed and windvane at various heights as well as information on the turbine's density. The dataset contains over 10,000 examples spanning over a years worth of time and a total of 28 features.
## Pipeline Architecture
![image](https://github.com/user-attachments/assets/19b89159-f35e-443b-aa2a-35626c3b1e94)
I utilized a batch ingestion pipeline, collecting the raw data with python and stored it within a data lake with AWS S3. I then used 
### Tools
Which pipeline did you use? Which tools?
## Data Quality Assessment: 
Describe the quality status of the data set and the way you assessed it
## Data Transformation Models used: 
Briefly describe the transformations and models used and final results that you were able to achieve. If there are any special instructions needed to execute your code (e.g., signing up to a specific API to access the dataset that is needed) those need to be listed as well.
## Infographic: 
Final infographic describing the results of the engineering task accomplished. Examples can be provided if needed.
## Code: 
A link to GitHub Repository
## Thorough Investigation: 
This critically assesses the viability of your idea: Based on the results of this project (your pilot project, your prototype, etc), from a technical leadership point of view, what are your conclusions or recommendations for continuing this project in terms of scaling it up? How would you assess the innovativeness of your project? Any technical or platform concerns, difficulties, or limitations of the pipeline for the project? Based on your experience and results, what next step would you recommend to take this project to the next level/phase?
