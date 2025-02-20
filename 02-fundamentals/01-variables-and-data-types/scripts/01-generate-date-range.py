from datetime import datetime, timedelta

# Date range configuration
START_DATE = datetime(2022, 1, 1)
END_DATE = datetime.today()
DATE_CHUNK_MONTHS = 9  # Split into ~9 month chunks for 4 batches
def generate_date_ranges():
    current = datetime(2022, 1, 1)
    while current < END_DATE:
        chunk_end = current + timedelta(days=270)  # 9 months
        yield (current, min(chunk_end, END_DATE))
        current = chunk_end + timedelta(days=1)

if __name__ == "__main__":
    for start_date, end_date in generate_date_ranges():
        print(f"Processing data from {start_date} to {end_date}")