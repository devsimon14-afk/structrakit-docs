from structrakit import GuildDatabase, SetupWizard

database = GuildDatabase("data/welcome.db")
wizard = SetupWizard(name="welcome", title="Join/leave setup", database=database)
wizard.add_channel(key="join_channel", label="Join channel", required=True)
wizard.add_channel(key="leave_channel", label="Leave channel")
wizard.add_role(key="ping_role", label="Ping role")
wizard.add_boolean(key="enabled", label="Enabled", default=True)
wizard.add_text(key="join_message", label="Join message", max_length=1000)
wizard.add_text(key="leave_message", label="Leave message", max_length=1000)

