Serverless To-Do List

A simple serverless to-do list application built with HTML, CSS, JavaScript (Frontend) and AWS Lambda, API Gateway, and DynamoDB (Backend). The frontend interacts with the AWS Lambda function through an API Gateway.

🚀 Features

✅ Add tasks to a DynamoDB table
✅ Fetch and display tasks from the database
✅ Serverless architecture using AWS Lambda
✅ API integration with AWS API Gateway
✅ Hosted frontend (Optional: AWS S3 & CloudFront)


🛠 Tech Stack

Frontend: HTML, CSS, JavaScript (Fetch API)
Backend: AWS Lambda (Python), API Gateway, DynamoDB
Deployment: AWS S3 (for frontend hosting), GitHub
🏗 Setup & Deployment


1️⃣ Clone the Repository
git clone (https://github.com/Vinothraja2405/Serverless-ToDoList-using-Aws-Services)
cd serverless-todo-list

2️⃣ Set Up the AWS Backend

Create a DynamoDB TableGo to AWS DynamoDB.
Create a table named TodoTable.
Set taskId as the partition key (String).
Enable On-Demand capacity mode.
Deploy the AWS Lambda FunctionGo to AWS Lambda → Create a new function.
Choose Author from scratch.
Runtime: Python 3.x.
Upload your lambda_function.py file.
Add DynamoDB Full Access permissions.
Deploy the function.
Create an API GatewayGo to AWS API Gateway → Create a new HTTP API.
Create a POST route (/tasks) → Link to Lambda function.
Create a GET route (/tasks) → Link to Lambda function.
Enable CORS for frontend access.
Deploy and copy the API Endpoint URL.

3️⃣ Configure the Frontend
Open index.html and update the API URL:
const apiUrl = "https://your-api-gateway-url.amazonaws.com/dev/tasks";
Save the file.

4️⃣ Run Locally

Open index.html in a browser:
open index.html  # Mac/Linux
start index.html  # Windows

5️⃣ Deploy Frontend to S3 (Optional)If you want to host the frontend:

Create an S3 bucket (Enable public access).
Upload index.html and styles.css.
Enable Static website hosting.
Copy the S3 URL and access your app!

📌 Contributing  Feel free to submit pull requests if you’d like to improve this project!


