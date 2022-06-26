from datetime import datetime


def check_country(place, database):
    if 'россия' in place.lower():
        database.set_abroad_or_local_status(database.get_last_id(), "local")

    else:
        database.set_abroad_or_local_status(database.get_last_id(), "abroad")


def get_and_set_result(database):
    local_grade = database.count_middle_grade('local')
    abroad_grade = database.count_middle_grade('abroad')

    summer_grade = database.count_middle_grade('summer')
    winter_grade = database.count_middle_grade('winter')

    act_rel_grade = database.count_middle_grade('active')
    pas_rel_grade = database.count_middle_grade('passive')

    now = datetime.now()

    database.set_result_date(datetime.now())
    database.set_middle_grade("local", local_grade, current_date=now)
    database.set_middle_grade("abroad", abroad_grade, current_date=now)
    database.set_middle_grade("winter", winter_grade, current_date=now)
    database.set_middle_grade("summer", summer_grade, current_date=now)
    database.set_middle_grade("active", act_rel_grade, current_date=now)
    database.set_middle_grade("passive", pas_rel_grade, current_date=now)

    return f"\n\nСредняя оценка местных зон отдыха: {local_grade}\nСредняя оценка зарубежных зон отдыха: {abroad_grade}\nСредняя оценка отдыха летом: {summer_grade}\nСредняя оценка отдыха зимой: {winter_grade}\nСредняя оценка активного отдыха: {act_rel_grade}\nСредняя оценка пассивного отдыха: {pas_rel_grade}\n\nОтечественных мест посещено: {database.count_grades(state='local')}\nЗарубежных мест посещено: {database.count_grades(state='abroad')}"
