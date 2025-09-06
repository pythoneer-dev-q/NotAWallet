# --- database --- #

MAIN_DATABASE = 'NotAWallet'

# --- collections --- #

database = 'not_users'
database_transactions = 'not_transaction'
limited_users = 'not_limited'
user_invouces = 'not_usersInvouces'
user_checks = 'not_usersChecks'
collection_list = [database, database_transactions, limited_users, user_invouces, user_checks ]
# --- errs --- #
errs_transactions = ['SUM_ERR', 'SRVR_ERR', 'WLT_NT_EXST', 'ACTIVATED', 'USER_ERR']