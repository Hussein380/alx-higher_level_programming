-- converts the entir r databse hbtn_Oc_O to UTF8
USE 'hbtn_0c_0'
ALTER TABLE 'first_table'
CONVERT TO CHARACTER SET utf8mb4 utf8mb4 COLLATE utf8mb4_unicode_ci;
