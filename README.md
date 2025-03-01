# 📌 Serverless To-Do List  

A simple **serverless To-Do List application** built with **HTML, CSS, JavaScript (Frontend)** and **AWS Lambda, API Gateway, DynamoDB (Backend)**. The frontend interacts with the backend using **API Gateway**.

---

## 🚀 Features  

✔️ Add tasks to a **DynamoDB** table  
✔️ Fetch and display tasks from the database  
✔️ **Serverless** architecture using AWS Lambda  
✔️ **API Gateway** integration for backend communication  
✔️ Hosted frontend (Optional: **AWS S3 & CloudFront**)  

---

## 🛠 Tech Stack  

- **Frontend**: HTML, CSS, JavaScript (Fetch API)  
- **Backend**: AWS Lambda (Python), API Gateway, DynamoDB  
- **Deployment**: AWS S3 (for frontend hosting), GitHub  

---

## 🏗 Step-by-Step Setup & Deployment  

### 1️⃣ Clone the Repository  

```bash
git clone https://github.com/Vinothraja2405/Serverless-ToDoList-using-Aws-Services
cd serverless-todo-list
2️⃣ Create a DynamoDB Table
Go to AWS Management Console → Search for DynamoDB.
Click "Create Table".
Enter Table Name: TodoTable.
Set Partition Key: taskId (String).
Choose On-Demand capacity mode.
Click Create Table.
3️⃣ Deploy the AWS Lambda Function
Go to AWS Console → Search for Lambda.
Click "Create Function" → Choose "Author from scratch".
Function Name: TodoFunction
Runtime: Select Python 3.x.
Permissions: Choose Create a new role with basic Lambda permissions.
Click "Create Function".
Upload lambda_function.py under the Code section.
Click Deploy.
4️⃣ Grant Lambda Access to DynamoDB
In AWS Console, go to IAM.
Click Roles → Find the role attached to your Lambda function.
Click Attach Policies.
Search for AmazonDynamoDBFullAccess and attach it.
Click Save Changes.
5️⃣ Create an API Gateway
Go to AWS Console → Search for API Gateway.
Click "Create API" → Select HTTP API.
Click "Add Integration" → Choose Lambda Function → Select TodoFunction.
Click Next, then Create API.
Click Routes → Create Route:
Method: POST
Path: /tasks
Integration Target: Select TodoFunction
Repeat Step 5 but create a GET route (/tasks) for fetching tasks.
Click Deploy API and copy the API URL.
6️⃣ Connect the Frontend to API
Open index.html in a text editor.

Find this line:

javascript
Copy
Edit
const apiUrl = "https://your-api-gateway-url.amazonaws.com/dev/tasks";
Replace "your-api-gateway-url" with your actual API Gateway URL.

Save the file.

7️⃣ Run Locally
To test the application locally:

Open the index.html file in a browser.

Mac/Linux:

bash
Copy
Edit
open index.html
Windows:

bash
Copy
Edit
start index.html
✅ Your app is working locally! 🎉

8️⃣ Deploy Frontend to S3 (Optional)
To host the frontend:

Go to AWS Console → Search for S3.

Click Create Bucket → Enter Bucket Name (e.g., todo-frontend).

Uncheck "Block all public access".

Upload index.html and styles.css.

Go to Permissions → Edit Bucket Policy:

json
Copy
Edit
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::todo-frontend/*"
    }
  ]
}
Enable Static Website Hosting under Properties.

Copy the S3 website URL and open it in a browser.

✅ Your To-Do List is now online! 🚀
