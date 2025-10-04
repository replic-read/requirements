#
# The pdf-files that are exported from figma have names based on their variants, that we can't change.
# This file contains a helper-script that renames the design files in './media/ui/ex/' and './media/ui/web/' to the names as referenced
#   in the .tex files.
#
# Script was only tested on linux.
#

import os

names_map_web = {
    "Account.pdf": "web-account.pdf",
    "AllAccounts_Expanded=No.pdf": "web-accounts-noconfig.pdf",
    "AllAccounts_Expanded=Yes.pdf": "web-accounts-config.pdf",
    "AllReplics_Expanded=No.pdf": "web-admin-replics-noconfig.pdf",
    "AllReplics_Expanded=Yes.pdf": "web-admin-replics-config.pdf",
    "AllReports_Expanded=No.pdf": "web-reports-noconfig.pdf",
    "AllReports_Expanded=Yes.pdf": "web-reports-config.pdf",
    "Login.pdf": "web-login.pdf",
    "OwnReplics_Expanded=No.pdf": "web-user-replics-noconfig.pdf",
    "OwnReplics_Expanded=Yes.pdf": "web-user-replics-config.pdf",
    "ServerConfig.pdf": "web-config.pdf",
    "Signup.pdf": "web-signup.pdf",
    "ViewReplic_Deactivated=No, ViewReplic_PasswordRequired=No.pdf": "web-replic-active.pdf",
    "ViewReplic_Deactivated=Yes, ViewReplic_PasswordRequired=No.pdf": "web-replic-inactive.pdf",
    "ViewReplic_Deactivated=No, ViewReplic_PasswordRequired=Yes.pdf": "web-replic-active-password.pdf",
    "EmailNotVerified.pdf": "web-email-not-verified.pdf",
    "EmailVerification_Success=No.pdf": "web-email-verification-error.pdf",
    "EmailVerification_Success=Yes.pdf": "web-email-verification-success.pdf"
}

names_map_ex = {
    "AccountMenu.pdf": "ex-account-menu.pdf",
    "AccountNotVerifiedInfo.pdf": "ex-account-not-verified.pdf",
    "ChangeEndpoint_Endpoint-set=No, ChangeEndpoint_logged-in=No.pdf": "ex-change-endpoint-none-logged-out.pdf",
    "ChangeEndpoint_Endpoint-set=Yes, ChangeEndpoint_logged-in=No.pdf": "ex-change-endpoint-present-logged-out.pdf",
    "ChangeEndpoint_Endpoint-set=Yes, ChangeEndpoint_logged-in=Yes.pdf": "ex-change-endpoint-present-logged-in.pdf",
    "CreateReplic_Expanded=No.pdf": "ex-create-replic-collapsed.pdf",
    "CreateReplic_Expanded=Yes.pdf": "ex-create-replic-expanded.pdf",
    "Login.pdf": "ex-login.pdf",
    "ReplicCreated.pdf": "ex-replic-created.pdf",
    "Signup.pdf": "ex-signup.pdf",
}

ui_dir = "../content/ui/"
web_dir = ui_dir + "web/"
ex_dir = ui_dir + "ex/"

def rename_files(dir, map):
    files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
    for filename in files:
        if filename in map:
            old_path = os.path.join(dir, filename)
            new_path = os.path.join(dir, map[filename])
            os.rename(old_path, new_path)

if __name__ == '__main__':
    rename_files(web_dir, names_map_web)
    os.system(f'cd {web_dir} && git add .')
    rename_files(ex_dir, names_map_ex)
    os.system(f'cd {ex_dir} && git add .')
