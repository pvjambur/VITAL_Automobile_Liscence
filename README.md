# VITAL_Automobile_Liscence

# Script-Sages

## Project Name: VITAL

### Vehicle Identification and Tracking Automobile License

# **Introduction to the VITAL**

 VITAL leverages advanced surveillance technology to accurately match car descriptions with license plate information, ensuring efficient and precise identification of suspect vehicles. This system integrates cutting-edge recognition algorithms to provide real-time tracking and analysis, enhancing security and enforcement operations. With VITAL, monitoring and pinpointing targeted vehicles has never been more reliable or effective.


![Notebook1-1.png](https://github.com/Asikpalysik/Automatic-License-Plate-Detection/blob/main/Presentation/Notebook1.png?raw=true)

**VITAL** identifies multiple features of the test case automobile, taking 3 major inputs:

1. The description of the car: **Colour & Type**

![colour_car](https://lh3.googleusercontent.com/proxy/UOpW12R9kZWRJegloBIb213BbL4FwGUA7gOG8CJ7oR2Su2rTpLXnoQYVEVrxW2e6lg8f6Z1nybDZIRv4XDg)

2. The automobile's licence plate: **Irrespective of country, font or design of number plate**

3. The video footage source file: **Either a Dashcam or CCTV footage**

# **What's the ouput:** User's perspective*

![rrrr](https://mobisoftinfotech.com/resources/wp-content/uploads/2022/02/og-Number-Plate-Detection.png)

1. Screenshot of the identified vehicle: **Time stamp included**

2. Duration of vehicle captures: **How long the vehicle was captured through the camera**


## Brief about the steps

In the above code, we individually take each file and parse into xml.etree and find the object -> bndbox. Then we extract xmin,xmax,ymin,ymax and saved those values in the dictionary. After we convert it into a pandas data frame and save that into CSV file and save it in project folder as shown below.

# VITAL: Vehicle Identification and Tracking Automated Locator

## Importance of VITAL

| Step | Description                                                                 |
|------|-----------------------------------------------------------------------------|
| 1    | **Enhanced Security:** VITAL improves public safety by swiftly identifying and tracking suspect vehicles, reducing the response time of law enforcement. |
| 2    | **Accurate Identification:** By combining car descriptions with license plate recognition, VITAL increases the accuracy of vehicle identification, minimizing errors and false positives. |
| 3    | **Real-Time Monitoring:** The system provides real-time data and alerts, allowing for immediate action and continuous surveillance. |
| 4    | **Data Integration:** VITAL integrates seamlessly with existing surveillance infrastructure, making it a cost-effective solution for enhancing security operations. |

![mointor](https://i.ytimg.com/vi/T4j7Ytb57Q0/maxresdefault.jpg)

## Future Scope of VITAL

| Area              | Description                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------------|
| **Technology Advancements** | Future developments in AI and machine learning will further enhance VITAL’s accuracy and speed, making it even more efficient. |
| **Scalability**             | VITAL can be scaled to cover larger areas and more vehicles, supporting expansive urban and rural security needs.             |
| **Integration with IoT**    | Integrating VITAL with IoT devices will enable more comprehensive monitoring and data collection from various sources.        |
| **Predictive Analysis**     | Advanced analytics can be incorporated to predict and prevent potential security threats based on historical data.            |

## Uses of VITAL

| Application Area          | Description                                                                                   |
|---------------------------|-----------------------------------------------------------------------------------------------|
| **Law Enforcement**       | Assists in quickly identifying and tracking vehicles involved in criminal activities.         |
| **Traffic Management**    | Helps in monitoring and managing traffic flow by identifying vehicles violating traffic rules. |
| **Public Safety**         | Enhances the safety of public spaces by identifying and tracking suspicious vehicles.          |
| **Event Security**        | Monitors and ensures the safety of large public events by tracking vehicles in real time.      |
| **Border Control**        | Assists in identifying and tracking vehicles crossing borders, enhancing national security.    |

VITAL stands as a robust and reliable solution, vital for modern surveillance and security operations. It not only addresses current security challenges but also paves the way for future innovations and broader applications.

# Model wise evaluation and procedure

## 1. *License Plate Recognition*

### Testing: Car with plate
![image](https://github.com/pvjambur/VITAL_Automobile_Liscence/assets/145439975/7e4d451e-41c9-4103-b76a-f67462578147)

### Results: Highlights the plate
![image](https://github.com/pvjambur/VITAL_Automobile_Liscence/assets/145439975/a47919e3-ada2-4cd2-be70-3f7d900b925e)


### **INCEPTION-RESNET-V2 TRAINING AND SAVE**

#### *Training and Saving an Inception-ResNet-v2 Model*

1. **Data Collection and Preprocessing:**
   - Collect a large and diverse dataset.
   - Normalize and augment the data.
   - Split the data into training, validation, and test sets.

2. **Model Initialization:**
   - Initialize the Inception-ResNet-v2 architecture.
   - Optionally use pre-trained weights to leverage transfer learning.

3. **Training:**
   - Train the model using a powerful GPU.
   - Employ techniques like learning rate scheduling, data augmentation, and batch normalization.
   - Continuously monitor the model's performance using validation data.
   - Fine-tune hyperparameters to achieve the best results.

4. **Evaluation:**
   - Assess the model's performance on the test set to ensure it meets the desired metrics.

5. **Saving the Model:**
   - Save the trained model in a suitable format (e.g., TensorFlow SavedModel or HDF5).

6. **Deployment:**
   - Load the saved model for inference in various applications to ensure efficient and accurate predictions.

## OPTICAL CHARACTER RECOGNITION - OCR

### TESSERACT OCR

![CRConvNet-the-Character-Recognition-Convolutional-Neural-Network-architecture](https://github.com/pvjambur/VITAL_Automobile_Liscence/assets/145439975/3c3ec8c5-4c09-498b-9c5b-599485ab22dd)


Optical character recognition (OCR) software that is used to extract text from the image. Tesseract OCR have a python API and it is open source. Firstly, we will do installation of it. It pretty simple and depend on you OS. You can find manual and files to download for installation here.

### OCR Input: Bounded box around plate

![image](https://github.com/pvjambur/VITAL_Automobile_Liscence/assets/145439975/24d96005-6b5b-462a-b6b6-315528d7c1fe)

#### Proccessing through OCR based formating

![Car-Number-Plate-Detection-Using-MATLAB-and-Image-Processing](https://github.com/pvjambur/VITAL_Automobile_Liscence/assets/145439975/056ed0ec-60f0-4602-b266-2867a96c4750)

### OCR Output: Return text recogninzed

![image](https://github.com/pvjambur/VITAL_Automobile_Liscence/assets/145439975/9f4f31cc-1de0-4748-9c68-dbfcc58c6625)

### Python based code: 

```
text = pt.image_to_string(roi)
print(text)
```
### Ouput:

```
WOR SIBK
```
As we can see, the model is'nt very accurate, however its depency on various parameters whould be the most proabable cause of its low effeciency.

# Final Output as a prompt

## When the user provides the ideo file to us, we give them annotated video with the timesstamps as well

### Original video



https://github.com/pvjambur/VITAL_Automobile_Liscence/assets/145439975/cf3a6e09-4a52-47ab-af2f-f0140262a0fa


### Annotated video: Final Ouput





https://github.com/pvjambur/VITAL_Automobile_Liscence/assets/145439975/551a5380-84cd-49aa-8a87-c5007483cc21

