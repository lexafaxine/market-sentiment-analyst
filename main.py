import crawl
import db
from sqlalchemy.dialects.postgresql import insert
import logging
import datetime
from datetime import timedelta

if __name__ == '__main__':
    key = 'WTAHAPPYACTIVITY'
    eg = crawl.EncryptDate(key)

    # connect to database
    DATABASE_URI = db.DATABASE_URI
    engine = db.create_engine(DATABASE_URI)
    Session = db.sessionmaker(bind=engine)
    conn = engine.connect()

    # start crawling
    date1 = datetime.date(2018, 8, 1)
    date2 = datetime.date(2020, 11, 11)

    delta = timedelta(days=1)
    post_date = date1-delta

    for i in range((date2-date1).days):
        post_date += delta
        print('======== start crawling posts on '+str(post_date)+' ========')
        try:
            post_list = crawl.get_post(eg, post_date)
            if len(post_list) == 0:
                print('error occurs on '+str(post_date))
                continue
            else:
                for x in post_list:
                    post_id = x['id']
                    up = x['sense']['up']
                    down = x['sense']['down']
                    title = x['title']
                    content = x['content']
                    views = x['views']
                    timestamp = x['post_date_format']
                    if len(x['tags']) > 0:
                        tags = x['tags'][0]['name']
                    else:
                        tags = None

                    # start insert
                    insert_stmt = insert(db.post).values(post_id=post_id, up=up, down=down, title=title, content=content,
                                                  views=views
                                                  , timestamp=timestamp, tags=tags)
                    do_nothing_stmt = insert_stmt.on_conflict_do_nothing(
                        index_elements=['post_id']
                    )
                    conn.execute(do_nothing_stmt)

                print(str(len(post_list))+' posts on '+str(post_date))

        except Exception as e:
            logging.exception(e)
            continue