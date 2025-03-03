import mysql.connector

def get_channel_data(channel_name):
    """
    Fetch data from MySQL database where the channel field matches the given channel_name.

    :param db_config: Dictionary containing database configuration with keys 'host', 'user', 'password', and 'database'.
    :param channel_name: The name of the channel to search for.
    :return: List of rows matching the channel_name.
    """
    db_config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': '',
        'database': 'produksi_tv'
    }
    try:
        # Establish the database connection
        connection = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )

        cursor = connection.cursor(dictionary=True)

        # Query to fetch data where channel field matches the given channel_name
        query = "SELECT * FROM live_streaming WHERE channel = %s"
        cursor.execute(query, (channel_name,))

        # Fetch all matching rows
        result = cursor.fetchall()
        
        if result:
            formatted_result = dict(
            ENVIRONMENT="dev",
            URL=result[0].get('url', ''),
            QUALITY=result[0].get('resolusi', ''),
            UPLOAD_LOCATION=result[0].get('upload_location', 'storage/'+result[0].get('channel', '').replace('STREAMING', '').lower()),
            COOKIES=result[0].get('cookies', ''),
            HEADERS={
                'user-agent': result[0].get('user_agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36')
            }
            )
            print(formatted_result)
            return formatted_result
        else:
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# channel_name = 'KOMPASSTREAMING'
# data = get_channel_data(channel_name)
# print(data)