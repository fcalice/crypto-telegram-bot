import json


class Users(object):
    def __init__(self, filename):
        self.filename = filename
        self.data = json.load(open(filename))

    @property
    def users(self):
        return self.data.keys()

    def __contains__(self, user_id):
        return str(user_id) in self.users

    def add(self, user_id, info=None):
        user_info = self.data.get(user_id, {})
        user_info.update(info or {})
        self.data[str(user_id)] = user_info
        json.dump(
            self.data, open(self.filename, "w"), sort_keys=True, indent=2
        )

    def __getitem__(self, user_id):
        return self.data.get(user_id)
