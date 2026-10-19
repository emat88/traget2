flagged_users = [
    "  AdminUser_99  ",
    " JDoe42",
    "GUEST_user  ",
    "  SysOp_Root ",
    "MaryK_2024   ",
    "   TECH_support",
    " BackupAdmin_01 ",
    "Kevin.Smith  ",
    "  NETWORK_ops",
    " DbManager_7 ",
    "   ITHelpDesk ",
    "SALLY_W  ",
    "  root_ACCESS ",
    " WebMaster_3",
    "FinanceUser_88   ",
    "  hr_Admin ",
    " Security_TEAM  ",
    "   devOps_Lead",
    "TempUser_100  ",
    "  Audit_Logger "
]

clean_users = [user.strip().lower() for user in flagged_users]
clean_users.sort()

for user in clean_users:
    print(user)