import eventlet
from eventlet import GreenPool
from funcs_for_test import last_number_of_factorial, make_3_dim_list
gp = GreenPool()

for i in gp.imap(make_3_dim_list, [500]*10):
    print(i)


