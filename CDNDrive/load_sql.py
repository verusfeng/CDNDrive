def load_history_to_sql_db(metadict):
    # this function add by me ...  COMPUTERNAME=LAPTOP-IJTKOVMF
    ''' 
{'time': 1613238715,
 'filename': 'Joplin-Setup-1.4.19.exe',
 'size': 164033816,
 'sha1': '704119bbf7639f78157d949b834e8e3a3cfdd345',
 'block': [],
 'url': 'bdex://17e543b86c128e7a68f477ccf2649ed7d9e81c93'}
    '''

    import os , sqlite3,logging ,json ,base64
    logging.basicConfig(level = 0 )
    if os.getenv("COMPUTERNAME") == "LAPTOP-IJTKOVMF":  # my acer laptop.. 
        # sqlite3.db -> bilidrive 
        db_url = [each for each in os.getenv("database").split(";") if "sqlite3.db" in each][0].strip()
        logging.info(db_url)
        with sqlite3.connect(db_url) as db:
            # create_table_sql = '''
            # CREATE TABLE IF NOT EXISTS bilidrive (
            # sha1        text   PRIMARY KEY
            #                     NOT NULL,
            # upload_time timestamp NOT NULL,
            # filename    text NOT NULL,
            # size        BIGINT NOT NULL,
            # url         TEXT   NOT NULL, 
            # block_list_base64  TEXT NOT NULL
            # );'''
            # db.execute(create_table_sql)

            replace_sql = '''
            REPLACE INTO bilidrive (sha1 , upload_time , filename, size , url , block_list_base64)
            VALUES ("{sha1}" , {upload_time} , "{filename}", {size} , "{url}" , "{block_list_base64}");
            '''
            sha1 = metadict["sha1"]
            upload_time = metadict["time"]
            filename = metadict["filename"].replace("'","''")
            size = metadict["size"]
            url = metadict["url"]
            block_list_base64 = base64.b64encode( json.dumps(metadict["block"]).encode() ).decode()

            string =  replace_sql.format(sha1= sha1, upload_time = upload_time, filename = filename , size = size , url = url , block_list_base64 = block_list_base64)
            db.execute(string)
            db.commit()
        # db.close()

    # end if 

# end def load_history...