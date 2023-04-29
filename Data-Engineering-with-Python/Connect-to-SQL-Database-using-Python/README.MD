# How to Connect to an SQL Database using Python

## Table Of Contents
- [Further Reading]()
  - [freeCodeCamp - How to Generate Automated Reports from a SQL Database Using Python](https://www.freecodecamp.org/news/automating-report-generation-from-sql-databases-using-python/)

# Connect to PostgreSQL Database using Python
* we use the `psycopg2` library.
* code snippet:

    ```py
        import psycopg2

        conn = psycopg2.connect(
        host="localhost",
        database="mydatabase",
        user="myusername",
        password="mypassword"
        )
    ```

* Replace the values in the `host`, `database`, `user`, and `password` parameters with the appropriate values for your database.

# How to Retrieve Data from the SQL Database

# How to Retrieve Data from the PostgreSQL Database
```py
    cur = conn.cursor();
    cur.execute("SELECT name, email FROM customers");

    rows = cur.fetchall();
```

# How to Create a Report
* Next, we need to create the report using a Python library such as `ReportLab` or `PyPDF2`.

    ```py
        from reportlab.pdfgen import canvas

        # Create a new PDF document
        pdf = canvas.Canvas("report.pdf")

        # Write the report title
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(50, 750, "Customer Report")

        # Write the report content
        pdf.setFont("Helvetica", 12)
        y = 700
        for row in rows:
            pdf.drawString(50, y, "Name: " + row[0])
            pdf.drawString(50, y - 20, "Email: " + row[1])
            pdf.drawString(50, y - 40, "Phone: " + row[2])
            y -= 60

        # Save the PDF document
        pdf.save()
    ```

* This code creates a new PDF document, writes the report title, and loops through the data retrieved from the SQL database to write the report content. The final PDF report is saved as `report.pdf`.