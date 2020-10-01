-- User migration is simplest with these views
CREATE VIEW users_user AS SELECT * FROM auth_user;
CREATE VIEW users_user_groups AS SELECT * FROM auth_user_groups;
CREATE VIEW users_user_user_permissions AS SELECT * FROM auth_user_user_permissions;
