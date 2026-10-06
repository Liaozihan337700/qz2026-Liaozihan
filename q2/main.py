import json

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name: str, age: int) -> dict:
        if self.users:
            max_id = max(user["id"] for user in self.users)
            new_id = max_id + 1
        else:
            new_id = 1
        user = {
            "id": new_id,
            "name": name,
            "age": age
        }
        self.users.append(user)
        return user

    def get_user(self, user_id: int):
        for user in self.users:
            if user["id"] == user_id:
                return user
            else:
                return None

    def update_age(self, user_id: int, new_age: int) -> bool:
        user = self.get_user(user_id)
        if user is not None:
            user["age"] = new_age
            return True
        return False

    def remove_user(self, user_id: int) -> bool:
        user = self.get_user(user_id)
        if user is not None:
            self.users.remove(user)
            return True
        return False

    def list_users(self) -> list:
        return self.users.copy()

    def save_to_json(self, file_path: str):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(self.users, f, ensure_ascii=False, indent=2)

    def load_from_json(self, file_path: str):
        with open(file_path, "r", encoding="utf-8") as f:
            self.users = json.load(f)

if __name__ == "__main__":
    um = UserManager()
    print(um.add_user("张三", 18))
    print(um.add_user("李四", 20))
    print(um.get_user(1))
    print(um.get_user(99))
    print(um.update_age(1, 19))
    print(um.remove_user(2))
    print(um.remove_user(2))
    print(um.list_users())
    um.save_to_json("users.json")
    um2 = UserManager()
    um2.load_from_json("users.json")
    print(um2.list_users())