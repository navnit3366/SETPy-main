from database import SLEEPdatabase

test_db = SLEEPdatabase('sleep.db')

entry_tracker = [
    ('02/27/22','22:30:00','02/28/22','07:48:00','09:18:00', 'Excellent'),
    ('02/28/22','20:40:00','03/01/22','06:15:00','09:35:00', 'Good'),
    ('03/01/22','23:05:00','03/02/22','06:23:00','07:18:00', 'Needs Improvement')
]

# test_db.delete_table("sleep_tracker")

# test_db.insert_all("sleep_tracker", entry_tracker)

# test_db.insert_one('sleep_tracker',
#                 '3/2/22','22:40:00',
#                 '3/3/22','06:18:00',
#                 '07:38:00', 'Bad')
                
# test_db.remove('sleep_tracker', 1)

# test_db.update('sleep_tracker', 3,
#                 '12/24/21','22:40:00',
#                 '12/25/21','06:18:00',
#                 '07:38:00', 'lol')

data_sleep_tracker = test_db.fetch('sleep_tracker')
print(type(data_sleep_tracker))
for i in data_sleep_tracker:
    print(f'• {i}')

