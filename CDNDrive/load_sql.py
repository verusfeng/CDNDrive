# -*- coding: utf-8 -*-

import os
import sqlite3
import logging
import json
import base64
import pathlib

logging.basicConfig(level=0)


def load_history_to_sql_db(metadict):
    db_url = pathlib.PurePath(
        os.getenv("HOME"), ".cdndrive", "cdrive_sqlite.db")
    logging.debug(f"sqlite3 db url is {db_url}")

    with sqlite3.connect(db_url) as db:
        replace_sql = '''
            REPLACE INTO bilidrive (sha1 , upload_time , 
            filename, size , url , block_list_base64)
            VALUES ("{sha1}" , {upload_time} , "{filename}", 
            {size} , "{url}" , "{block_list_base64}");
            '''
        sha1 = metadict["sha1"]
        upload_time = metadict["time"]
        filename = metadict["filename"].replace("'", "''")
        size = metadict["size"]
        url = metadict["url"]
        block_list_base64 = base64.b64encode(
            json.dumps(metadict["block"]).encode()).decode()

        string = replace_sql.format(sha1=sha1, upload_time=upload_time,
                                    filename=filename, size=size, url=url,
                                    block_list_base64=block_list_base64)
        db.execute(string)
        db.commit()
    # db.close()
# end if
# end def load_history...
