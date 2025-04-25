user_val = int(input())
num_users = int(input())
update_direction = int(input())


cond_str =  'negative' if user_val < 0 else 'non-negative'
num_users = (num_users + 1) if update_direction == 3 else (num_users - 1)
print(user_val, 'is', cond_str)
print('New value is:', num_users)