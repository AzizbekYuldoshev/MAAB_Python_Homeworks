# 1. Why do you think companies analyze large volumes of data?
""" Companies analyze data to remove guesswork. Large volumes of data reveal patterns, trends, and anomalies that are invisible in small samples. 
This helps them predict customer behavior, optimize costs, and make decisions based on facts rather than "gut feelings." """

#2. If Excel is difficult for large data, how can Python help?
""" Python (specifically the Pandas library) handles data in the computer's RAM, not in a visual grid like Excel.
Automation: You write the logic once, and it can process millions of rows instantly.
No Crashing: Excel often freezes with 500k+ rows; Python can handle millions without breaking a sweat.
Reproducibility: You can re-run the same script on new data every day with one click. """

#3. How would you analyze 10,000 daily transactions?
""" I would use an ETL (Extract, Transform, Load) approach:
Extract: Use SQL to pull the data from the database.
Transform: Use Python to clean the data (fix dates, remove duplicates) and calculate totals.
Analyze: Group the data by "Region" or "Product Category" to see where the money is coming from.
Visualize: Use a tool like Power BI or Python libraries (Matplotlib/Seaborn) to create a daily dashboard. """

#4. What tasks can Python be useful for in BI?
""" Data Cleaning: Removing "junk" data or fixing inconsistent formats automatically.
Data Integration: Combining data from different sources (e.g., a SQL database + a CSV file + a Website API).
Advanced Analytics: Performing statistical calculations or machine learning (predicting future sales).
Automation: Scheduling reports to be generated and emailed without human intervention. """

#5. Comparing profit year-over-year with Python?
"""I would use the .groupby() function to group the data by the "Year" column and then apply the .sum() function to the "Profit" column. 
I would then use a Line Chart or Bar Chart to visually compare the growth between years. """

#6. Difficulties of working with large data without Python?
""" The "Excel Wall": You will hit the row limit or face constant software crashes.
Human Error: Manually copying, pasting, and sorting data leads to mistakes that are hard to find.
Time Waste: Tasks that take hours to do manually in Excel can be done in seconds with Python.
Static Results: Without code, your analysis is a "one-time" thing; you have to do all the work again when next month's data arrives. """