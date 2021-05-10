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
  -------------------hyperparameter
  - The hyper-parameter runs are associated with the sagemaker experiments and "train:rmse","validation:rmse" are logged.
  -----------------image
  - Once the training is completed, the below charts are created from Sagemaker experiment:
    - num_round vs train:rmse
    - num_round vs validation:rmse
    - gamma vs train:rmse
    - gamma vs validation:rmse
    - eta vs train:rmse
    - eta vs validation:rmse
    - max_depth vs train:rmse
    - max_depth vs validation:rmse
  - The best model is selected based on rmse score
  ------------image
  - For the selected best model, debugger is configured again 
    - with "loss_not_decreasing" and "overfit" debugger rules
    - To collect SHAP and feature values for the best model
  - The best model is visualized and below plots are made
    - Metrics vs num_rounds/Iteration 
    - Feature-Importance (Weight and Cover) vs num_rounds/Iteration
    - Average-SHAP values vs num_rounds/Iteration
    - Global Explanations
    - Local Explanations
    - Stacked Force Plot
    - Outlier Plots
  - The built model is deployed using sagemaker endpoint


Other information:



### Set-up AWS for preprocessing  
  - Create a new S3 bucket and store the input data:  
       - Create a new S3 bucket named "1905-assignment2-sm". Enable versioning and add tags. Created in "us-east-1"  
       - Upload the raw housing dataset into this bucket. This file will be sent for train-test-split.  
          ![Kiku](Images/S3_Bucket_contents.png)  
       - Create a notebook instance in "us-east-1" in "ml.m4.xlarge" instance. Add an IAM role with access to Sagemaker and S3 while creating.  
         ![Kiku](Images/Notebook_instance.png)  
           
### Deploying the code in local machine  
We will first deploy the code from our local machine before running it on SageMaker Notebook instance. This is done as follows:  
  - The "xgboost_inbuilt_updated.ipynb" needs to be changed a little bit to deploy it in local machine.   
  - Make the following changes in "xgboost_inbuilt_updated.ipynb"  
    - Change "role = get_execution_role()" and mention the role name directly. For eg, "role = 'role_name_here'".  
  - Open the Ubuntu terminal in your local machine and follow the below steps to preprocess:  
    - Setup the Git environment by cloning into the branch.  
    - Open a python virtual environment  
    - Install necessary packages (sagemaker, pandas, s3fs, fsspec)  
    - Configure aws using your access key and access ID  
    - Run the "train_test_split.ipynb" notebook using "runipy". This will create the train and test datasets in the s3 bucket as shown.  
      ![Kiku](Images/Local_Split_Data.png)  
    - Run the "xgboost_inbuilt_updated.ipynb". This will create processing task, training job and batch transform job.  
      ![Kiku](Images/Local_Processing.png)  
      ![Kiku](Images/Local_Training.png)  
      ![Kiku](Images/Local_Batch_Transform.png)  
    - The preprocessed data will be placed in the S3 bucket as shown below.  
      ![Kiku](Images/Local_output.png)  
    - Finally, push these changes to the github repository.  
        
### Deploying in Sagemaker Notebook instance  
  - Start the Notebook Instance we had created and open JupyterLab  
  - Clone into the GitHub repositry's "main" branch  
  - Run the "train_test_split.ipynb" folowed by "xgboost_inbuilt_updated.ipynb". Similar to the local run, the relevant jobs will be created this time too.  
     ![Kiku](Images/Sagemaker_Processing.png)  
     ![Kiku](Images/Sagemaker_Training.png)  
     ![Kiku](Images/Sagemaker_Batchtransform.png)  
     All batch trasnform jobs (training, testing for local and sagemaker runs)  
     ![Kiku](Images/All_Batchtrasnforms.png)  
  -   The preprocessed data will be stored in S3 as shown during local deployment  
    
### Real time Transformation  
  - Previously, we performed batch transform wherein we gave a predefined set od datapoints as inputs.   
  - In real-time transform, we will invoke an endpoint and deploy our preprocessor in it.   
  - By doing this we will be able to input a set of data points and get the processed outputs in real time. The below snippets show the same.  
    ![Kiku](Images/Real_Time_Transform_1.png)  
    ![Kiku](Images/Real_Time_Transform_2.png)  
    ![Kiku](Images/Real_Time_Transform_3.png)  
        
### Output Files  
The preprocessed output files are kept in "Datasets" folder for reference.  
        
### Billing information (will be updated after 24 hours)  
  ![Kiku](Images/Billing_Dashboard.png)  
  ![Kiku](Images/Bill1.png)  
  ![Kiku](Images/Bill2.png)  
  ![Kiku](Images/Bill3.png)  
  ![Kiku](Images/FreeTier_Usage.png)  
