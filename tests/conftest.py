"""

import pytest
import pymysql.cursors
import sshtunnel


@pytest.fixture(scope="function")
def conn_to_db():
    tunnel = sshtunnel.SSHTunnelForwarder(
        ('78.46.93.126', 927),
        ssh_username='qa',
        ssh_password='aczekj954lwkfj85',
        remote_bind_address=('localhost', 3306),
        local_bind_address=('localhost', 3307),
    )
    tunnel.start()
    global conn_to_test_db
    conn_to_test_db = pymysql.connect(host='localhost',
                                      user='qa',
                                      port=3307,
                                      password='p363Vw3SxEAAdWND',
                                      db='explorer_dev',
                                      charset='latin1',
                                      cursorclass=pymysql.cursors.DictCursor)
    yield tunnel, conn_to_test_db
    tunnel.close()
    conn_to_test_db.close()


@pytest.fixture
def return_connection(conn_to_db):
    return conn_to_test_db


########################################################################################

@pytest.fixture()
def connection(return_connection):  # Использовать подключение из (имя фикстуры) фикстуры
    return return_connection  # Вернуть подключение для выполнения запроса


def test_make_request():  # Выполнить запрос (заявка для получения токена)
    response = requests.request("POST", url, data=payload, headers=headers)
    assert response.status_code == 200


def test_check_email_in_db(connection):  # Проверить в DB есть ли запись с указанным  email
    with connection as cursor:
        sql = 'SELECT email FROM explorer_dev.explorer_user_key_requests ' \
              'WHERE email = %s'
        cursor.execute(sql, user_email)
        result = cursor.fetchone().get('email')
        assert result == user_email




"""