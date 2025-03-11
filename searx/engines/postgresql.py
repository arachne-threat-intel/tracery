# SPDX-License-Identifier: AGPL-3.0-or-later
"""
 PostgreSQL database (Offline)
"""

# error is ignored because the admin has to
# install it manually to use the engine
# pylint: disable=import-error

import psycopg

engine_type = 'offline'
host = "127.0.0.1"
port = "5432"
database = ""
username = ""
password = ""
query_str = ""
limit = 10
paging = True
result_template = 'key-value.html'


def init(engine_settings):
    if 'query_str' not in engine_settings:
        raise ValueError('query_str cannot be empty')

    if not engine_settings['query_str'].lower().startswith('select '):
        raise ValueError('only SELECT query is supported')


def get_connection():
    """Creates and returns a new connection."""
    connection_string = (
        f"hostaddr='{host or ''}' "
        f"port='{port or ''}' "
        f"dbname='{database}' "
        f"user='{username}' "
        f"password='{password}'"
    )
    return psycopg.connect(conninfo=connection_string)


def search(query, params):
    query_params = {'query': query}
    query_to_run = query_str + ' LIMIT {0} OFFSET {1}'.format(limit, (params['pageno'] - 1) * limit)

    with get_connection() as _connection:
        with _connection.cursor() as cur:
            cur.execute(query_to_run, query_params)

            return _fetch_results(cur)


def _fetch_results(cur):
    results = []
    titles = []

    try:
        titles = [column_desc.name for column_desc in cur.description]

        for res in cur:
            result = dict(zip(titles, map(str, res)))
            result['template'] = result_template
            results.append(result)

    # no results to fetch
    except psycopg.ProgrammingError:
        pass

    return results
