# Review Branch  
Can be merged with branch "Assignment_3" after approval.  
  
# HARTFORD_ASSIGNMENT3_SUDSM_AWS  
Assignment 3 as part of Hartford AWS SageMaker Assignment  
  
## Goal:  
Create training model using sagemaker's own xgboost model.   
    
## Procedure:    
    
### Create the required code    
  - The code is built on top of Assignment 2's code which handles pre-processing of data  
  - Therefore, many files in this branch would be common to Assignment 2.  
      - The only file of interest for assignment 3 is "xgboost_inbuilt_Assignment3.ipynb" at:  
        - Notebooks/inbuilt-sagemaker-model/xgboost_inbuilt_updated.ipynb  
  
### Steps  
  
  - The inbuilt XGBoost model is used. Before training the model, the debug paths, experiments are setup.  
  - XGBoost model is trained using the below hyperparameters:  
    ![Kiku](Images/hyperparameter.png)  
  - The hyper-parameter runs are associated with the sagemaker experiments and "train:rmse","validation:rmse" are logged.  
  - Once the training is completed, the below charts are created from Sagemaker experiment:  
    - num_round vs train:rmse  
      ![Kiku](Images/num_rounds_vs_train_rmse.png)  
    - num_round vs validation:rmse  
      ![Kiku](Images/num_rounds_vs_validation_rmse.png)  
    - gamma vs train:rmse  
      ![Kiku](Images/gamma_vs_train_rmse.png)  
    - gamma vs validation:rmse  
      ![Kiku](Images/gamma_vs_validation_rmse.png)  
    - eta vs train:rmse  
      ![Kiku](Images/eta_vs_train_rmse.png)  
    - eta vs validation:rmse  
      ![Kiku](Images/eta_vs_validation_rmse.png)  
    - max_depth vs train:rmse  
      ![Kiku](Images/max_depth_vs_train_rmse.png)  
    - max_depth vs validation:rmse  
      ![Kiku](Images/max_depth_vs_validation_rmse.png)  
  - The best model is selected based on rmse score  
      ![Kiku](Images/bestmodel.png)  
  - For the selected best model, debugger is configured again   
    - with "loss_not_decreasing" and "overfit" debugger rules  
    - To collect SHAP and feature values for the best model  
      ![Kiku](Images/reconfigure_best_model_1.png)  
      ![Kiku](Images/reconfigure_best_model_2.png)  
  - The best model is visualized and below plots are made  
    - Metrics vs num_rounds/Iteration   
      ![Kiku](Images/Metrics_num_rounds.png)  
    - Feature-Importance (Weight and Cover) vs num_rounds/Iteration  
      ![Kiku](Images/Feature-Importance_num_rounds.png)  
    - Average-SHAP values vs num_rounds/Iteration  
      ![Kiku](Images/Average-SHAP__num_rounds.png)  
    - Global Explanations  
      ![Kiku](Images/Global_Explanations.png)  
    - Local Explanations  
      ![Kiku](Images/Local_explanations_1.png)  
      ![Kiku](Images/Local_explanations_2.png)  
    - Stacked Force Plot  
       ![Kiku](Images/stacked_force_plot_1.png)    
    - Outlier Plots  
      ![Kiku](Images/outlier1.png)  
      ![Kiku](Images/outlier2.png)  
      ![Kiku](Images/outlier3.png)  
      ![Kiku](Images/outlier4.png)  
      ![Kiku](Images/outlier5.png)  
      ![Kiku](Images/outlier6.png)  
  - The built model is deployed using sagemaker endpoint 
      ![Kiku](Images/endpoint.png)    
  
### Other information:  
  
- Sagemaker Experiment Screenshots  
  - ![Kiku](Images/sm_experiments_1.png)  
  - ![Kiku](Images/sm_experiments_2.png)  
  - ![Kiku](Images/sm_experiments_3.png)   
  
- Billing information (will be updated post 24hrs once)  
  - ![Kiku](Images/Bill1.png)  
  - ![Kiku](Images/Bill2.png)  
  - ![Kiku](Images/Bill3.png)  
   
