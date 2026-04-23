from urlextract import URLExtract
from wordcloud import WordCloud

extractor = URLExtract()

def fetch_stats(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]

    words = []
    for message in df['message']:
        words.extend(message.split())

    num_media_messages = df[df['message'] == '<Media omitted>'].shape[0]

    links = []
    for message in df['message']:
        links.extend(extractor.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)


def most_busy_user(df):
    x = df['user'].value_counts().head()

    new_df = (df['user'].value_counts() / df.shape[0] * 100)\
        .round(2)\
        .reset_index()\
        .rename(columns={'index': 'name', 'user': 'percent'})

    return x, new_df


def create_word_cloud(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc = wc.generate(df['message'].str.cat(sep=" "))

    return df_wc