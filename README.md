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

## 🏗 Setup & Deployment  

### 1️⃣ Clone the Repository  

```bash
git clone https://github.com/Vinothraja2405/Serverless-ToDoList-using-Aws-Services
cd serverless-todo-list
2️⃣ Set Up the AWS Backend
✅ Create a DynamoDB Table
Go to AWS DynamoDB.
Create a table named TodoTable.
Set taskId as the Partition Key (String).
Enable On-Demand capacity mode.
✅ Deploy the AWS Lambda Function
Go to AWS Lambda → Create Function.
Choose "Author from scratch".
Select Runtime: Python 3.x.
Upload your lambda_function.py file.
Add DynamoDB Full Access permissions.
Deploy the function.
✅ Create an API Gateway
Go to AWS API Gateway → Create an HTTP API.
Add a POST route (/tasks) → Link to Lambda function.
Add a GET route (/tasks) → Link to Lambda function.
Enable CORS for frontend access.
Deploy and copy the API Endpoint URL.
3️⃣ Configure the Frontend
Open index.html.
Update the API URL:
javascript
Copy
Edit
const apiUrl = "https://your-api-gateway-url.amazonaws.com/dev/tasks";
Save the file.
4️⃣ Run Locally
Open index.html in a browser:

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
5️⃣ Deploy Frontend to S3 (Optional)
If you want to host the frontend:

Create an S3 bucket (Enable public access).
Upload index.html and styles.css.
Enable Static Website Hosting in S3 settings.
Copy the S3 URL and access your app! 🎉
