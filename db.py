import sqlite3

arr = []


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_column(self, new_column):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`for_new_column`) VALUES(?)", (new_column,))

    def set_time(self, last_id, date_time):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `month` = ? WHERE id = ?", (date_time, last_id,))

    def set_place(self, last_id, place):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `place` = ? WHERE id = ?", (place, last_id))

    def get_last_place(self, unique_id):
        with self.connection:
            result = self.cursor.execute("SELECT `place` FROM users WHERE id = ?", (unique_id,)).fetchmany(1)
            return result[0][0]

    def set_abroad_or_local_status(self, unique_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `abroad_or_local_hol` = ? WHERE id = ?", (status, unique_id))

    def get_last_id(self):
        with self.connection:
            result = self.cursor.execute("SELECT `id` FROM `users`").fetchall()
            for row in result:
                last_number = row[-1]

            return last_number

    def set_grade(self, last_id, grade):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `user_grade` = ? WHERE id = ?", (grade, last_id))

    def get_all_places(self):
        with self.connection:
            result = self.cursor.execute("SELECT `place` FROM `users`").fetchall()

            row = [r for r in result]
            return row

    def set_wint_or_sum_relax(self, wint_or_sum, month):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `wint_or_sum_relax` = ? WHERE `month` = ?",
                                       (wint_or_sum, month))

    def check_month(self):
        with self.connection:
            self.set_wint_or_sum_relax('winter', 12)

            self.set_wint_or_sum_relax('summer', 6)

            self.set_wint_or_sum_relax('winter', 1)

            self.set_wint_or_sum_relax('summer', 7)

            self.set_wint_or_sum_relax('winter', 2)

            self.set_wint_or_sum_relax('summer', 8)

    def get_abroad_or_local_hol(self, last_id):
        with self.connection:
            result = self.cursor.execute("SELECT `abroad_or_local_hol` FROM users WHERE id = ?", (last_id,)).fetchmany(
                1)
            return result[0][0]

    def get_month(self, last_id):
        with self.connection:
            result = self.cursor.execute("SELECT `month` FROM users WHERE id = ?", (last_id,)).fetchmany(1)
            return result[0][0]

    def set_act_or_pas_relax(self, last_id, act_or_pas):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `act_or_pas_relax` = ? WHERE `id` = ?",
                                       (act_or_pas, last_id))

    def count_middle_grade(self, state):
        with self.connection:
            count_sum = 0
            count = 0

            if state == 'local':
                result = self.cursor.execute(
                    "SELECT `user_grade` FROM users WHERE abroad_or_local_hol == 'local'").fetchall()

            elif state == 'abroad':
                result = self.cursor.execute(
                    "SELECT `user_grade` FROM users WHERE abroad_or_local_hol == 'abroad'").fetchall()

            elif state == 'active':
                result = self.cursor.execute(
                    "SELECT `user_grade` FROM users WHERE act_or_pas_relax == 'active'").fetchall()

            elif state == 'passive':
                result = self.cursor.execute(
                    "SELECT `user_grade` FROM users WHERE act_or_pas_relax == 'passive'").fetchall()


            elif state == 'winter':
                result = self.cursor.execute(
                    "SELECT `user_grade` FROM users WHERE wint_or_sum_relax == 'winter'").fetchall()

            elif state == 'summer':
                result = self.cursor.execute(
                    "SELECT `user_grade` FROM users WHERE wint_or_sum_relax == 'summer'").fetchall()

            for row in result:
                count_sum += int(row[0])
                count += 1

            return round(float(count_sum / count), 1)

    def count_grades(self, state):
        with self.connection:
            count = 0

            if state == 'local':
                result = self.cursor.execute(
                    "SELECT `user_grade` FROM users WHERE abroad_or_local_hol == 'local'").fetchall()

            elif state == 'abroad':
                result = self.cursor.execute(
                    "SELECT `user_grade` FROM users WHERE abroad_or_local_hol == 'abroad'").fetchall()

            for row in result:
                count += 1

            return count

    def get_abroad_or_local_hol_grade(self):
        with self.connection:
            result = self.cursor.execute("SELECT `user_grade` FROM users").fetchall()
            return result[0][0]

    def set_middle_grade(self, state, value, current_date=0):
        with self.connection:
            if state == 'local':
                return self.cursor.execute("UPDATE result SET `local_grade` = ? WHERE `current_date` = ?",
                                           (value, current_date,))

            elif state == 'abroad':
                return self.cursor.execute("UPDATE result SET `abroad_grade` = ? WHERE `current_date` = ?",
                                           (value, current_date,))

            elif state == 'active':
                return self.cursor.execute("UPDATE result SET `act_relax_grade` = ? WHERE `current_date` = ?",
                                           (value, current_date,))

            elif state == 'passive':
                return self.cursor.execute("UPDATE result SET `pass_relax_grade` = ? WHERE `current_date` = ?",
                                           (value, current_date,))


            elif state == 'winter':
                return self.cursor.execute("UPDATE result SET `wint_rel_grade` = ? WHERE `current_date` = ?",
                                           (value, current_date,))

            elif state == 'summer':
                return self.cursor.execute("UPDATE result SET `summer_rel_grade` = ? WHERE `current_date` = ?",
                                           (value, current_date,))

    def set_result_date(self, date):
        with self.connection:
            return self.cursor.execute("INSERT INTO `result` (`current_date`) VALUES(?)", (date,))

    def delete_result(self):
        with self.connection:
            return self.cursor.execute("DELETE FROM result")


db = Database('database.db')
