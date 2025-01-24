from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def form():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>MIV Form</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                padding: 20px;
                background-color: #f4f4f9;
            }
            label {
                display: block;
                margin-top: 10px;
                font-weight: bold;
            }
            input, select {
                width: 100%;
                padding: 8px;
                margin-top: 5px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            button {
                background-color: #007BFF;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 4px;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <h1>MIV Form</h1>
        <form action="/submit" method="post">
            <label for="mivNumber">MIV Number</label>
            <input type="text" id="mivNumber" name="mivNumber">

            <label for="mivDate">MIV Date</label>
            <input type="date" id="mivDate" name="mivDate" required>

            <label for="indentNumber">Indent Number</label>
            <input type="text" id="indentNumber" name="indentNumber">

            <label for="itemCode">Item Code</label>
            <input type="text" id="itemCode" name="itemCode" required>

            <label for="category">Category</label>
            <select id="category" name="category" required>
                <option value="Category1">Category 1</option>
                <option value="Category2">Category 2</option>
            </select>

            <label for="quantityRequested">Quantity Requested</label>
            <input type="number" id="quantityRequested" name="quantityRequested" min="0" step="0.001" required>

            <label for="quantityIssued">Quantity Issued</label>
            <input type="number" id="quantityIssued" name="quantityIssued" min="0" step="0.001" required>

            <label for="freeIssueMaterial">Free Issue Material</label>
            <input type="checkbox" id="freeIssueMaterial" name="freeIssueMaterial">

            <label for="submittedBy">Submitted By</label>
            <input type="text" id="submittedBy" name="submittedBy" required>

            <button type="submit">Submit</button>
        </form>
    </body>
    </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get form data
        data = {
            "mivNumber": request.form.get("mivNumber"),
            "mivDate": request.form.get("mivDate"),
            "indentNumber": request.form.get("indentNumber"),
            "itemCode": request.form.get("itemCode"),
            "category": request.form.get("category"),
            "quantityRequested": request.form.get("quantityRequested"),
            "quantityIssued": request.form.get("quantityIssued"),
            "freeIssueMaterial": "freeIssueMaterial" in request.form,
            "submittedBy": request.form.get("submittedBy")
        }

        # Log the submitted data
        print("Form Submitted:", data)

        # Respond with JSON
        return jsonify({"message": "Form submitted successfully!", "data": data}), 200
    except Exception as e:
        print("Error:", e)
        return jsonify({"message": "An error occurred while submitting the form."}), 500

if __name__ == '__main__':
    app.run(debug=True)
