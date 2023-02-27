# import sqlite3
#
# conn = sqlite3.connect('food_blog.db')
#
# cur = conn.cursor()
#
# # Executes some SQL query
# with conn:
#     conn.execute("CREATE TABLE IF NOT EXISTS meals (meal_id INTEGER PRIMARY KEY AUTOINCREMENT, meal_name TEXT NOT NULL UNIQUE)")
#     conn.execute("CREATE TABLE IF NOT EXISTS ingredients (ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT, ingredient_name TEXT NOT NULL UNIQUE)")
#     conn.execute("CREATE TABLE IF NOT EXISTS measures (measure_id INTEGER PRIMARY KEY AUTOINCREMENT, measure_name TEXT UNIQUE)")
#
# data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
#         "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
#         "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}
#
# # print(data["meals"])
# for k in data:
#     # for v in data.values():
#     for i in data[k]:
#         a = k[:-1]
#         conn.execute(f"INSERT INTO {k} ({a}_name) VALUES ('{i}');")
#         # print(a+"_name")
# conn.commit()
# conn.close()
# # cur.execute(f'INSERT INTO {data[i]} (id, number, pin, balance) VALUES ({j}, {self.key}, {self.pin}, 0);')
# # cur.execute("CREATE TABLE card (id INTEGER PRIMARY KEY AUTOINCREMENT, number VARCHAR(255) NOT NULL, pin VARCHAR(255) NOT NULL, balance INT DEFAULT 0)")
# # sql = "SELECT balance FROM card WHERE number = " + '4000005084440495' + " and pin = " + '9106'
#
# # cur.execute(sql)
# # myresult = cur.fetchone()
# # print(myresult)
# # for x in myresult:
# #     print(x)
#     # print("Balance: {0}".format(x))
# # After doing some changes in DB don't forget to commit them!
# # conn.commit()


import sqlite3
from sqlite3 import Error


def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    connection = None
    try:
        connection = sqlite3.connect('./food_blog.db')
        return connection
    except Error as e:
        print(e)
        return connection


def create_tables(conn):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    table_measures = """
    create table if not exists measures (
        measure_id INTEGER PRIMARY KEY,
        measure_name TEXT UNIQUE
    )
    """

    table_ingredients = """
    create table if not exists ingredients (
        ingredient_id INTEGER PRIMARY KEY,
        ingredient_name TEXT NOT NULL UNIQUE
    )
    """

    table_meals = """
    create table if not exists meals (
        meal_id INTEGER PRIMARY KEY,
        meal_name TEXT NOT NULL UNIQUE
    )
    """
    table_recipe = """
        create table if not exists recipes (
            recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_name TEXT NOT NULL ,
            recipe_description TEXT 
        )
        """
    table_serve = """
        create table if not exists serve (
            serve_id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_id INTEGER NOT NULL ,
            meal_id INTEGER NOT NULL, 
            FOREIGN KEY (meal_id)
       REFERENCES meals (meal_id) 
                   FOREIGN KEY (recipe_id)
       REFERENCES recipes (recipe_id) 
        )
        """
    table_quantity = """
        create table if not exists quantity (
            quantity_id INTEGER PRIMARY KEY AUTOINCREMENT,
            quantity INTEGER NOT NULL,
            measure_id INTEGER NOT NULL, 
            ingredient_id INTEGER NOT NULL, 
            recipe_id INTEGER NOT NULL ,
        FOREIGN KEY (recipe_id)
       REFERENCES recipes (recipe_id) 
        FOREIGN KEY (measure_id)
       REFERENCES meals (measure_id) 
       FOREIGN KEY (ingredient_id)
       REFERENCES meals (ingredient_id) 
        )
        """
    try:
        c = conn.cursor()
        c.execute(table_measures)
        c.execute(table_ingredients)
        c.execute(table_meals)
        c.execute(table_recipe)
        c.execute(table_serve)
        c.execute(table_quantity)
    except Error as e:
        print(e)


def insert_into_ingredients(conn, elements):
    try:
        cursor = conn.cursor()
        stmt = "insert into ingredients (ingredient_id, ingredient_name) values (?, ?)"
        values = [*map(lambda el: (None, el), elements)]
        cursor.executemany(stmt, values)
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False


def insert_into_measures(conn, elements):
    try:
        cursor = conn.cursor()
        stmt = "insert into measures  (measure_id , measure_name ) values (?, ?)"
        values = [*map(lambda el: (None, el), elements)]
        cursor.executemany(stmt, values)
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False


def insert_into_meals(connection, elements):
    try:
        cursor = connection.cursor()
        stmt = "insert into meals(meal_id, meal_name) values (?, ?)"
        values = [*map(lambda el: (None, el), elements)]
        cursor.executemany(stmt, values)
        connection.commit()
        return cursor
    except Error as e:
        print(e)
        return False

def insert_into_recipe(connection, elements, ela):
    try:
        cursor = connection.cursor()
        stmt = f"insert into recipes( recipe_name, recipe_description) values ('{elements}', '{ela}')"
        # values = [*map(lambda el, e: (None, el, e), elements, ela)]
        cursor.execute(stmt)
        # cursor.executemany(stmt, values)
        connection.commit()
        return cursor
    except Error as e:
        print(e)
        return False
def insert_into_serve(connection, elements, ela):
    try:
        cursor = connection.cursor()
        stmt = f"insert into serve( recipe_id, meal_id) values ('{elements}', '{ela}')"
        # values = [*map(lambda el, e: (None, el, e), elements, ela)]
        cursor.execute(stmt)
        # cursor.executemany(stmt, values)
        connection.commit()
        return cursor
    except Error as e:
        print(e)
        return False

def insert_into_quantity(connection,quantity, elements, ela, i):
    try:
        cursor = connection.cursor()
        stmt = f"insert into quantity( quantity, recipe_id, measure_id, ingredient_id) values ('{quantity}','{elements}', '{ela}', '{i}')"
        # values = [*map(lambda el, e: (None, el, e), elements, ela)]
        cursor.execute(stmt)
        # cursor.executemany(stmt, values)
        connection.commit()
        return cursor
    except Error as e:
        print(e)
        return False


def main(conn):
    data = {
        "meals": ("breakfast", "brunch", "lunch", "supper"),
        "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
        "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")
    }
    insert_into_ingredients(conn, data['ingredients'])
    insert_into_measures(conn, data['measures'])
    insert_into_meals(conn, data['meals'])
    count = 0
    while True:
        rec_name = input()
        if rec_name =="":
            conn.commit()
            conn.close()
            break
        desc_name = input()
        switcher = {
            1: "breakfast",
            2: "brunch",
            3: "lunch",
            4: "supper"
        }
        count +=1
        if len(rec_name) != 0 or len(desc_name)!=0:
            insert_into_recipe(conn, rec_name, desc_name)

            print("1) breakfast  2) brunch  3) lunch  4) supper ")
            a = input().split(" ")
            for i in a:
                insert_into_serve(conn, count, int(i))
            while True:
                in_qu = input().split(" ")
                if in_qu == ['']:
                    break
                cursor = conn.cursor()
                mea = cursor.execute(f"SELECT measure_id FROM measures where measure_name = '{in_qu[1]}' or measure_name like 'tbp%';").fetchone()[0]
                if mea == "":
                    ing = cursor.execute(f"SELECT ingredient_id FROM ingredients where ingredient_name like '%{in_qu[1]}%';").fetchone()[0]
                else:
                    ing = cursor.execute(f"SELECT ingredient_id FROM ingredients where ingredient_name like '%{in_qu[2]}%';").fetchone()[0]
                    if ing == "":
                        print("The measure is not conclusive!")
                    else:
                        insert_into_quantity(conn,in_qu[0], count, count, count )

            # if in_qu == ['']:
            #     break
        if len(rec_name) == 0 or len(desc_name)==0:
            conn.close()
            break
# def switch_demo():
#     switcher = {
#         1: "breakfast",
#         2: "brunch",
#         3: "lunch",
#         4: "supper"
#     }
    # print(switcher.get(5, "Invalid month"))

if __name__ == '__main__':
    init_conn = create_connection()
    create_tables(init_conn)
    main(init_conn)
    init_conn.close()