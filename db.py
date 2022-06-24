import sqlite3
import time

arr = []


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES(?)", (user_id,))

    def user_money(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `money` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchmany(1)
            return int(result[0][0])

    def get_user_status(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `cast` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchmany(1)
            return result[0][0]

    def set_user_status(self, cast, user_id):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `cast` = ? WHERE `user_id` = ?", (cast, user_id,))

    def set_money(self, user_id, money):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `money` = ? WHERE `user_id` = ?", (money, user_id,))

    def add_check(self, user_id, money, bill_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `check` (`user_id`, `money`, `bill_id`) VALUES(?,?,?)",
                                       (user_id, money, bill_id,))

    def get_check(self, bill_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `check` WHERE `bill_id` = ?", (bill_id,)).fetchmany(1)
            if not bool(len(result)):
                return False
            return result[0]

    def delete_check(self, bill_id):
        with self.connection:
            return self.cursor.execute("DELETE FROM `check` WHERE `bill_id` = ?", (bill_id,))

    def get_all_users_id(self):
        with self.connection:
            result = self.cursor.execute("SELECT `user_id` FROM `users`").fetchall()
            for row in result:
                users_id = row[0]
                arr.append(users_id)

            return arr

    def set_nickname(self, user_id, nickname):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `user_nickname` = ? WHERE `user_id` = ?",
                                       (nickname, user_id,))

    def set_password(self, user_id, password):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `password` = ? WHERE `user_id` = ?", (password, user_id,))

    def get_nickname(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `user_nickname` FROM `users` WHERE `user_id` = ?",
                                         (user_id,)).fetchall()
            for row in result:
                nickname = str(row[0])

            return nickname

    def get_password(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `password` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                password = str(row[0])

            return password

    def check_admin(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `cast` FROM `users` WHERE `user_id`=?", (user_id,)).fetchall()
            try:
                return result[0][0]
            except Exception as e:
                print(e)

    def get_podpiska(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `subscribe` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                podpiska = str(row[0])

            return podpiska

    def set_time_sub(self, user_id, time_sub):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `time_sub` = ? WHERE `user_id` = ?", (time_sub, user_id,))

    def get_time_sub(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `time_sub` FROM `users` WHERE `user_id` = ?",
                                         (user_id,)).fetchall()
            for row in result:
                time_sub = int(row[0])

            try:
                return time_sub
            except:
                pass

    def get_sub_status(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `time_sub` FROM `users` WHERE `user_id` = ?",
                                         (user_id,)).fetchall()
            for row in result:
                time_sub = int(row[0])

            if time_sub > int(time.time()):
                return True
            else:
                return False

    def set_sub_status(self, user_id, sub_status):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `subscribe` = ? WHERE `user_id` = ?", (sub_status, user_id,))

    def set_photo(self, number, photo_id):
        with self.connection:
            return self.cursor.execute("UPDATE `advertisements` SET `photo_id` = ? WHERE `number` = ?",
                                       (photo_id, number,))

    def set__advertisement_name(self, number, name):
        with self.connection:
            return self.cursor.execute("UPDATE `advertisements` SET `name` = ? WHERE `number` = ?", (name, number))

    def set_description(self, number, description):
        with self.connection:
            return self.cursor.execute("UPDATE `advertisements` SET `description` = ? WHERE `number` = ?",
                                       (description, number))

    def set_price(self, number, price):
        with self.connection:
            return self.cursor.execute("UPDATE `advertisements` SET `price` = ? WHERE `number` = ?",
                                       (price, number))

    def set_advert_user_id(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `advertisements` (`user_id`) VALUES(?)", (user_id,))

    def set_advert_user_name(self, user_name, user_id):
        with self.connection:
            return self.cursor.execute("Update `advertisements` SET `user_name` = ? WHERE user_id = ?", (user_name, user_id))

    def get_photo_id(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `photo_id` FROM `advertisements` WHERE `user_id` = ?",
                                         (user_id,)).fetchall()
            for row in result:
                photo_id = str(row[0])

            return photo_id

    def check_max_advertisements(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `advertisements` WHERE `user_id` = ?", (user_id,)).fetchall()

            if len(result) <= 2:
                return True
            else:
                return False

    def get_all_user_advertisements(self, user_id):
        with self.connection:
            result = self.cursor.execute(
                "SELECT `photo_id`, `name`, `description`, `price`, `number` FROM `advertisements` WHERE `user_id` = ?",
                (user_id,)).fetchall()

        return result

    def get_all_advertisements(self, user_id):
        with self.connection:
            result = self.cursor.execute(
                "SELECT `photo_id`, `name`, `description`, `price`, `user_name` FROM `advertisements` WHERE user_id != ?", (user_id,)
            ).fetchall()

        return result

    def get_last_number(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `number` FROM `advertisements` WHERE `user_id` = ?",
                                         (user_id,)).fetchall()
            for row in result:
                last_number = row[-1]

            return last_number


    def delete_advertisement(self, user_id, number):
        with self.connection:
            return self.cursor.execute("DELETE FROM `advertisements` where `number` = ? and `user_id` = ?",
                                       (number, user_id,)).fetchall()

    def check_user_number(self, number, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `number` FROM `advertisements` WHERE `number` = ? and `user_id` = ?",
                                         (number, user_id)).fetchall()

            return bool(len(result))

    def delete_nul_advertisements(self):
        with self.connection:
            return self.cursor.execute(
                "DELETE FROM `advertisements` where `photo_id` = 'nul' or `name` = 'nul' or description = 'nul' or price = 'nul'",
                ()).fetchall()


db = Database("C:\\Users\\hdhrh\\Desktop\\pythonProject\\database.db")