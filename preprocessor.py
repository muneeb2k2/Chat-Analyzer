import re
import pandas as pd

def preprocess(data):

    pattern = r'(\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s(?:AM|PM))\s-\s(.*?):\s(.*)'
    matches = re.findall(pattern, data)

    df = pd.DataFrame(matches, columns=['message_date', 'user', 'message'])

    df['date'] = pd.to_datetime(
        df['message_date'],
        format='%m/%d/%y, %I:%M %p',
        errors='coerce'
    )

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['hours'] = df['date'].dt.hour
    df['minutes'] = df['date'].dt.minute

    df.drop(columns=['message_date'], inplace=True)

    return df