# SQLAlchemy

# Version Check

    import sqlalchemy
    sqlalchemy.__version__

# Establishing Connectivity - the Engine

    from sqlalchemy import create_engine
    engine = create_engine(
        'sqlite+pysqlite:///:memory:', echo=True, future=True
    )

# Working with Transactions and the DBAPI

# Basics of Statement Execution

## Fetching Rows

    from sqlalchemy import text

    with engine.connect() as conn:
        result = conn.execute(text('select id,username from user'))
        
        # Attribute Name
        for row in result:
            id = row.id
            username = row.username
            
        # Tuple Assignment
        for key, value in result:
            pass

        # Integer Index
        for row in result:
            id = row[0]

        # Mapping Access
        for dict_row in result.mappings:
            id = dict_row['id]
            username = dict_row['username']

## Sending Parameters

    from sqlalchemy import text

    with engine.connect() as conn:
        result = conn.execute(
            text('SELECT id, username FROM some_table' WHERE age > :age),
            {'age',28}
        )

        for row in result:
            id = row.id
            username = row.username

## Sending Multiple Parameters

    from sqlalchemy import text

    with engine.connect() as conn:
        conn.execute(
            text('INSERT INTO  user(username,password) VALUES(:username, :password)'),
            [
                {'username': 'sarah','password': '123456'},
                # ...
            ]
        )

        conn.commit()

## Bundling Parameters with a Statement

    stmt = text('SELECT username, age FROM \
    user WHERE age > :age ORDER BY create_time).bindparams(age=27)

    with engine.connect() as conn:
        result = conn.execute(stmt)
        for row in result:
            username = row.username


# Executing with an ORM Session

    from sqlalchemy.orm import Session

    stmt = 'SELECT username, is_active FROM user WHERE is_active = :isactive'

    with Session(engine) as session:
        result = session.execute(stmt, {'is_active': True})
        for row in result:
            username = row.username

    with Session(engine) as session:
        result = session.execute(
            text('UPDATE user SET is_active=:is_active WHERE username=:username'),
            [
                {'usernaem': 'alex', 'is_active'=True},
                {'usernaem': 'lily', 'is_active'=True}
            ]
        )
        session.commit()

# Tip

    知识都是有用的，只是你不知道什么时候用