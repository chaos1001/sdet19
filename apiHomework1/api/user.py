import logging

from apiHomework1.api.base_api import BaseApi


class User(BaseApi):
    def add(self, user_id, user_name, department_id_list, **kwargs):
        data = {
            "userid": user_id,
            "name": user_name,
            "department": department_id_list
        }
        # mobile 和 email不能同时为空
        data.update(**kwargs)
        # 不要自动邀请
        data["to_invite"] = False

        r = self.send("POST", f"user/create?access_token={self.token}", json=data)
        logging.debug("add user result: {}".format(r.json()))
        return r

    def get(self, user_id):
        r = self.send("GET", f"user/get?access_token={self.token}&userid={user_id}")
        logging.debug("get user result: {}".format(r.json()))
        return r

    def update(self, user_id, **kwargs):
        """
        data参数：
        userid	是	成员UserID。对应管理端的帐号，企业内必须唯一。不区分大小写，长度为1~64个字节
        name	否	成员名称。长度为1~64个utf8字符
        alias	否	别名。长度为1-32个utf8字符
        mobile	否	手机号码。企业内必须唯一。若成员已激活企业微信，则需成员自行修改（此情况下该参数被忽略，但不会报错）
        department	否	成员所属部门id列表，不超过100个
        order	否	部门内的排序值，默认为0。当有传入department时有效。数量必须和department一致，数值越大排序越前面。有效的值范围是[0, 2^32)
        position	否	职务信息。长度为0~128个字符
        gender	否	性别。1表示男性，2表示女性
        email	否	邮箱。长度不超过64个字节，且为有效的email格式。企业内必须唯一。若是绑定了腾讯企业邮箱的企业微信，则需要在腾讯企业邮箱中修改邮箱（此情况下该参数被忽略，但不会报错）
        telephone	否	座机。由1-32位的纯数字、“-”、“+”或“,”组成
        is_leader_in_dept	否	上级字段，个数必须和department一致，表示在所在的部门内是否为上级。
        avatar_mediaid	否	成员头像的mediaid，通过素材管理接口上传图片获得的mediaid
        enable	否	启用/禁用成员。1表示启用成员，0表示禁用成员
        extattr	否	自定义字段。自定义字段需要先在WEB管理端添加，见扩展属性添加方法，否则忽略未知属性的赋值。与对外属性一致，不过只支持type=0的文本和type=1的网页类型，详细描述查看对外属性
        external_profile	否	成员对外属性，字段详情见对外属性
        external_position	否	对外职务，如果设置了该值，则以此作为对外展示的职务，否则以position来展示。不超过12个汉字
        nickname	否	视频号名字（设置后，成员将对外展示该视频号）。须从企业绑定到企业微信的视频号中选择，可在“我的企业”页中查看绑定的视频号
        address	否	地址。长度最大128个字符
        main_department	否	主部门
        """
        data = {
            "userid": user_id,
        }
        data.update(**kwargs)

        r = self.send("POST", f"user/update?access_token={self.token}", json=data)
        logging.debug("update user result: {}".format(r.json()))
        return r

    def delete(self, user_id):
        r = self.send("GET", f"user/delete?access_token={self.token}&userid={user_id}")
        logging.debug("delete user result: {}".format(r.json()))
        return r

    def user_is_not_exist(self, user_id):
        errcode = self.get(user_id).json().get("errcode")
        if errcode == 60111:
            return True
        else:
            return False
