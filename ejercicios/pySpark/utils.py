from IPython.core.display import HTML
display(HTML("<style>pre { white-space: pre !important; }</style>"))

import datetime
from pyspark.sql import Row

def schema_to_ddl(spark, df):
    return spark.sparkContext._jvm.org.apache.spark.sql.types.DataType.fromJson(df.schema.json()).toDDL().replace(" NOT NULL", "")

def difference(l1, l2):
    return list(set(l1) - set(l2))

def write_tmp_df(df_list):
    for df,table_name in df_list:
        df.write.mode("overwrite").parquet("../../resources/data/tmp/parquet/" + table_name)

def read_tmp_df(spark, df_list):
    dict_dfs = {}
    for table_name in df_list:
        df = spark.read.parquet("../../resources/data/tmp/parquet/" + table_name)
        dict_dfs[table_name] = df
    return dict_dfs

top_movies = [
    Row(title='Band of Brothers (2001)', year=2001, genre='Action', top=1),
    Row(title='Seven Samurai (Shichinin no samurai) (1954)', year=1954, genre='Action', top=2),
    Row(title='Fight Club (1999)', year=1999, genre='Action', top=3),
    Row(title='Over the Garden Wall (2013)', year=2013, genre='Adventure', top=1),
    Row(title='Seven Samurai (Shichinin no samurai) (1954)', year=1954, genre='Adventure', top=2),
    Row(title='Spirited Away (Sen to Chihiro no kamikakushi) (2001)', year=2001, genre='Adventure', top=3),
    Row(title='Over the Garden Wall (2013)', year=2013, genre='Animation', top=1),
    Row(title='Spirited Away (Sen to Chihiro no kamikakushi) (2001)', year=2001, genre='Animation', top=2),
    Row(title='Parasite (2019)', year=2019, genre='Comedy', top=1),
    Row(title='Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb (1964)', year=1964, genre='Comedy', top=2),
    Row(title='Shawshank Redemption, The (1994)', year=1994, genre='Crime', top=1),
    Row(title='Godfather, The (1972)', year=1972, genre='Crime', top=2),
    Row(title='Usual Suspects, The (1995)', year=1995, genre='Crime', top=3),
    Row(title='Godfather: Part II, The (1974)', year=1974, genre='Crime', top=4),
    Row(title='Fight Club (1999)', year=1999, genre='Crime', top=5),
    Row(title='Planet Earth (2006)', year=2006, genre='Documentary', top=1),
    Row(title='Planet Earth II (2016)', year=2016, genre='Documentary', top=2),
    Row(title='Blue Planet II (2017)', year=2017, genre='Documentary', top=3),
    Row(title='The Blue Planet (2001)', year=2001, genre='Documentary', top=4),
    Row(title='Shawshank Redemption, The (1994)', year=1994, genre='Drama', top=1),
    Row(title='Band of Brothers (2001)', year=2001, genre='Drama', top=2),
    Row(title='Parasite (2019)', year=2019, genre='Drama', top=3),
    Row(title='Godfather, The (1972)', year=1972, genre='Drama', top=4),
    Row(title='Twin Peaks (1989)', year=1989, genre='Drama', top=5),
    Row(title='12 Angry Men (1957)', year=1957, genre='Drama', top=6),
    Row(title='Godfather: Part II, The (1974)', year=1974, genre='Drama', top=7),
    Row(title='Over the Garden Wall (2013)', year=2013, genre='Drama', top=8),
    Row(title='Seven Samurai (Shichinin no samurai) (1954)', year=1954, genre='Drama', top=9),
    Row(title='Fight Club (1999)', year=1999, genre='Drama', top=10),
    Row(title="Schindler's List (1993)", year=1993, genre='Drama', top=11),
    Row(title="One Flew Over the Cuckoo's Nest (1975)", year=1975, genre='Drama', top=12),
    Row(title='Lives of Others, The (Das leben der Anderen) (2006)', year=2006, genre='Drama', top=13),
    Row(title='Casablanca (1942)', year=1942, genre='Drama', top=14),
    Row(title='Spirited Away (Sen to Chihiro no kamikakushi) (2001)', year=2001, genre='Fantasy', top=1),
    Row(title='Twin Peaks (1989)', year=1989, genre='Mystery', top=1),
    Row(title='Usual Suspects, The (1995)', year=1995, genre='Mystery', top=2),
    Row(title='Rear Window (1954)', year=1954, genre='Mystery', top=3),
    Row(title='Lives of Others, The (Das leben der Anderen) (2006)', year=2006, genre='Romance', top=1),
    Row(title='Casablanca (1942)', year=1942, genre='Romance', top=2),
    Row(title='Usual Suspects, The (1995)', year=1995, genre='Thriller', top=1),
    Row(title='Fight Club (1999)', year=1999, genre='Thriller', top=2),
    Row(title='Rear Window (1954)', year=1954, genre='Thriller', top=3),
    Row(title='Lives of Others, The (Das leben der Anderen) (2006)', year=2006, genre='Thriller', top=4),
    Row(title='Band of Brothers (2001)', year=2001, genre='War', top=1),
    Row(title="Schindler's List (1993)", year=1993, genre='War', top=2),
    Row(title='Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb (1964)', year=1964, genre='War', top=3)]