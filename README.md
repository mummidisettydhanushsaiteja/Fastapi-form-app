🚀 FastAPI Form Application

This is a FastAPI-based project 🌐 that serves a dynamic web form 📝 for capturing MIV (Material Issue Voucher) data. The form allows users to input details like MIV number, date, item codes, categories, quantities, and more. Submitted data is validated and processed by the FastAPI backend 🛠️.

✨ Features

- 🖥️ Dynamic Web Form: A user-friendly HTML form served by FastAPI.  
- ✔️ Validation: Backend validation for required fields using FastAPI's data handling.  
- 📄 JSON Response: Submitted data is returned as a JSON response.  
- 🔧 Customizable: Easily extend and modify for various use cases.

 🛠️ Technologies Used

- ⚡ FastAPI: A modern Python web framework for building APIs.  
- 🔌 Uvicorn: ASGI server for running the FastAPI application.  
- 🐍 Python: The main programming language used.

 📋 Prerequisites

- ✅ Python 3.7 or higher installed on your system.  
- ✅ `pip` (Python package manager).  

 ⚙️ Installation and Setup

1. Clone the Repository:  
   
   git clone https://github.com/your-username/fastapi-form-app.git
   cd fastapi-form-app
   

2. Create a Virtual Environment (optional):  
   
   python -m venv venv
   source venv/bin/activate    For Linux/Mac
   .\\venv\\Scripts\\activate   For Windows
   

3. Install Dependencies:  
   
   pip install fastapi uvicorn
   

4. Run the Application:  
   
   uvicorn main:app --reload
   

5. Access the Application:  
   Open your browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
