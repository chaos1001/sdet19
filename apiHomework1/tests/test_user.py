from apiHomework1.api.user import User
import logging


class TestUser:
    def setup_class(self):
        self.user = User()

    def test_add_user(self, get_unique_user_with_email):
        user_id, user_name, department_id_list, email = get_unique_user_with_email
        r = self.user.add(user_id, user_name, department_id_list, email=email)
        assert r.json().get("errcode") == 0

    def test_get_user(self):
        user_id = "YangChuChao"
        r = self.user.get(user_id)
        assert r.json().get("userid") == user_id

    def test_update_user(self, get_unique_user_with_email):
        user_id, user_name, department_id_list, email = get_unique_user_with_email
        self.user.add(user_id, user_name, department_id_list, email=email)

        updated_name = "{}{}".format(user_name, "改")
        logging.info(user_id)
        r = self.user.update(user_id, name=updated_name)
        assert r.json().get("errcode") == 0

    def test_delete_user(self, get_unique_user_with_email):
        user_id, user_name, department_id_list, email = get_unique_user_with_email
        self.user.add(user_id, user_name, department_id_list, email=email)

        r = self.user.delete(user_id)
        assert r.json().get("errcode") == 0
        assert self.user.user_is_not_exist(user_id)
