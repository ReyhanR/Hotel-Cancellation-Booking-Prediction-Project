## Purwadhika Final Project - Hotel Cancellation Booking Prediction

##### By : Reyhan Ryanafi

### Project Brief Description
---
Hotel industry is one industry that can utilize data and machine learning in helping management to increase revenue. 
one of them by using machine learning as a tool to take preventive action against the possibility of a consumer to cancel their bookings.

So in this project I was using booking data from a hotel in Portugal that is used to take insight and design a simple machine learning model.

* Dataset Source : Kaggle.com

* Dataset Info : [Source](https://www.sciencedirect.com/science/article/pii/S2352340918315191#bib1)

##### Project Objectives
- Create and choose one of several machine learning models, to predict hotel cancellation bookings.
- Create a web application using the flask, from a model that was created and selected previously.

#### The Dataset 
---
![dataset](https://github.com/ReyhanR/Final_Project_Purwadhika/blob/master/presentation_pic/dataset_pic.png)

#### Brief Model Selection

* Models Score 

Model Score (Train Set)                                                                                                 |Model Score (Test Set) 
:----------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:
|![model score](https://github.com/ReyhanR/Final_Project_Purwadhika/blob/master/presentation_pic/model_score_train.png)|![model score](https://github.com/ReyhanR/Final_Project_Purwadhika/blob/master/presentation_pic/model_score_test.png)|

* Models ROC Curve and AUC Score

![ROC Curve](https://github.com/ReyhanR/Final_Project_Purwadhika/blob/master/presentation_pic/Roc_curve.png)

* Models ROC Curve and AUC Score (Normal Data VS Oversampling)

![ROC Curve oversampling](https://github.com/ReyhanR/Final_Project_Purwadhika/blob/master/presentation_pic/Roc_curve_ovsam.png)

* Gradient Boosting Precision and Recall Score (Normal Data VS Oversampling)

Precision Score                                                                                                |Recall Score 
:----------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------:
|![model score](https://github.com/ReyhanR/Final_Project_Purwadhika/blob/master/presentation_pic/score_ovsam_precision.png)|![recall score](https://github.com/ReyhanR/Final_Project_Purwadhika/blob/master/presentation_pic/score_ovsam_recall.png)|

**The final choice of this classification model is that I chose the Gradient Boosting Classifier without oversampling the data as my model.**

### The Web Apps
---

#### Homepage
---
![homepage](https://github.com/ReyhanR/Final_Project_Purwadhika/blob/master/presentation_pic/Homepage.png)

#### Prediction
---
![data input](https://github.com/ReyhanR/Final_Project_Purwadhika/blob/master/presentation_pic/Input_data.png)

Feature  |Description |
:-------:|:----------:|
Country|Country of origin. Categories are represented in the ISO 3155–3:2013 format.
Deposit Type|Indication on if the customer made a deposit to guarantee the booking. This variable can assume three categories No-Deposit, Non-Refund and Refundable
Lead Time|Number of days that elapsed between the entering date of the booking into the PMS and the arrival date.
Total of Special Request|Number of special requests made by the customer (e.g. twin bed or high floor).
Average Daily Rate(ADR)|Calculated by dividing the sum of all lodging transactions by the total number of staying nights.
Market Segment|Market segment designation. In categories, the term “TA” means “Travel Agents” and “TO” means “Tour Operators”.
Arrival Date Day of Month|Day of the month of the arrival date.
Arrival Date Week Number|	Week number of the arrival date.
Stays In Week Nights|Number of week nights (Monday to Friday) the guest stayed or booked to stay at the hotel. Calculated by counting the number of week nights from the total number of nights.

#### Prediction Result
---

![Result](https://github.com/ReyhanR/Final_Project_Purwadhika/blob/master/presentation_pic/Result_pic.png)

#### Visualization Page
---

![visualization](https://github.com/ReyhanR/Final_Project_Purwadhika/blob/master/presentation_pic/visualization_page.png)
